'''
Tuto utilisé : https://towardsdatascience.com/how-to-use-riot-api-with-python-b93be82dbbd6

Need riot api key dans le fichier api_key.py (meme path)

Libraries :
pandas
riotwatcher
'''

import sys
import pandas as pd
import riotwatcher

from test_functions import pull_data_test
from functions import Functions

# Put API key in file (not on git), DO NOT SHARE. Must be refreshed daily, or error 403
# https://developer.riotgames.com/
from api_key import api_key
print(api_key)

#pull_data_test(api_key, region='euw1', player_name='Patheman')

fc = Functions(api_key, region='euw1', player_name='Patheman')
fc.verif_algo()



print('--- END ---')