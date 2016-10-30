import praw
from OAuth2Util import OAuth2Util
import yaml


class AutomodRule:

    def __init__(self, text):
        self.plain_text = text
        self.type = None
        self.title = tuple()
        self.body = tuple()


class AutomodConfigParser:

    def __init__(self):
        self.r = praw.Reddit(user_agent="windows:AutomodConfigParser v0.1 by /u/Santi871")
        self._authenticate()

    def _authenticate(self):
        o = OAuth2Util(self.r)
        o.refresh(force=True)
        self.r.config.api_request_delay = 1

    def grab_automod_config(self, subreddit):
        page = self.r.get_wiki_page(subreddit, 'config/automoderator')
        print("parsing")
        print(list(yaml.load_all(page.content_md))[0])
        return page.content_md


am_configparser = AutomodConfigParser()
am_configparser.grab_automod_config('explainlikeimfive')

