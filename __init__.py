from mycroft import MycroftSkill, intent_file_handler


class Lightcontrol(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('lightcontrol.intent')
    def handle_lightcontrol(self, message):
        self.speak_dialog('lightcontrol')


def create_skill():
    return Lightcontrol()

