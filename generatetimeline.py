from stable import generate_image
import os


def create_folder(video):
    dirs = os.listdir(f'{video.get_path()}')
    if 'background' not in dirs:
        os.mkdir(fr'{video.get_path()}\background')


def main(video):
    create_folder(video)
    index = 1
    print(fr'GENERATING {len(video.get_timeline_description())} BACKGROUND IMAGES')
    if video.get_is_short():
        for image_description in video.get_timeline_description():

            generate_image(image_description,
                           fr'{video.get_path()}\background\img_{index}.png',
                           width=720,
                           height=1280,
                           steps=100)

            print(fr'IMAGE {index} / {len(video.get_timeline_description())} GENERATED')
            index += 1
    else:
        for image_description in video.get_timeline_description():

            generate_image(image_description, fr'{video.get_path()}\background\img_{index}.png',
                           width=1280,
                           height=720,
                           steps=100)

            print(fr'IMAGE {index} / {len(video.get_timeline_description())} GENERATED')
            index += 1
