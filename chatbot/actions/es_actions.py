from typing import Any, Text, Dict, List
from urllib import request
import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset

affirm = [
    'yes',
    'y',
    'indeed',
    'correct',
    'ya',
    'benar',
    'betul',
    'ok'
]

deny = [
    "no"
    "n"
    "never"
    "I don't think so"
    "don't like that"
    "no way"
    "not really"
    "tidak"
    "nggak"
    "nope"
    "bukan"
]

# Isi Expert System
class ActionEsCovid(Action):

    def name(self) -> Text:
        return "action_es_covid"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        values = [1]
        temp = []

        temp.append(tracker.get_slot('es_covid_1'))
        temp.append(tracker.get_slot('es_covid_2'))
        temp.append(tracker.get_slot('es_covid_3'))
        temp.append(tracker.get_slot('es_covid_4'))
        temp.append(tracker.get_slot('es_covid_5'))
        temp.append(tracker.get_slot('es_covid_6'))
        temp.append(tracker.get_slot('es_covid_7'))

        for n in temp :
            if n in affirm : 
                values.append(1)
            else:
                values.append(0)

        body = {'data' : [values]}

        r = requests.post(url = 'http://localhost:8080/es/covid', json = body)
        data = r.json()
        if r.status_code == 422 :
            message = data['detail'][0]['msg']
        else :
            if data['prediction'][0] == 1 :
                message = 'Sistem pakar kami memprediksi anda terkena Covid.\nApakah ada lagi yang bisa saya bantu?'
            elif data['prediction'][0] == 0:
                message = 'Sistem pakar kami memprediksi anda tidak terkena Covid.\nApakah ada lagi yang bisa saya bantu?'

        dispatcher.utter_message(text=message)

        return [AllSlotsReset()]