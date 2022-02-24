import sys
import pandas as pd
from riotwatcher import LolWatcher, ApiError

import helpers

def pull_data(api_key, region, player_name):
    print('hey')
    print(api_key)

    region_v5 = helpers.get_region_v5(region)
    watcher = LolWatcher(api_key)
    me = watcher.summoner.by_name(region, player_name)
    print(me)

    my_ranked_stats = watcher.league.by_summoner(region, me['id'])
    print(my_ranked_stats)

    # AttributeError: 'MatchApiV5' object has no attribute 'matchlist_by_account'
    #my_matches = watcher.match.matchlist_by_account(region, me['accountId'])
    my_matches = watcher.match.matchlist_by_puuid(region_v5, me['puuid'])
    print(my_matches)

    # fetch last match detail
    last_match = my_matches[0]
    match_detail = watcher.match.by_id(region_v5, last_match)
    print(match_detail)

    participants = []
    for row in match_detail['participants']:
        participants_row = {}
        participants_row['champion'] = row['championId']
        participants_row['spell1'] = row['spell1Id']
        participants_row['spell2'] = row['spell2Id']
        participants_row['win'] = row['stats']['win']
        participants_row['kills'] = row['stats']['kills']
        participants_row['deaths'] = row['stats']['deaths']
        participants_row['assists'] = row['stats']['assists']
        participants_row['totalDamageDealt'] = row['stats']['totalDamageDealt']
        participants_row['goldEarned'] = row['stats']['goldEarned']
        participants_row['champLevel'] = row['stats']['champLevel']
        participants_row['totalMinionsKilled'] = row['stats']['totalMinionsKilled']
        participants_row['item0'] = row['stats']['item0']
        participants_row['item1'] = row['stats']['item1']
        participants.append(participants_row)
    df = pd.DataFrame(participants)
    print(df)