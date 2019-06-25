import re
def remove_url(URL):
    URL1=re.sub(r'http\S+', 'httpaddr', URL)
    return(URL1)


