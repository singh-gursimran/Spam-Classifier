from wordstem import stem_word
spam_path="C://Users//Experty//Desktop//spam//spamlist.txt"
ff= open(spam_path)
s_data= ff.readlines()
s_data= ''.join(s_data)
s_data=stem_word(s_data)
def ind(t):
    k = []
    for i in s_data:
        if i in t:
            k.append(1)
        else:
            k.append(0)
    return k
