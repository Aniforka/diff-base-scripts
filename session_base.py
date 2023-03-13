import requests
from fake_useragent import UserAgent

def create_session(random_user=True, proxy=None, ssl=None):
    session = requests.Session()

    if random_user:
        session.headers.update({
            'User-Agent': UserAgent().random
        })

    if proxy:
        session.proxies.update(proxy)

    if ssl:
        session.verify = ssl

    return session

def delete_session(session):
    session.close()