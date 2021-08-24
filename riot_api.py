from riotwatcher import LolWatcher
import os
key = os.environ['RITO_KEY']
watcher = LolWatcher(key)
usr_region = 'na1'

def printstats(summonername):
    k_lis = list()
    d_lis = list()
    a_lis = list()
    #this pulls information about summoner, pulls info "ID" then gets a list of matches based on their puuid
    summoner = watcher.summoner.by_name(usr_region, summonername)
    p_stats = watcher.league.by_summoner(usr_region, summoner["id"])
    matches = watcher.match_v5.matchlist_by_puuid("AMERICAS", summoner["puuid"])
    #this pulls the KDA of all matches availible to the API
    for i in range(len(matches)):
        spef_match = watcher.match_v5.by_id("AMERICAS", matches[i])
        info_match = dict(spef_match["info"])
        part_list = info_match["participants"]
        for i in range(len(part_list)):
            if part_list[i]["summonerName"] == summonername:
                k_lis.append(part_list[i]["kills"])
                d_lis.append(part_list[i]["deaths"])
                a_lis.append(part_list[i]["assists"])
            else:
                continue
    return p_stats,k_lis,d_lis,a_lis