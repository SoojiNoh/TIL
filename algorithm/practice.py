# parser.py
import requests
from bs4 import BeautifulSoup as bs

# 로그인할 유저정보를 넣어줍시다. (모두 문자열입니다!)
LOGIN_INFO = {
    'userId': 'thensj6873@gmail.com',
    'userPwd': 'ensuzyasm95^^'
}

# html = requests.get("https://edu.ssafy.com/edu/main/index.do").content

# Session 생성, with 구문 안에서 유지
with requests.Session() as s:
    # 우선 클리앙 홈페이지에 들어가 봅시다.
    # first_page = s.get('https://edu.ssafy.com/edu/main/index.do')
    # html = first_page.text
    # soup = bs(html, 'html.parser')
    # print(soup)
    # csrf = soup.find('meta', {'name': '_csrf'}) # input태그 중에서 name이 _csrf인 것을 찾습니다.
    # print(csrf['content']) # 위에서 찾은 태그의 content를 가져옵니다.

    # 이제 LOGIN_INFO에 csrf값을 넣어줍시다.
    # (p.s.)Python3에서 두 dict를 합치는 방법은 {**dict1, **dict2} 으로 dict들을 unpacking하는 것입니다.
    LOGIN_INFO = {**LOGIN_INFO, **{'_csrf': "9b837cc8-13b2-44b2-a02a-ed7e658ccf20"}}
    print(LOGIN_INFO)

    # 이제 다시 로그인을 해봅시다.
    login_req = s.post('https://edu.ssafy.com/comm/login/SecurityLoginCheck.do', data=LOGIN_INFO)
    # 어떤 결과가 나올까요? (200이면 성공!)
    print(login_req.status_code)

    # -- 여기서부터는 로그인이 된 세션이 유지됩니다 --
    # 이제 장터의 게시글 하나를 가져와 봅시다. 아래 예제 링크는 중고장터 공지글입니다.
    post_one = s.get('https://edu.ssafy.com/data/upload_files/crossUpload/openLrn/ebook/unzip/A2022012813080928300/index.html')
    soup = bs(post_one.text, 'html.parser') # Soup으로 만들어 줍시다.
    # 아래 CSS Selector는 공지글 제목을 콕 하고 집어줍니다.

    print(soup)
    # img = soup.select('img')
    # # HTML을 제대로 파싱한 뒤에는 .text속성을 이용합니다.
    # print(img) # 글제목의 문자만을 가져와봅시다.
