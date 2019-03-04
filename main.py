# -*- coding: utf-8 -*-
import time
import random
import sys

from plugins.config import CONFIGURATION
from plugins.bot import InstagramBot


if __name__ == "__main__":
    username = CONFIGURATION.config['Username']
    password = CONFIGURATION.config['Password']
    ig = InstagramBot(username, password)
    ig.login()
    hashtags = ['fun', 'drole', 'humour', 'blague', 'rigolade']
    while True:
        try:
            # Choose a random tag from the list of tags
            tag = random.choice(hashtags)
            ig.like_photo(tag)
        except Exception:
            ig.close_browser()
            time.sleep(60)
            ig = InstagramBot(username, password)
            ig.login()
