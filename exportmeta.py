def main(video):
    print(video)
    output_file = open(fr'{video.get_path()}\metadata.txt', 'w')
    output_file.write(f'{video.get_title()}\n')
    output_file.write(f'{video.get_description()}\n')
    output_file.write(f'{video.get_tags()}\n')
    output_file.write(f'{video.get_thumbnail_description()}\n')
    output_file.close()