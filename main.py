from tools import get_config
from stable import generate_image
from video import Video
import time
import createscript
import metadata
import timeline
import generatetimeline
import generatethumbnail
import audiogen
import createvideo
import exportmeta
from video import Video

PER_VIDEO_DELAY = 30 # 1800 = 30 mins // 30 = 30 seconds

def get_ideas(configs):
    ideas = []
    idea_list = open(configs['ideapath'], 'r')
    for idea in idea_list:
        ideas.append(idea.strip())
    return ideas

def main():
    generate_image("a test image", fr'test.png', steps=10)
    time.sleep(2)
    configs = get_config()
    ideas = get_ideas(configs)
    index = 0

    for idea in ideas:  # For every idea in the IDEA LIST
        print(f'GENERATING VIDEO {index+1} of {len(ideas)}')
        # BULK OF CODE GOES IN HERE
        working_video = Video(idea)  # Creates video folder and establishes the video class
        createscript.main(working_video)  # Writes script and saves as file
        metadata.main(working_video)  # Creates title, description, tags, and thumbnail description
        timeline.main(working_video)  # Creates background image generation
        generatetimeline.main(working_video)
        generatethumbnail.main(working_video)
        audiogen.main(working_video)
        createvideo.main(working_video)
        exportmeta.main(working_video)

        # INCREASES VIDEO COMPLETION COUNT

        index += 1

        # DELAY BETWEEN VIDEO TO COMPLY WITH CHAT-GPT RATE LIMITS

        time.sleep(PER_VIDEO_DELAY)

def main2():
    vid = Video('how ai will take over,essay,100,False')
    vid.set_script('this is a test\ntesting again\n')
    timeline.main(vid)
    generatetimeline.main(vid)



main()
