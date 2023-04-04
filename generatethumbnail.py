from stable import generate_image


def main(video):
    generate_image(video.get_thumbnail_description(), fr'{video.get_path()}\thumbnail.png', steps=65)
