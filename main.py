# -*- coding: utf-8 -*-
import time
import random
import sys

from plugins.bot import InstagramBot


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    max_sub = sys.argv[3]
    ig = InstagramBot(username, password)
    ig.login()
    hashtags = ['fun', 'drole', 'humour', 'blague', 'rigolade']
    while True:
        try:
            # Choose a random tag from the list of tags
            tag = random.choice(hashtags)
            ig.explore_tag(tag, max_sub)
            break
        except Exception:
            ig.close_browser()
            time.sleep(60)
            ig = InstagramBot(username, password)
            ig.login()
