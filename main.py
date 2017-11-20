import requests
import sys

r1 = requests.get('https://uber.com/')
r2 = requests.get('https://www.uber.com/')
r3 = requests.get('https://partners.uber.com/login')
r4 = requests.get('https://auth.uber.com/login/?next_url=https%3A%2F%2Fpartners.uber.com')


def handleanswer(request, resp, data):
    return request.post('https://auth.uber.com/login/handleanswer',
                        headers={'Content-Type': 'application/json', 'x-csrf-token': resp.headers['x-csrf-token']},
                        data=data,
                        cookies=resp.cookies)


r5 = handleanswer(requests, r4,
                  '{"answer":{"type":"VERIFY_INPUT_EMAIL","userIdentifier":{"email":"'
                  + sys.argv[1] + '"}},"init":true}')

r6 = handleanswer(requests, r5,
                  '{"answer":{"type":"VERIFY_PASSWORD","password":"' + sys.argv[2] + '"},"rememberMe":true}')

print(r6.status_code)
print(r6.text)
