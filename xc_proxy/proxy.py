import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import requests
from utils.redis import SetRedis
from utils import sleep

class Proxy(object):
    def __init__(self, **redis_cfg):
        self.container = SetRedis(**redis_cfg)

    def get(url):
        resp = requests.get(url)
        content = resp.content
        if not content:
            return None
        content = content.decode()
        content = content.split()
        return content

    def loop_save(t=10*60):
        while 1:
            proxies = get(URL)
            self.container.update(*proxies)
            sleep(t)