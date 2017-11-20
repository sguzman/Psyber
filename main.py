import requests


def get(request, scheme, host, path):
    return request.get(scheme + host + path, headers={'Host': host})


def printReq(request):
    print(r.status_code)
    print(r.text)


persistHeaders = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9'
}
for key in persistHeaders.keys():
    requests.Session().headers.update({key: persistHeaders[key]})

r = get(requests, 'https://', 'www.uber.com', '/')

printReq(r)