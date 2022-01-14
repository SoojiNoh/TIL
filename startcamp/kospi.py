from urllib import response
import requests
from bs4 import BeautifulSoup

#KOSPI
response = requests.get('https://finance.naver.com/sise/').text
bs = BeautifulSoup(response, 'html.parser').select_one('#KOSPI_now')
kospi = bs.text
print(kospi)

#환율
response02 = requests.get('https://finance.naver.com/marketindex/').text
usd = BeautifulSoup(response02, 'html.parser').select_one('#exchangeList > li.on > a.head.usd > div > span.value').text


print(usd)

