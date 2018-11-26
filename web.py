from flask import Flask, request, render_template
import mido
import time
import threading, Queue
from midinumpad import Toggler, MidiNumpad
from midicontroller import Midihost
from config import Config


global app
app = Flask("midicontroller")

@app.route('/cctoggle/<int:value>')
def control_toggle(value):
    toggled = app.config['toggler'].switch(str(value))
    message = mido.Message('control_change', control=value, value=toggled)
    app.config['command_q'].put(message)
    return str(message)

@app.route('/pcset/<int:value>')
def program_change(value):
    message = mido.Message('program_change', program=value)
    app.config['command_q'].put(message)
    return str(message)

@app.route('/ccset/<int:value>/<int:data>')
def control_set(value, data):
    message = mido.Message('control_change', control=value, value=data)
    app.config['command_q'].put(message)
    return str(message)


@app.route('/quit/')
def quit():
    app.config['command_q'].put("KILLSIGNAL")
    shutdown_server()
    return "QUIT"

@app.route('/')
def iframe():
    return render_template('iframe.html')

@app.route('/pc')
def pc():
    return render_template('pc.html')

@app.route('/cc')
def cc():
    return render_template('cc.html')

@app.route('/cclevel')
def cclevel():
    return render_template('level.html')

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

def start_midicontroller():
    global app
    command_q = Queue.Queue()

    mt = Midihost(command_q = command_q)
    mt.start()

    if 'numpad' in Config.MODULES:
        numpad = MidiNumpad(command_q)
        numpad.start()

    app.config['command_q'] = command_q
    app.config['toggler'] = Toggler()
    app.run(host=Config.SERVERNAME.split(':')[0], port=Config.SERVERNAME.split(':')[1])
    Config.shutdown()


if __name__ == '__main__':
    start_midicontroller()