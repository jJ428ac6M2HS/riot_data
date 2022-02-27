import sys
import pandas as pd
from riotwatcher import LolWatcher, ApiError

import helpers

def pull_data_test(api_key, region, player_name):
    print('hey')
    print(api_key)

    region_v5 = helpers.get_region_v5(region)
    watcher = LolWatcher(api_key)
    me = watcher.summoner.by_name(region, player_name)
    print('player profile')
    print(me)

    my_ranked_stats = watcher.league.by_summoner(region, me['id'])
    print('ranked stats')
    print(my_ranked_stats)

    # AttributeError: 'MatchApiV5' object has no attribute 'matchlist_by_account'
    #my_matches = watcher.match.matchlist_by_account(region, me['accountId'])
    #my_matches = watcher.match.matchlist_by_puuid(region_v5, me['puuid'])
    """
    On peut filtrer le type de match avec type ou queue : 
    https://developer.riotgames.com/apis#match-v5/GET_getMatchIdsByPUUID
    type='ranked' donne toutes les ranked flex+solo
    queue=420 donne la soloQ, 440 la flex
    https://static.developer.riotgames.com/docs/lol/queues.json
    """

    # On peut filtrer les ranked avec type (https://developer.riotgames.com/apis#match-v5/GET_getMatchIdsByPUUID)
    # On
    my_matches = watcher.match.matchlist_by_puuid(region_v5, me['puuid'], type='ranked')
    print('match history')
    print(my_matches)

    # fetch last match detail
    last_match = my_matches[8]
    match_detail = watcher.match.by_id(region_v5, last_match)
    print('match detail')
    print(match_detail)
    print(match_detail['metadata']['participants'])

    participants = []
    for row in match_detail['info']['participants']:
        participants_row = {}
        participants_row['puuid'] = row['puuid']
        participants_row['summonerId'] = row['summonerId']
        participants_row['summonerName'] = row['summonerName']
        participants_row['teamId'] = row['teamId']
        participants_row['win'] = row['win']
        print(participants_row)
        participants.append(participants_row)

    print(participants)
    df = pd.DataFrame(participants)
    print(df.to_string())
    print(df['teamId'].to_string())
    print(df['summonerName'].to_string())

    df_group = df.groupby(['teamId', 'win']).sum().reset_index()
    df_group = df_group[['teamId', 'win']]
    print(df_group)

