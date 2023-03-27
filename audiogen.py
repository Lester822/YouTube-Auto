from gtts import gTTS

def main(video):
    print('GENERATING AUDIO FILE')
    script = video.get_script()
    script = script.replace('\n', '')
    tts = gTTS(text=script, lang='en')
    tts.save(fr'{video.get_path()}\audio.mp3')
    print('AUDIO FILE GENERATED')