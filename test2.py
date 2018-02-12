from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://www.daum.net")
bs = BeautifulSoup(html,"html.parser")
namelist=bs.findAll("a",{"class":"link_issue","tabindex":"-1"})
for name in namelist:
    print(name.get_text())