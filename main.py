import random

data = []

with open("DATA/names.csv", "r") as fd:
    lines = fd.read().splitlines()
    data += lines

n = random.randint(0, 100)
extrax = ['.', '_', '-', 'the', 'and']

if n <= 10:
    P_1 = random.choice(data) + random.choice(extrax) + random.choice(data)
elif n in range(10, 36):
    P_1 = random.choice(data) + str(random.randint(1950, 2020))
elif n in range(36, 50):
    P_1 = random.choice(data) + random.choice(data)
elif n in range(50, 75):
    P_1 = random.choice(data) + random.choice(data) + str(random.randint(1950, 2020))
elif n in range(75, 100):
    P_1 = random.choice(data) + random.choice(data) + str(random.randint(1, 30)) + str(random.randint(1, 12))
else:
    P_1 = "Good luck next time"

domains = ["hotmail.com", "gmail.com", "aol.com", "mail.com", "mail.kz", "yahoo.com"]

n = random.randint(0, 100)

if n <= 50:
    P_2 = random.choice(domains)
else:
    P_2 = random.choice(data) + ".com"

domain_country = [".eu", ".ru", ".bru",
                  '.cn', '.de', '.tk',
                  '.uk', '.tw', '.fr',
                  '.br', '.vn', '.au', '.us']

m = random.randint(0, 100)

if m <= 50:
    account = P_1 + "@" + P_2
else:
    account = P_1 + "@" + P_2 + random.choice(domain_country)

print(account)

# Password generator

pass_list = []
with open("DATA/words.txt", "r") as fd:
    lines = fd.read().splitlines()
    pass_list += lines

password = random.choice(pass_list) + str(random.randint(10000, 9999999))
print(password)

