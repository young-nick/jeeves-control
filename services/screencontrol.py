from subprocess import call, check_output
from servicebase import ServiceBase

class ScreenControl(ServiceBase):

    def __init__(self):
        self.commands = {
            "On": ['sudo', 'tvservice', '-p'],
            "Off": ['sudo', 'tvservice', '-o'],
            "Check": ['sudo', 'tvservice', '-s']
        }

    def on(self):
        return call(self.commands['On'])

    def off(self):
        return call(self.commands['Off'])

    def toggle(self):

        if 'off' in check_output(self.commands['Check']):
            return call(self.commands['On'])
        else:
            return call(self.commands['Off'])
