def get_config(configpath='config.txt'):
    """Return a dictonary of various configs with their results from the config path which is default CONFIG.TXT"""
    lines = []
    config_file = open(configpath, 'r')
    for line in config_file:
        lines.append(line.strip())
    config_file.close()

    configs = {}

    # EVERYTHING BELOW IS ESTABLISHING DICTIONARY!
    configs['ideapath'] = lines[0][12:]
    configs['output_path'] = lines[1][15:]
    return configs

def clean_text(text):
    cleaned = text
    bad_characters = ['/', fr'\'', ':', '*', '?', '"', '<', '>', '|']
    for character in bad_characters:
        cleaned = cleaned.replace(character, '')
    return cleaned
