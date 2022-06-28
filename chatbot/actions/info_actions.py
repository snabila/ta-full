from email import message_from_binary_file
from typing import Any, Text, Dict, List
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset

class ActionDiseaseInfo(Action):

    def name(self) -> Text:
        return "action_disease_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        penyakit = tracker.get_slot('penyakit_apa')
        info = tracker.get_slot('informasi_apa').lower()
        message = ''
        
        r = requests.get(url = 'http://localhost:8080/infod/n/' + penyakit)
        data = r.json()

        if r.status_code == 200:
            message = "Maaf kami tidak mempunyai informasi mengenai penyakit " + penyakit
        
            if info in 'penjelasan':
                message = data['overview']
            elif info in 'gejala' : 
                message = data['symptoms']
            elif info in 'kapan harus menemui dokter':
                message = data['when_to_see_doctor']
            elif info in 'penyebab':
                message = data['causes']
            elif info in 'faktor resiko':
                message = data['risk_factors']
            elif info in 'komplikasi':
                message = data['complication']
            elif info in 'pencegahan':
                message = data['prevention']
        else:
            message = 'Mohon maaf, kami tidak dapat menemukan informasi mengenai ' + info + ' ' + penyakit

        if message == '':
            dispatcher.utter_message(text='Mohon maaf, kami tidak dapat menemukan informasi mengenai ' + info + ' ' + penyakit)
        else :
            dispatcher.utter_message(text=message)

        return [AllSlotsReset()]