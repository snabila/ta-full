# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from email import message
from email.errors import MessageError
from typing import Any, Text, Dict, List
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

class ActionOpiniBantu(Action):

    def name(self) -> Text:
        return "action_opini_bantu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        temp = tracker.get_slot('opini_bantu')
        
        if temp in affirm :
            message = 'Senang bisa membantu! Anda bisa membantu dalam pengembangan chatbot ini dengan mengisi form feedback pada link dibawah dan jelaskan pengalaman Anda.\n\n[link]'
        else:
            message = 'Mohon maaf atas ketidaknyamanannya, Anda bisa membantu dalam pengembangan chatbot ini dengan mengisi form feedback pada link dibawah dan jelaskan pengalaman Anda.\n\n[link]'

        dispatcher.utter_message(text=message)

        return [AllSlotsReset()]

# class ActionApakahBantu(Action):

#     def name(self) -> Text:
#         return "action_apakah_bantu"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         temp = tracker.get_slot('bantu_lagi')
        
#         if temp in affirm :
#             message = 'Senang bisa membantu! Anda bisa membantu dalam pengembangan chatbot ini dengan mengisi form feedback pada link dibawah dan jelaskan pengalaman Anda.\n\n[link]'
#         else:
#             message = 'Senang bisa membantu! Anda bisa membantu dalam pengembangan chatbot ini dengan mengisi form feedback pada link dibawah dan jelaskan pengalaman Anda.\n\n[link]'

#         dispatcher.utter_message(text=message)

#         return [AllSlotsReset()]