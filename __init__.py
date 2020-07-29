from mycroft import MycroftSkill, intent_file_handler, intent_handler
from adapt.intent import IntentBuilder
from os.path import dirname, abspath
from .light import set, off, fade

#these are redundant as they are listed in both the light.py file and here
#this is just lazy coding on my part, they are the pin numbers
red_front = 16
green_front = 20
blue_front = 27

red_back = 22
green_back = 21
blue_back = 17


class Lightcontrol(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)


#in the initialize defenitton i create the events that read the message bus for the ready message
#and read for the wake word message
    def initialize(self):
        self.add_event('mycroft.ready', self.handler_mycroft_ready)
        self.add_event('recognizer_loop:wakeword', self.handler_wakeword)


    @intent_handler(IntentBuilder("colorChangeIntent").require("location").require("color"))
    def handle_turn_on_lights_intent(self, message):
        if message.data["location"].upper() == "FRONT LIGHTS":
            light.set(message.data["location"].upper(), message.data['color'])

        if message.data["location"].upper() == "BACK LIGHTS":
            light.set(message.data["location"].upper(), message.data['color'])

        if message.data["location"].upper() == "BOTH LIGHTS":
            light.set(message.data["location"].upper(), message.data['color'])

        self.speak_dialog('deskcontrol')

    @intent_handler(IntentBuilder("").require('powerOff').require('location'))
    def handle_turn_off_lights_intent(self, message):
        light.off(message.data['location'].upper())
        self.speak_dialog('deskcontrol')

#this code fades white when the code word is reconginzed
    def handler_wakeword(self, message):
        fade(blue_back, blue_front)

#this function causes the lights to fade red when ready to go
    def handler_mycroft_ready(self, message):
        fade(red_back,red_front)

def create_skill():
    return Lightcontrol()

