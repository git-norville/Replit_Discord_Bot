import os
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
import matplotlib.pyplot as plt
import riot_api
from riot_api import *

def create_pi(sumnam,stats):
    feed_list = {"feeding":0,"didn't feed":0}
    KDA_list = list()
    nothing_list = {"feeding":0,"didn't feed":0}
    stats = list()
    kills = list()
    deaths = list()
    assists = list()
    stats, kills, deaths, assists = printstats(sumnam)
    print(stats,kills,deaths,assists)

    for i in range(len(kills)):
        #I put this here incase the value is zero
        try:
            kda = round((kills[i] + assists[i]) / deaths[i], 2)
            KDA_list.append(kda)
        except:
            KDA_list.append(float(kills[i] + assists[i]))
    
    for i in range(len(KDA_list)):
        if KDA_list[i] >= 3.0:
            feed_list["didn't feed"] +=1
    else:
        feed_list["feeding"] +=1
    print(feed_list)
    mylabels = ["fed", "didn't feed"]
    plt.pie(feed_list.values(), labels= mylabels,autopct='%1.1f%%', startangle=15,)
    plt.title(sumnam + " do you feed?")
    plt.legend()
    plt.axis('equal')
    plt.savefig('dyf.png')
    plt.clf()
    
    return stats