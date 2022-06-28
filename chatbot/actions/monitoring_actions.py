from typing import Any, Text, Dict, List
# import config
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset

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
class ActionMonitHapusList(Action):
    def name(self) -> Text:
        return "action_monit_hapus_list"

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

        if r.status_code == 200 :
            message = 'Anda berhasil membatalkan pendaftaran pada monitoring ' + monit_kode + '.' 
        else:
            message = 'Mohon maaf terjadi kesalahan pada server'

        dispatcher.utter_message(text=message)


        return [AllSlotsReset()]