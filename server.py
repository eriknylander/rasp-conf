from bottle import route, run, get, post, request, static_file
from subprocess import call
import os
import sys

@route('<path:path>')
def server_static(path):
    return static_file(path, root='./static')

@route('/')
def main():
    return static_file("index.html", root='./static/')

CURRENT_AUDIO = 1
HDMI_AUDIO = 2
HEADPHONE_JACK_AUDIO = 1

@get('/audio_device')
def getAudioDevice():
    return getAudioDeviceString(CURRENT_AUDIO)

@post('/audio_device')
def setAudioDevice():
    body = request.json
    newAudioDevice = int(body["deviceNumber"])
    validDeviceNumber = checkDeviceNumber(newAudioDevice)
    if validDeviceNumber:
        global CURRENT_AUDIO
        CURRENT_AUDIO = newAudioDevice
        print("Setting audio device " + str(newAudioDevice))
        os.system("amixer cset numid=3 " + str(newAudioDevice))
    return "Set audio to: " + getAudioDeviceString(newAudioDevice)    

def getAudioDeviceString(input):
    if input == HDMI_AUDIO:
        return "HDMI audio"
    elif input == HEADPHONE_JACK_AUDIO:
        return "Headphone jack audio"

def checkDeviceNumber(number):
    if number != HDMI_AUDIO and number != HEADPHONE_JACK_AUDIO:
        return False
    else:
        return True

if len(sys.argv) < 2:
    host = "localhost"
else:
    host = sys.argv[1]
 
run(host=host, port=8080, debug=True)
