import requests
import os

def downloadSdf(zinc_id, loc): 
    # zinc id is like this ZINC000000002614
    #try:
        url = f"https://zinc.docking.org/substances/{zinc_id}.sdf"
        res = requests.get(url)
        if (res.status_code == 200):
            with open(f'{loc}/{zinc_id}.sdf', 'wb') as f:
                f.write(res.content)
            print(f'SDF file for {zinc_id} saved successfully.')
            return True
        else:
            print(f'Error downloading SDF file for {zinc_id}.')
            return False
    #except:
    #    print(f'Error downloading SDF file for {zinc_id}.')
    #    return False


zincId = []
downloaded = list(map(lambda x : x[:-4], os.listdir('estrogen - data/erDecoy')))
notDownloaded = []

with open('estrogen - data/ERdecoys.txt') as f:
    zincId = list(map(lambda x : x.strip().split()[0], f.readlines()))

path = 'estrogen - data/erDecoy'
for nm in zincId:
    if nm not in downloaded and downloadSdf(nm, path):
        downloaded.append(nm)
    else:
        notDownloaded.append(nm)
    print(f"{len(downloaded)} / {len(zincId)}", end='\r')
