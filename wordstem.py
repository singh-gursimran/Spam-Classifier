from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

#stemming fuction
def stem_word(data):
    ps = PorterStemmer()
    words = word_tokenize(data)
    t=[]
    for w in words :
        tt= (ps.stem(w))
        t.append(tt)

    return (t)

