from RealtimeSTT import AudioToTextRecorder
from text_processing import text_processing
# https://github.com/KoljaB/RealtimeSTT?tab=readme-ov-file#configuration


keywords = [ # list of all possible interpretations of the word echo
    'echo','eco','eko', 'ecko',
    'hecho','heco', 'heko', 'hecko', 'ecos',
    'ecou', 'ecoute',
]

if __name__ == '__main__':
    def recording_started():
        print("Speak now...")

    def recording_finished():
        print("Speech end detected... processing...")
    
    while True:
        # alexa, americano, blueberry, bumblebee, computer, grapefruits, grasshopper, hey google, hey siri, jarvis, ok google, picovoice, porcupine, terminator
        wake_word = 'hey google'
        # https://github.com/KoljaB/RealtimeSTT?tab=readme-ov-file#training-models
        recorder = AudioToTextRecorder(spinner=True, model="medium", compute_type='float32', language="en", wake_words=wake_word, on_wakeword_detected=recording_started, on_recording_stop=recording_finished)
        print(f'Say "{wake_word}".')
        text_processing(recorder.text())
        print("Done.")