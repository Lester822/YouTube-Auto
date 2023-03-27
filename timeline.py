from chatgpt import chat_gpt


def background_image_prompt_generator(text):
    #inquiry = f'Create a three sentence highly descriptive visual description to be fed into an AI art generator to create a good background image to be shown while this is said in a YouTube video: {text}'
    inquiry = fr'Write a three sentence hyper-detailed one paragraph description to be fed into an AI art generator for an eye-catching background, Have sentence one declare the foreground, sentence two declare the background, and fill in extra details with the third sentence. Make sure it is releveant to a video with this script and make sure the design does not rely on any text or speech bubbles, for a YouTube video while this is being said: {text}'
    return chat_gpt(inquiry)


def main(video):
    descriptions = []
    for line in video.get_script().split('\n'):
        if line != '\n' and line != '' and line != ' ':
            prompt = background_image_prompt_generator(line)
            descriptions.append(prompt)
    video.set_timeline_description(descriptions)