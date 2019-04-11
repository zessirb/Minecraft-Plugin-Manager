import os
import re
import urllib


class Install:

    def __init__(self, input):
        self.input = input
        self.is_url = False
        self.is_path = False
        self.process_input()

    def process_input(self):
        url_regex = '(https?|ftp)://(-\.)?([^\s/?\.#-]+\.?)+(/[^\s]*)?$'
        path_regex = '\\w/\\w'
        self.is_url = True if re.match(url_regex, self.input) else False
        self.is_path = True if re.match(path_regex, self.input) else False
        # TODO : Raise exception if input is neither url nor path

    def download_plugin(self):
        if not os.path.exists('mods'):
            os.mkdir('mods')
        if self.is_url:
            urllib.request.urlretrieve(self.input, './mods/' + os.path.basename(self.input))

