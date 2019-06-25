import re

def nem(str):
    temp=str
    email = re.findall(r'\w+@\w+.com',temp)
    for em in email:
        t=temp.replace(em,'emailaddr')
        temp=t
    return temp

