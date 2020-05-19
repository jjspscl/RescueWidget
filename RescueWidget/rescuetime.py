import requests
import json

from pprint import pprint

class RescueTime:
    url = "https://www.rescuetime.com/anapi/"

    def __init__(self, key):
        super(RescueTime, self).__init__()
        self.key = key

    def daily_summary(self):
        url = f'{self.url}daily_summary_feed'
        res = requests.get(
               url,
               params = {'key': self.key})
        return json.loads(res.text)

    def analytics(self):
        url = f'{self.url}data'
        res = requests.get(
           url,
           params={'key': self.key,
                   'rk': 'productivity',
                   'pv': 'member',
                   'format': 'json'})
        return json.loads(res.text)
