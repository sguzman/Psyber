import requests
import sys

r1 = requests.get('https://uber.com/')
r2 = requests.get('https://www.uber.com/')
r3 = requests.get('https://partners.uber.com/login')
r4 = requests.get('https://auth.uber.com/login/?next_url=https%3A%2F%2Fpartners.uber.com')

head1 = {'Content-Type': 'application/json', 'x-csrf-token': r4.headers['x-csrf-token']}
r5 = requests.post('https://auth.uber.com/login/handleanswer',
         headers=head1,
         data='{"answer":{"type":"VERIFY_INPUT_EMAIL","userIdentifier":{"email":"' + sys.argv[1] + '"}},"init":true}',
         cookies=r4.cookies)

head2 = {'Content-Type': 'application/json', 'x-csrf-token': r5.headers['x-csrf-token']}
r6 = requests.post('https://auth.uber.com/login/handleanswer',
         headers=head2,
         data='{"answer":{"type":"VERIFY_PASSWORD","password":"' + sys.argv[2] + '"},"rememberMe":true}',
         cookies=r5.cookies)

print(r6.status_code)
print(r6.text)