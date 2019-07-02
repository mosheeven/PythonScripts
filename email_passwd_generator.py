import urllib
import string
import random
import json


def randomPassword(name):
    chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    passwd = ''.join(random.choice(chars) for i in range(8)) + name
    return passwd


def createRandomEmail(name):
    name_extra_digit = ''.join(random.choice(string.digits))
    name_extra_hexdigit = ''.join(random.choice(string.hexdigits))
    rand_email = name + name_extra_digit + name_extra_hexdigit + '@gmail.com'

    return rand_email


names = json.loads(open('random_names_list.json').read())
rnd_name = random.choice(names)

print('Username:' + createRandomEmail(rnd_name))
print('Password:' + randomPassword(rnd_name))

