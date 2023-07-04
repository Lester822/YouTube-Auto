from chatgpt import chat_gpt


def create_prompt(video):
    if video.get_is_short() == False:
        if video.get_vid_type().lower() == 'essay':
            prompt = f'You are "AI Recon" a fully automated YouTube channel that creates video essays about topics. You only write factual information, however, you do insert funny remarks, you have a fun YouTuber personality, and can insert made up stories treating them as real to help get your point across.\nEverything you write is going to be fed directly into a Text to Speech reader without any edits, so be sure that the output is clean and doesnt include any details or headers. DO NOT INCLUDE MUSIC DETAILS. DO NOT INCLUDE VISUALS THAT SHOULD BE SHOWN. DO NOT PUT "AI RECON:" AT THE BEGINNING OF EACH PARAGRAPH.DO NOT LABEL THE VARIOUS SECTIONS OR INTO\nEstablishing that... write a {video.get_word_count()} word YouTube video script for a video essay about the topic: {video.get_idea()}. In the format "PARAGRAPH 1\nPARAGRAPH 2\nETC'
        else:
            raise Exception('Invalid video type')
    else:
        if video.get_vid_type().lower() == 'essay':
            prompt = f'Create a voiceover script for a YouTube short that is 30 seconds or less, that doesnt have any headers or visual descriptions, just the voiceover, the focus of the videos should be: {video.get_idea()}'
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
