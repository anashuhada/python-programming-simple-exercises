import re

s = "My Profile: https://www.pavanonlinetrainings.com/about.html and My Blog: https://www.pavantestingtools.com/"

pattern = r'https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&/=]*)'

urls = re.findall(pattern, s)
print(urls)
