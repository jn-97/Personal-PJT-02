import string, random

# Get ascii Characters numbers and punctuation (minus quote characters as they could terminate string).
# 시크릿 키 만들기 
chars = ''.join([string.ascii_letters, string.digits, string.punctuation]).replace('\'', '').replace('"', '').replace('\\', '')

SECRET_KEY = ''.join([random.SystemRandom().choice(chars) for i in range(50)])

print(SECRET_KEY)