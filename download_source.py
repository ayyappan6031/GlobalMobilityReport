from tqdm import *
import requests
class SourceDownlaod:
    def downloadsourcefile(self):
        try:
            f = open('Global_Mobility_Report.csv')
        except:
            url = "https://www.gstatic.com/covid19/mobility/Global_Mobility_Report.csv"
            name = 'Global_Mobility_Report.csv'
            with requests.get(url, stream=True) as r:
                r.raise_for_status()
                with open(name, 'wb') as f:
                    pbar = tqdm(total=int(r.headers['Content-Length']))
                    for chunk in r.iter_content(chunk_size=8192):
                        if chunk:  # filter out keep-alive new chunks
                            f.write(chunk)
                            pbar.update(len(chunk))
        finally:
            f.close()

SourceDownlaod().downloadsourcefile()