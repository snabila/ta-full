from typing import Any, Text, Dict, List
from datetime import datetime as dt
import requests
import json
from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset, SlotSet, EventType
from rasa_sdk.types import DomainDict

# settings = config.Settings()

# Daftar form
class ActionMonitDaftar(Action):
    def name(self) -> Text:
        return "action_monit_daftar"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Ambil input kode monitoring dan username
        monit_kode = tracker.get_slot('monit_kode')
        uname = tracker.sender_id

        # Cek monitoring dengan kode yang diinput ada atau nggak
        r = requests.get(url = 'http://localhost:8080/monit/code/' + monit_kode)

        # Kalau ada (status 200)
        if r.json()['code'] == 200 :
            # Kalau usernya udah terdaftar, kabarin
            if uname in r.json()['data'][0]['participants']:
                message = 'Anda sudah terdaftar pada kode monitoring ' + monit_kode

            # Kalau user belum terdaftar
            else:
                # Update list subscribe di service user
                r = requests.put(url = 'http://localhost:8003/api/subs-add', json = { 'code' : monit_kode, 'uname' : uname })

                # Update list subscribe di service monitoring
                r2 = requests.put(url = 'http://localhost:8080/monit/code/' + monit_kode + '/push', json = { 'username' : uname })

                if r.status_code == 401 :
                    message = 'Unauthorized'
                elif r.status_code == 200 :
                    message = 'Berhasil menambahkan monitoring ' + monit_kode + ' pada akun ' + uname
                else:
                    message = "Maaf, terdapat error pada server. Harap mencoba beberapa saat lagi"
        # Kalau kode monitoring tidak ditemukan
        else:
            message = 'Monitoring dengan kode ' + monit_kode + ' tidak ditemukan.'

        dispatcher.utter_message(text=message)

        return [AllSlotsReset()]

# List subscribed
class ActionMonitList(Action):
    def name(self) -> Text:
        return "action_monit_list"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        uname = tracker.sender_id

        global listFound
        listFound = []

        r = requests.get(url = 'http://localhost:8003/api/subs-list', json = {'uname': uname})

        if r.status_code == 200 :
            subs_list = r.json()['subscribed']

            if subs_list:
                message = 'Berikut daftar monitoring yang anda terdaftar'

                for code in subs_list:
                    message = message + '\n- ' + code
                    listFound.append(code)

            else:
                message = 'Anda tidak terdaftar pada monitoring manapun.' 

        else:
            message = 'Mohon maaf terjadi kesalahan pada server'
        
        dispatcher.utter_message(text=message)


        return [AllSlotsReset()]

# 
class AskMonitKode2(Action):
    def name(self) -> Text:
        return "action_ask_monit_kode_2"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        if listFound :
            dispatcher.utter_message(text='Masukkan kode monitoring yang Anda mau:')
        else: 
            SlotSet('monit_kode_2', 'nonefound')
        return []

class ValidateMonitForm2(FormValidationAction):
    def name(self) -> Text:
        return "validate_monit_form_2"

    def validate_monit_kode_2(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if listFound:
            return {'monit_kode_2': slot_value}
        else:
            return {'monit_kode_2': 'nonefound'}

# Hapus form
class ActionMonitHapusAct(Action):
    def name(self) -> Text:
        return "action_monit_hapus_act"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        if listFound:
            monit_kode = tracker.get_slot('monit_kode_2')
            uname = tracker.sender_id

            if monit_kode in listFound:
                r = requests.put(url = 'http://localhost:8003/api/subs-pull', json = { 'code' : monit_kode, 'uname' : uname })
                r2 = requests.put(url = 'http://localhost:8080/monit/code/' + monit_kode + '/pull', json = { 'username' : uname })
                r3 = requests.delete(url = 'http://localhost:8080/record/code/' + monit_kode + '/' + uname)

                if r.status_code == 200 :
                    message = 'Anda berhasil membatalkan pendaftaran pada monitoring ' + monit_kode + '.' 
                else:
                    message = 'Mohon maaf terjadi kesalahan pada server'
            else:
                message = 'Anda tidak terdaftar pada monitoring ' + monit_kode
        else:
            message = 'Anda tidak terdaftar pada monitoring manapun.'

        dispatcher.utter_message(text=message)

        return [AllSlotsReset()]

# Isi form
class ActionMonitIsi(Action):
    def name(self) -> Text:
        return "action_monit_isi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        if listFound:
            # initialize disini biar gak kereset tiap nanya pertanyaan
            global answers
            answers = []

            global codeFound
            global subsFound
            global qFound

            global qLoop
            qLoop = 1

            # ambil kode monitoring dari form sebelumnya (monit_form)
            global monit_kode_isi
            monit_kode_isi = tracker.get_slot('monit_kode_2')

            if monit_kode_isi in listFound:
                subsFound = True

                # get request buat dapet teks pertanyaannya
                r = requests.get(url = 'http://localhost:8080/monit/code/' + monit_kode_isi + '/q')

                # kalo nemu kode monitoringnya
                if r.json()['code'] == 200:
                    codeFound = True

                    # tes data pertanyaannya ada nggak
                    global questions
                    questions = r.json()['data'][0]

                    # kalo ada set codeFound jadi true
                    if (questions):
                        qFound = True
                    else:
                        qFound = False
                else:
                    codeFound = False
                    qFound = False
            else:
                subsFound = False

        return [AllSlotsReset()]

class AskMonitIsiLoop(Action):
    def name(self) -> Text:
        return "action_ask_monit_isi_loop"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        if listFound:
            if subsFound:
                if codeFound:
                    if qFound:
                        message = questions[qLoop-1]['question']
                        # dispatcher.utter_message(text=questions[qLoop-1]['question'])
                    else:
                        message = 'Kode monitoring ' + monit_kode_isi + ' tidak memiliki pertanyaan.'
                else:
                    message = 'Kode monitoring ' + monit_kode_isi + ' tidak ditemukan.'
            else:
                message = "Anda tidak terdaftar di monitoring " + monit_kode_isi
        else:
            message = 'Anda tidak terdaftar di monitoring manapun.'
            SlotSet('monit_isi_loop', 'done')

        dispatcher.utter_message(text=message)
        return []

class ValidateMonitIsiForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_monit_isi_form"

    def validate_monit_isi_loop(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        global qLoop

        if listFound:
            if subsFound:
                if codeFound:
                    if qFound:
                        if qLoop == len(questions):
                            answers.append({
                                "q_id": questions[qLoop-1]['id'],
                                "answer": tracker.get_slot('monit_isi_loop')
                            })
                            return {'monit_isi_loop': slot_value}
                        else:
                            answers.append({
                                "q_id": questions[qLoop-1]['id'],
                                "answer": tracker.get_slot('monit_isi_loop')
                            })
                            qLoop += 1
                            return {'monit_isi_loop': None}
        else:
            return {'monit_isi_loop': 'done'}

class ActionMonitIsiSubmit(Action):
    def name(self) -> Text:
        return "action_monit_isi_submit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        if listFound:
            if subsFound:
                if codeFound:
                    if qFound:
                        uname = tracker.sender_id
                        submit_time = dt.now().astimezone().replace(microsecond=0).isoformat()

                        r = requests.post(url = 'http://localhost:8080/record', json = { 
                            'user' : uname,
                            'submit_time' : submit_time,
                            'qs_code' : monit_kode_isi,
                            'answers' : answers
                        })

                        if (r.status_code == 200):
                            message = 'Record baru berhasil disimpan.'
                        else:
                            message = 'Terjadi kesalahan pada server'
        #         else:
        #             message = 'Kode monitoring ' + monit_kode_isi + ' tidak memiliki pertanyaan.'
        #     else:
        #         message = 'Kode monitoring ' + monit_kode_isi + ' tidak ditemukan.'
        # else:
        #     message = 'Anda tidak terdaftar di monitoring manapun.'

                dispatcher.utter_message(text=message)

        return [AllSlotsReset()]    