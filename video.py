from tools import get_config, clean_text
import os

class Video:
    def __init__(self, idea):
        split_idea = idea.split(',')
        self._idea = clean_text(split_idea[0])
        self._vid_type = split_idea[1]
        self._word_count = int(split_idea[2])
        if split_idea[3].strip() == 'True':
            self._is_short = True
        else:
            self._is_short = False
        print(split_idea[3])
        print(self._is_short)
        self._title = ''
        self._description = ''
        self._tags = ''
        self._hashtags = ''
        self._script = ''
        self._path = self.generate_path()
        self._thumb_description = ''
        self._timeline_description = None

    def generate_path(self):
        configs = get_config()
        current_files = os.listdir(f'{configs["output_path"]}')
        if self._idea[:35] not in current_files:
            os.mkdir(fr'{configs["output_path"]}\{self._idea[:35]}')
        else:
            print('PROJECT FILE ALREADY CREATED')
        return fr'{configs["output_path"]}\{self._idea[:35]}'

    def get_idea(self):
        return self._idea

    def set_idea(self, idea):
        self._idea = idea

    def get_vid_type(self):
        return self._vid_type

    def set_vid_type(self, vid_type):
        self._vid_type = vid_type

    def get_word_count(self):
        return self._word_count

    def set_word_count(self, word_count):
        self._word_count = word_count

    def get_is_short(self):
        return self._is_short

    def set_is_short(self, is_short):
        self._is_short = is_short

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def get_tags(self):
        return self._tags

    def set_tags(self, tags):
        self._tags = tags

    def get_hashtags(self):
        return self._hashtags

    def set_hashtags(self, hashtags):
        self._hashtags = hashtags

    def get_script(self):
        return self._script

    def set_script(self, script):
        self._script = script

    def get_path(self):
        return self._path

    def set_path(self, path):
        self._path = path

    def get_thumbnail_description(self):
        return self._thumb_description

    def set_thumbnail_description(self, thumbnail_description):
        self._thumb_description = thumbnail_description

    def get_timeline_description(self):
        return self._timeline_description

    def set_timeline_description(self, timeline_description):
        self._timeline_description = timeline_description

    def __repr__(self):
        return f'Video({self._idea},{self._vid_type},{self._word_count},{self._is_short})'

    def __str__(self):
        return f'{self._idea}'
