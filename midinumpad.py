import mido
from subprocess import call
from itertools import cycle
import threading, Queue
import keyboard

class Toggler(object):
    items = {}

    def switch(self, item):
        if not item in self.items:
            self.items.update({item: True}) #default toggle mode
        else:
            self.items[item] = not self.items[item]
        return self.to_number_value(self.items[item])

    def to_number_value(self, item):
        if item:
            return 127
        else:
            return 0

class MidiNumpad():
    def __init__(self, command_q):
        self.command_q = command_q
        self.toggler = Toggler()
        self.modes = cycle(('PC', 'CC', 'LEVEL'))
        self.mode = next(self.modes)
        self.memory = {}
        self.last = None
        
    def stop_signal(self):
        keyboard.unhook_all()
        self.command_q.put("KILLSIGNAL")

    def start(self):
        keyboard.on_press(self.receive_message)
        keyboard.add_word_listener('987', self.stop_signal, triggers=['0'], match_suffix=True, timeout=2)

    def _send_message(self, message):
        self.command_q.put(message)

    def _set_level(self, key, operator):
        v = self.memory[key]
        temp = eval(str(v) + ' ' + operator + ' 13')
        if temp < 0:
            temp = 0
        elif temp > 127:
            temp = 127
        self.memory[key] = temp
        return temp

    def _should_execute_level_set(self, event):
        return self.last and self.mode == 'LEVEL' and (event.name == '+' or event.name == '-')


    def _adjust_event_value(self, event):
        try:
            value = int(event.name)
            if value == 0:
                value += 1
        except ValueError:
            if event.scan_code == 96 or event.name == ',': # switching with a toe, not so accurate
                value=2
            else:
                value = None
        return value

    def _generate_message(self, value):
        message = None
        if self.mode == 'CC':
            message = mido.Message('control_change', control=value, value=self.toggler.switch(value))
        if self.mode == 'LEVEL':
            level_cc = str(value + 10)
            self.last = level_cc
            if not level_cc in self.memory:
                self.memory[level_cc] = 26
            message = mido.Message('control_change', control=int(level_cc), value=self.memory[level_cc])
        if self.mode == 'PC':
            message = mido.Message('program_change', program=int(value)-1)
        return message

    def _switch_mode(self, event):
        if event.scan_code == 71:
            self.mode = 'PC'
        elif event.scan_code == 75:
            self.mode = 'CC'
        elif event.scan_code == 67:
            self.mode = 'LEVEL'
        print '\nMode change to ' + self.mode

    def receive_message(self, event):
        print "scan_code: " + str(event.scan_code)
        if event.scan_code == 69:
            pass
            #call("setleds -D +num", shell=True)
        if event.scan_code == 71 or event.scan_code == 75 or event.scan_code == 67:
            self._switch_mode(event)
        value = self._adjust_event_value(event)
        if value and value >= 0 and value <= 127:
            self._send_message(self._generate_message(value))
        if self._should_execute_level_set(event):
            message = mido.Message('control_change', control=int(self.last), value=self._set_level(self.last, event.name))
            self._send_message(message)


if __name__ == '__main__':
    print 'record keys until esc'
    print 'prints out key name and scan code'
    recorded = keyboard.record(until='esc')
    for keypress in recorded:
        
        print keypress.name + " " + str(keypress.scan_code)         