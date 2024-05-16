import requests

url='https://www.zhipin.com/wapi/zpgeek/search/joblist.json'
data = {"scene":"1","query":"项目运营主管","city":"101020100","experience":"","payType":"","partTime":"","degree":"","industry":"","scale":"","stage":"","position":"","jobType":"","salary":"","multiBusinessDistrict":"","multiSubway":"","page":"1","pageSize":"30"}
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}

response = requests.get(url=url, params=data, headers = headers)

text = response.text
with open('t.html', 'w', encoding='utf-8') as fb:
    fb.write(text)
# print(text)