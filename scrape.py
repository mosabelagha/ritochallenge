import requests
import time
from datetime import datetime
import os

requests.packages.urllib3.disable_warnings()

def convertEpoch(timestamp):
    epoch_start = datetime(1970,1,1)
    epoch = (timestamp - epoch_start).total_seconds()
    return epoch

def curls(timestamp):
    req = 'https://na.api.pvp.net/api/lol/na/v4.1/game/ids?beginDate=' + str(timestamp) + '&api_key=1c692a41-8f5a-4360-bc7e-5c86dd323a91'
    r = requests.get(req, verify=False)
    return r

t = datetime.now() # Get the time right now
t = t.replace(second = 0, microsecond = 0)
if (t.minute % 5 != 0):
    newminute = t.minute - (t.minute % 5)
    t = t.replace(minute=newminute)

epoch = convertEpoch(t)
os.mkdir(t.strftime('matches/%Y-%m-%d_%H-%M'))
for i in range(0, 96):
    epoch -= 300
    req = curls(int(epoch))
    time.sleep(1)
    txt_file = open(('matches/' + t.strftime('%Y-%m-%d_%H-%M') + '/' + str(int(epoch)) + '.json'), 'w')
    txt_file.write(str(req.json()))
    print(str(i+1) + "/96 files retrieved")

