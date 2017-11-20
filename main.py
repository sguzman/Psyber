import requests


def get(request, method, scheme, host, path, querystring=None, data=None):
    schemehost = scheme + host
    schemehostpath = schemehost + path
    schemehostpathquery = schemehostpath + ('?' + querystring if querystring else '')
    return request.request(method, schemehostpathquery, headers={'Host': host}, allow_redirects=False, data=data)


def printreq(request):
    print(request.status_code)
    print(request.text)


persistHeaders = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Upgrade-Insecure-Requests': '1',
    'Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9'
}
for key in persistHeaders.keys():
    requests.Session().headers.update({key: persistHeaders[key]})

r1 = get(requests, 'GET', 'https://', 'uber.com', '/')
r2 = get(requests, 'GET', 'https://', 'www.uber.com', '/')
r3 = get(requests, 'GET', 'https://', 'partners.uber.com', '/login')

requests.Session().headers.update({'X-Csrf-Token': r3.headers['X-Csrf-Token']})
requests.Session().headers.update({'Accept': 'application/json'})

r4 = get(requests, 'GET', 'https://', 'auth.uber.com', '/login/', 'next_url=https%3A%2F%2Fpartners.uber.com')
r5 = get(requests, 'POST', 'https://', 'auth.uber.com', '/login/handleanswer', data='{"answer":{"type":"VERIFY_INPUT_EMAIL","userIdentifier":{"email":"guzmansalv@gmail.com"}},"init":true}')
requests.Session().headers.update({'X-Csrf-Token': r4.headers['X-Csrf-Token']})

printreq(r5)
