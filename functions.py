import sys
import pandas as pd
from riotwatcher import LolWatcher, ApiError

from helpers import Helpers

class Functions(Helpers):
    def __init__(self, api_key, region, player_name):
        self.api_key = api_key
        self.region = region
        self.region_v5 = Helpers.get_region_v5(self.region)
        self.player_name = player_name
        self.watcher = LolWatcher(api_key)


    def get_match_history_by_name(self, player_name, soloQ_only=True):
        player = self.watcher.summoner.by_name(self.region, player_name)

        if soloQ_only:
            match_history = self.watcher.match.matchlist_by_puuid(self.region_v5, player['puuid'], queue=420)
        else:
            match_history = self.watcher.match.matchlist_by_puuid(self.region_v5, player['puuid'])

        return match_history


    ###########################################################
    #                       Main program                      #
    ###########################################################

    def verif_algo(self):
        print('######### MAIN ########')
        print(self.api_key)
        print(self.player_name)
        print(self.region)

        match_history = self.get_match_history_by_name(self.player_name)
        print(match_history)
