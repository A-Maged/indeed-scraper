import Cookie
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def get_cookie():
  try:
    query = 'https://www.indeed.com/jobs?q=marketing&l=New+York,+NY&radius=100&jt=contract&start=980'
    s = requests.Session()
    r = s.get(query, headers ={'Accept': 'text/html,application','Connection': 'close'}  ,verify=False )
    cookie = r.headers.get('Set-Cookie')

    parsed_cookie = [
      parse_cookie(cookie,'CTK'),
      parse_cookie(cookie,'ctkgen'),
      parse_cookie(cookie,'JSESSIONID'),
      parse_cookie(cookie,'INDEED_CSRF_TOKEN'),
      parse_cookie(cookie,'BIGipServerjob')
     ]

    cookie ='CTK=1b7ojajfa5ou4f7e'+"; ctkgen="+parsed_cookie[1]+'; JSESSIONID='+parsed_cookie[2]+'; INDEED_CSRF_TOKEN='+parsed_cookie[3]+'; BIGipServerjob_iad='+parsed_cookie[4]

    return cookie
  except Exception as e:
    if 'HTTPSConnectionPool' in str(e):
      print '[-]check your internet connection'
    return False

def parse_cookie(cookie_value, attripute):
  if cookie_value == False:
    print '[-]there\'s problems parsing the cookie'
    return False

  cookie = Cookie.SimpleCookie()
  cookie.load(cookie_value)
  parsed = cookie[attripute].value
  return parsed
