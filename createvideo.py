from moviepy.editor import AudioFileClip, ImageClip, concatenate_videoclips, CompositeAudioClip
import os

def main(video):
    audio_file = AudioFileClip(fr'{video.get_path()}\audio.mp3')
    audio_length = audio_file.duration
    background_images = []
    images = os.listdir(fr'{video.get_path()}\background')
    image_count = len(images)
    for image in images:
        temp_clip = ImageClip(fr'{video.get_path()}\background\{image}').set_duration(audio_length/image_count)
        background_images.append(temp_clip)
    concat_clip = concatenate_videoclips(background_images, method='compose')
    concat_clip.audio = CompositeAudioClip([audio_file])
    concat_clip.write_videofile(fr'{video.get_path()}\video.mp4', fps=30)

