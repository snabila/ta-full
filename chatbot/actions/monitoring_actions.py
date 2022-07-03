from os import uname
from typing import Any, Text, Dict, List
# import config
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormValidationAction
from rasa.core.actions.action import ActionListen
from rasa.core.actions.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset, FollowupAction, SlotSet

# settings = config.Settings()

# Daftar form
class ActionMonitDaftar(Action):
    def name(self) -> Text:
        return "action_monit_daftar"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        monit_kode = tracker.get_slot('monit_kode')
        uname = tracker.sender_id

        r = requests.get(url = 'http://localhost:8080/monit/code/' + monit_kode)

        if r.status_code == 200 :
            r = requests.put(url = 'http://localhost:8003/api/subs-add', json = { 'code' : monit_kode, 'uname' : uname })
            r2 = requests.put(url = 'http://localhost:8080/monit/code/' + monit_kode + '/push', json = { 'username' : uname })

            if r.status_code == 401 :
                message = 'Unauthorized'
            elif r.status_code == 200 :
                message = 'Berhasil menambahkan monitoring ' + monit_kode + ' pada akun ' + uname
            else:
                message = "Maaf, terdapat error pada server. Harap mencoba beberapa saat lagi"
        else:
            message = 'Monitoring dengan kode ' + monit_kode + ' tidak ditemukan. ' + uname

        dispatcher.utter_message(text=message)


        return [AllSlotsReset()]

# Hapus form 1 : list
class ActionMonitList(Action):
    def name(self) -> Text:
        return "action_monit_list"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        uname = tracker.sender_id

        r = requests.get(url = 'http://localhost:8003/api/subs-list', json = {'uname': uname})

        if r.status_code == 200 :
            subs_list = r.json()['subscribed']

            if subs_list:
                message = 'Berikut daftar monitoring yang anda terdaftar'

                for code in subs_list:
                    message = message + '\n- ' + code
            else:
                message = 'Anda tidak terdaftar pada monitoring manapun.' 
        else:
            message = 'Mohon maaf terjadi kesalahan pada server'

        dispatcher.utter_message(text=message)


        return [AllSlotsReset()]

# Hapus form 2 : hapus
class ActionMonitHapusAct(Action):
    def name(self) -> Text:
        return "action_monit_hapus_act"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        monit_kode = tracker.get_slot('monit_kode')
        uname = tracker.sender_id

        r = requests.put(url = 'http://localhost:8003/api/subs-pull', json = { 'code' : monit_kode, 'uname' : uname })
        r2 = requests.put(url = 'http://localhost:8080/monit/code/' + monit_kode + '/pull', json = { 'username' : uname })

        if r.status_code == 200 :
            message = 'Anda berhasil membatalkan pendaftaran pada monitoring ' + monit_kode + '.' 
        else:
            message = 'Mohon maaf terjadi kesalahan pada server'

        dispatcher.utter_message(text=message)


        return [AllSlotsReset()]

# Isi form
class ActionMonitIsi(Action):
    def name(self) -> Text:
        return "action_monit_isi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global tes
        tes = []
        monit_kode = tracker.get_slot('monit_kode')
        uname = tracker.sender_id

        r = requests.get(url = 'http://localhost:8080/monit/code/' + monit_kode + '/q')

        if (r.status_code == 200):
            questions = r.json()['data'][0]
            if (questions):
                i = 0
                message = 'Input :'

                for question in questions:
                    if (i > 1) : 
                        tes.append(tracker.latest_message['text'])

                    dispatcher.utter_message(text=question['question'])

                    i += 1

                    return [FollowupAction('action_monit_isi_form')]
                    
                    # return [FollowupAction(name = 'action_monit_isi_form')]
                    # tes.append(tracker.latest_message['text'])
                    # tes.append(tracker.get_slot('monit_isi_loop'))
                    # SlotSet('monit_isi_loop', None)
                tes.append(tracker.latest_message['text'])

                for test in tes:
                    message = message + '\n- ' + test
                
                dispatcher.utter_message(text=message)
        else:
            dispatcher.utter_message(text='Mohon maaf terjadi kesalahan pada server')

        return [AllSlotsReset()]

class ActionMonitIsiForm():
    def name(self) -> Text:
        return "action_monit_isi_form"

    def requiredslot():
        return ['monit_isi_loop']

    def submit():
        return [SlotSet('monit_isi_loop', None), FollowupAction('action_monit_isi')]

class ValidActionMonitIsiForm(FormValidationAction):
    def name(self) -> Text:
        return "action_monit_isi_form_valid"

    async def required_slots(
        self,
        domain_slots: List[Text],
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: "DomainDict",
    ) -> List[Text]:
        monit_kode = tracker.get_slot('monit_kode')
        r = requests.get(url = 'http://localhost:8080/monit/code/' + monit_kode + '/q')

        if (r.status_code == 200):
            questions = r.json()['data'][0]
            if (questions):
                for question in questions:
                    dispatcher.utter_message(text=question['question'])
                    
        additional_slots = ["outdoor_seating"]


        if tracker.slots.get("outdoor_seating") is True:
            # If the user wants to sit outside, ask
            # if they want to sit in the shade or in the sun.
            additional_slots.append("shade_or_sun")

        return additional_slots + domain_slots