import subprocess
import os
# sudo -E  python installSelenium.py 
def install_module(module):
    if subprocess.run(f"pip show {module}", shell=True, capture_output=True, text=True).returncode != 0:
        subprocess.run(f"pip install {module}", shell=True)
 
def installGecko():
    install_module("bs4"), install_module("requests"), install_module("wget")
    from bs4 import BeautifulSoup
    import requests
    import wget
    soup = BeautifulSoup(requests.get('https://github.com/mozilla/geckodriver/releases').content, 'html.parser')
    refs = soup.find_all('a')
    match = "linux64.tar.gz"
    url = None
    for a in refs:
        # print(a)
        # break
        if a['href'][-len(match):] == match:
            url = "https://github.com" + a['href']
    if url:
        print(f"downloading {url}")
        filename = wget.download(url, out='/usr/local/bin/')
        run = subprocess.run(f"tar -xf {filename} -C /usr/local/bin/", shell=True, capture_output=True)
        if run.returncode != 0:
            print("failed to untar")
            print(run.stderr)
        # os.rename(filename, '/usr/local/bin/geckodriver')
    # else: 
    #     raise()

if not os.path.isfile("/usr/local/bin/geckodriver"):
    installGecko()
