import re
from urllib.request import urlopen

url = input("Enter a website to scan: (include http(s)://)\n")

website = urlopen(url).read().decode('utf8')

print()
print("Phone Numbers:")
print(re.findall(r"((?:\d{3}|\(\d{3}\))?(?:\s|-|\.)?\d{3}(?:\s|-|\.)\d{4})",website))
print()
print("Emails:")
print(re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",website))
