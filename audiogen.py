import pyttsx3
from gtts import gTTS

def main(video):
    print('GENERATING AUDIO FILE')
    script = video.get_script()
    script = script.replace('\n', '')
    tts = gTTS(text=script, lang='en-uk', slow=False)
    tts.save(fr'{video.get_path()}\audio.mp3')
    print('AUDIO FILE GENERATED')


from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer

def main3(video):
    print('GENERATING AUDIO FILE')
    #script = video.get_script()
    #script = script.replace('\n', '')
    script = 'This is AI Recon, youre favorite YouTuber who talks about AI and other shit'
    path = fr"C:\Users\sasta\PycharmProjects\autoYouTube\venv\Lib\site-packages\TTS\.models.json"

    model_manager = ModelManager(path)

    model_path, config_path, model_item = model_manager.download_model("tts_models/en/ljspeech/hifigan_v2")

    voc_path, voc_config_path, _ = model_manager.download_model(model_item["default_vocoder"])

    syn = Synthesizer(
        tts_checkpoint=model_path,
        tts_config_path=config_path,
        vocoder_checkpoint=voc_path,
        vocoder_config=voc_config_path
    )
    outputs = syn.tts(script)
    syn.save_wav(outputs, fr"audio.mp3")
    #syn.save_wav(outputs, fr"{video.get_path()}\audio.mp3")

def main34(video):
    converter = pyttsx3.init(driverName='sapi5')
    converter.setProperty('rate', 150)
    converter.setProperty('volume', 0.7)
    voices = converter.getProperty('voices')
    index = 1
    for voice in voices:
        print(voice, voice.id)
        converter.setProperty('voice', voice.id)
        converter.save_to_file(video, f"voices/{str(index)}a.mp3")
        converter.runAndWait()
        index += 1

    print('test')