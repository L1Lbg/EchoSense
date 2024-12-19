from RealtimeSTT import AudioToTextRecorder
# pip install RealtimeSTT
# https://github.com/KoljaB/RealtimeSTT?tab=readme-ov-file#configuration

def process_text(text):
    print(text)

if __name__ == '__main__':
    recorder = AudioToTextRecorder(language='fr', model='large-v2', compute_type='float32', post_speech_silence_duration=1)
    while True:
        recorder.text(process_text)