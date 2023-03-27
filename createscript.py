from chatgpt import chat_gpt


def create_prompt(video):
    if video.get_is_short() == False:
        if video.get_vid_type().lower() == 'essay':
            prompt = f'Write a {video.get_word_count()} word YouTube script without any headers for sections for a video essay about the topic: {video.get_idea()}'
        else:
            raise Exception('Invalid video type')
    else:
        if video.get_vid_type().lower() == 'essay':
            prompt = f'Write a short YouTube shorts script that starts with "This entire video was created by an AI" with a really catchy and obvious hook that asks a question without any headers for sections that wont take longer than 20 seconds for a tts reader to read for a video explaining the topic: {video.get_idea()}'
        else:
            raise Exception('Invalid video type')

    return prompt


def main(video):
    prompt = create_prompt(video)
    output = chat_gpt(prompt)
    video.set_script(output)
    output_file = open(fr'{video._path}\script.txt', 'w')
    output_file.write(output)
    output_file.close()
