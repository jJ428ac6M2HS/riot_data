
class Helpers:
    def get_region_v5(region_v4):
        '''
        Cette API a deux codifications pour les régions, une pour v4 et une pour v5.

        old = ["na1", "euw1", "eun1", "kr", "br1", "jp1", "ru", "oc1", "tr1", "la1", "la2"]
        new = ["europe", "asia", "americas"]

        :param region_v4: Nom de la région en format v4
        :return:
        '''

        if region_v4 in ["euw1", "eun1", "ru", "tr1"]:
            return 'europe'
        if region_v4 in ["na1", "br1", "la1", "la2"]:
            return 'americas'
        if region_v4 in ["kr", "jp1", "oc1"]:
            return 'asia'
