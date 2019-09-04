from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet


#自定义的action 必须继承Action 并且重写run 方法

class ActionAskWeather(Action):
    def name(self):
        return 'action_ask_weather'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(f'您问的天气地点是哪里呢')
        return [SlotSet('city', '深圳')]
