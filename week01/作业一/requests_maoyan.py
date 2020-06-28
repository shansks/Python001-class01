import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url = "https://maoyan.com/films?showType=3"

payload = {}
headers = {
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
  'Cookie': 'uuid_n_v=v1; uuid=39FC6F70B85411EAA94453F28D7995DF30374A1B311048A9B8C0900DBC5F4AFA; _csrf=e6b5b20adff4d4b71bf4303351c7d78324a1cf5dc7d7c26de74a65faab1d5b13; mojo-uuid=fbe505445402c37757b6d1cf54e300ff; mojo-session-id={"id":"68b4e93fa43ec9f1946a096fc70c9af9","time":1593248253216}; _lxsdk_cuid=172f4ff1214c8-0cd354d6e5c9a9-3b634504-1fa400-172f4ff1214c8; _lxsdk=39FC6F70B85411EAA94453F28D7995DF30374A1B311048A9B8C0900DBC5F4AFA; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593248257,1593248489; mojo-trace-id=3; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593249934; __mta=108402749.1593248261085.1593248489433.1593249934442.3; _lxsdk_s=172f4ff1215-ae3-ce5-b41%7C%7C6'
}

response = requests.request("GET", url, headers=headers, data = payload)

# print(response.text.encode('utf8'))

bs_info = bs(response.text,'html.parser')
# print(bs_info)
movie_file = open('movie_infos.csv','a+',encoding='utf-8')
movie_file.write('电影名,电影类型,上映时间\r')
count = 0
for tag in bs_info.find_all('div',attrs={'class':'movie-hover-title'}):
	title = tag.get('title')
	if tag.find('span',).text == '类型:':
		type = (tag.text).replace('\n','').replace(' ','').strip('类型:')
		movie_file.write(title+','+type+',')
	if tag.find('span',).text == '上映时间:':
		date = (tag.text).replace('\n','').replace(' ','').strip('上映时间:')
		movie_file.write(date+'\r')
	count += 1
	if count == 40:
		break
movie_file.close()