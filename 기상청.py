from bs4 import BeautifulSoup
import urllib.request as req
import os.path
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

# download Url
url = 'http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=159'
savename = '/Users/song/project/크롤링/forecast.xml'

if not os.path.exists(savename):
    req.urlretrieve(url, savename)
    # print('다운로드 확인')

xml = open(savename, 'r', encoding='utf-8').read()
soup = BeautifulSoup(xml, 'html.parser')

#지역확인
info = {}
for location in soup.find_all('location'):
    loc = location.find('city').string
    # print(loc)
    weather = location.find_all('tmn')
    # print(weather)
    if not (loc in info):
        info[loc] = [] #중복 피하기
    for tmn in weather:
        info[loc].append(tmn.string)
print(info.keys())
print(list(info.keys()))
print(info.values())



with open('/Users/song/project/크롤링/forecast.txt', 'wt',  encoding="utf-8") as f:
    for loc in sorted(info.keys()):
        print("+",loc)
        f.write(str(loc)+'\n')
        for n in info[loc]:
            print('-', n)
            f.write('\t'+str(n) +'\n')

# info = {}
# for location in soup.find_all("location"):
#     loc = location.find('city').string
#     weather = location.find_all('tmn')
#     #print(weather)
#     if not (loc in info):
#         info[loc] = []
#     for tmn in weather:
#         info[loc].append(tmn.string)

#print(info)

# 각 지역의 날씨 출력
# with open('/Users/song/project/크롤링/forecast.txt', "wt", encoding="utf-8") as f:
#     for loc in sorted(info.keys()):
#         print("+", loc)
#         f.write(str(loc)+'\n')
#         for name in info[loc]:
#             print(" - ", name)
#             f.write('\t'+str(name)+'\n')
