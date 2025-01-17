from RealtimeSTT import AudioToTextRecorder
from scripts.assistant_audio.text_processing  import text_processing
from scripts.assistant_audio.tts import text_to_speech
from scripts.os.openapp import openapp
from scripts.os.closeapp import closeapp
import serial
import json


#arduino = serial.Serial(port='COM3', baudrate=9600, timeout=0.1)


# 0: red, 1: blue, 2: yellow, 3: green, 4: off
# red: error/not ready yet
# blue: hearing
# yellow: processing
# green: answer is ready (put black to blue after all is done)

def send_to_arduino(state):
    # arduino.write(state.encode())
    print(state)

def recording_started():
        print("Speak now...")
        send_to_arduino(1)

def recording_finished():
    print("Speech end detected... processing...")
    send_to_arduino(2)

def process_actions(actions:list):    
    functions = { 
        'openapp':{
            'function':openapp
        },
        'closeapp':{
            'function':closeapp
        }
    }
    
    for action in actions:
        try:
            functions[action['action']](action['parameter'])
        except:
            pass   

keywords = [ # list of all possible interpretations of the word echo
    'echo','eco','eko', 'ecko',
    'hecho','heco', 'heko', 'hecko', 'ecos',
    'ecou', 'ecoute',
]

if __name__ == '__main__':
    send_to_arduino(0)   
    
    while True:
        # alexa, americano, blueberry, bumblebee, computer, grapefruits, grasshopper, hey google, hey siri, jarvis, ok google, picovoice, porcupine, terminator
        wake_word = 'computer'
        # winget install Gyan.FFmpeg
        # sudo apt update && sudo apt install ffmpeg
        # https://github.com/KoljaB/RealtimeSTT?tab=readme-ov-file#training-models
        recorder = AudioToTextRecorder(spinner=True, model="medium", compute_type='float32', language="en", wake_words=wake_word, on_wakeword_detected=recording_started, on_recording_stop=recording_finished)
        print(recorder.text())
        processed_text = text_processing(recorder.text())
        print(processed_text)
        try:
            processed_text = json.loads(processed_text)
        except: continue

        # speak
        print('converting to wav')
        text_to_speech(processed_text['text'])
        print('ended converting to wav')

        send_to_arduino(3)

        # load the instructions
        process_actions(processed_text['actions'])




        send_to_arduino(1)