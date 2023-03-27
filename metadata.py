from chatgpt import chat_gpt


def generate_title(video):
    prompt = fr'Create a catchy YouTube title in the format "AI [Explains OR Discusses]: MAIN TOPIC" for a YouTube video with the script: {video.get_script()}'
    return chat_gpt(prompt)


def generate_tags(video):
    prompt = fr'Create a list of tags and buzzwords related to a YouTube video in the format "TERM 1,TERM 2,TERM 3,ETC": {video.get_script()}'
    return chat_gpt(prompt)


def generate_thumbnail_description(video):
    prompt = fr'Write a three sentence, one paragraph, with no headers or indicators of foreground and background, hyper-detailed description to be fed into an AI art generator for an eye-catching thumbnail for a YouTube video. Have sentence one declare the foreground, sentence two declare the background, and fill in extra details with the third sentence. Make sure it is releveant to a video with this script and make sure the design does not rely on any text or speech bubbles: {video.get_script()}'
    response = chat_gpt(prompt)
    return response


def generate_description(video):
    prompt = fr'Create a seven sentence catchy YouTube description paragraph, using keywords and buzzwords related to the script, for a YouTube video with the script: {video.get_script()}'
    return chat_gpt(prompt)


def main(video):
    video.set_title(generate_title(video))
    video.set_description(generate_description(video))
    video.set_tags(generate_tags(video))
    video.set_thumbnail_description(generate_thumbnail_description(video))
