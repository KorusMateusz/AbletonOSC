import os
import sys
import tempfile
import Live
import json
from functools import partial
from typing import Tuple, Any
import logging
logger = logging.getLogger("abletonosc")

from .handler import AbletonOSCHandler

class BrowserHandler(AbletonOSCHandler):
    def __init__(self, manager):
        super().__init__(manager)
        self.class_identifier = "browser"
        logger.info("loaded browser handler")


    def init_api(self):
        def get_browser_clips(self):
            return 
        self.osc_server.add_handler("/live/browser/test", lambda _: ("test",))
        self.osc_server.add_handler("/live/browser/test1", partial(self._get_property, "browser", "clips"))



    def clear_api(self):
        super().clear_api()
        try:
            self.song.remove_current_song_time_listener(self.current_song_time_changed)
        except:
            pass
