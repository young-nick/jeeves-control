from subprocess import call, check_output
from servicebase import ServiceBase

class ScreenControl(ServiceBase):

    def __init__(self):
        self.commands = {
            "On": ['sudo', 'vcgencmd', 'display_power', '1'],
            "Off": ['sudo', 'vcgencmd', 'display_power', '0'],
        }
        self.state = 'On'

    def on(self):
	self.state = 'On'
        return call(self.commands['On'])

    def off(self):
	self.state = 'Off'
        return call(self.commands['Off'])

    def toggle(self):

        if self.state == 'Off':
            self.state = 'On'
            return call(self.commands['On'])
        else:
            self.state = 'Off'
            return call(self.commands['Off'])
