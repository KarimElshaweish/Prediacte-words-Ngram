from nltk.book import  *
from decimal import *
getcontext().prec= 2

word_lower=[w.lower() for w in text1]
tranning_single_word=[w for w in word_lower if w.isalpha()]
tranning_single_word_dict=dict()
for w in tranning_single_word:
    if w in tranning_single_word_dict:
        tranning_single_word_dict[w]+=1
    else:
        tranning_single_word_dict[w]=1
tranning_single_word_cnt=len(tranning_single_word)
tranning_single_word_prob_dict=dict()
for w in tranning_single_word_dict:
    tranning_single_word_prob_dict[w]=Decimal(Decimal(tranning_single_word_dict[w])/tranning_single_word_cnt)
tranning_pair_word=[(tranning_single_word[i],tranning_single_word[i+1]) for i in range(len(tranning_single_word)-1)]
tranning_pair_word_dict=dict()
for pair in tranning_pair_word:
    key=(pair[0],pair[1])
    if key in tranning_pair_word_dict:
        tranning_pair_word_dict[key]+=1
    else:
        tranning_pair_word_dict[key]=1
tranning_pair_word_cnt=len(tranning_pair_word)
tranning_pair_word_prob=dict()
for pair in tranning_pair_word_dict:
    tranning_pair_word_prob[pair]=Decimal(Decimal(tranning_pair_word_dict[pair])/tranning_pair_word_cnt)
tranning_3_word=[(tranning_single_word[i],tranning_single_word[i+1],tranning_single_word[i+2])
                 for i in range(len(tranning_single_word)-2)]
tranning_3_word_dict=dict()
for triple in tranning_3_word:
    key=(triple[0],triple[1],triple[2])
    if key in tranning_3_word_dict:
        tranning_3_word_dict[key]+=1
    else:
        tranning_3_word_dict[key]=1
tranning_3_word_dict_cnt=len(tranning_3_word)
tranning_3_word_dict_prob=dict()
for t in tranning_3_word_dict:
    tranning_3_word_dict_prob[t]=Decimal(tranning_3_word_dict[t]/tranning_3_word_dict_cnt)
tranning_4_word=[(tranning_single_word[i],tranning_single_word[i+1],tranning_single_word[i+2],tranning_single_word[i+3])
                 for i in range(len(tranning_single_word)-3)]
tranning_4_word_dict=dict()
for w in tranning_4_word:
    if w in tranning_4_word_dict:
        tranning_4_word_dict[w]+=1
    else:
        tranning_4_word_dict[w]=1
tranning_4_word_dict_prob=dict()
tranning_4_word_cnt=len(tranning_4_word)
for w in tranning_4_word_dict:
    tranning_4_word_dict_prob[w]=Decimal(tranning_4_word_dict[w]/tranning_4_word_cnt)
tranning_5_word=[(tranning_single_word[i],tranning_single_word[i+1],tranning_single_word[i+2],tranning_single_word[i+3],tranning_single_word[i+4])
                 for i in range(len(tranning_single_word)-4)]
tranning_5_word_dict=dict()
for w in tranning_5_word:
    if w in tranning_5_word_dict:
        tranning_5_word_dict[w]+=1
    else:
        tranning_5_word_dict[w]=1
tranning_5_word_dict_prob=dict()
tranning_5_word_cnt=len(tranning_5_word)
for w in tranning_5_word_dict:
    tranning_5_word_dict_prob[w]=Decimal(tranning_5_word_dict[w]/tranning_5_word_cnt)
#####################################################################################
def get_text_prob(text):
    text=text.split(' ')
    prob = tranning_single_word_prob_dict[text[0]]
    prob =chec_prob(prob)
    for i in range(len(text)-1):
        n=round(tranning_pair_word_prob[(text[i],text[i+1])],5)
        prob=chec_prob(prob)
        prob=n*prob
        n=chec_prob(round(tranning_single_word_prob_dict[text[-1]],5))
        prob=round(prob*n,5)
        prob=chec_prob(prob)
    return round(prob,5)

def chec_prob(prob):
    if(prob==Decimal(0)):
        return  Decimal(0.0001)
    else:
        return prob
def searach_next_word(word):
    gram2 = sorted(tranning_pair_word_dict.items(), key=lambda item: (item[0], -item[1]))
    #next_wrod=next((element[0][1] for element in gram2 if element[0][0]==word),None)
    next_word=dict()
    for element in  gram2:
        if element[0][0]==word:
            next_word[element[0][1]]=element[1]

    return next_word
def change_dict_value(dict_list):
    for key in dict_list:
        if dict_list[key] is None:
            dict_list[key]=0
    return  dict_list
def get_the_end_word(text):
    text=text.split(' ')
    return  text[-1]
def predicet(text,n):
    next_list=searach_next_word(get_the_end_word(text))
    sentance_dict=dict()
    for w in next_list:
        ntext=text+" "+w
        stext=ntext.split(' ')
        if(n==1):
            sentance_dict[w]=tranning_pair_word_prob.get((stext[0],stext[1]))
        elif(n==2):
            sentance_dict[w]=tranning_3_word_dict_prob.get((stext[0],stext[1],stext[2]))
        elif(n==4):
            sentance_dict[w]=tranning_5_word_dict_prob.get((stext[0],stext[1],stext[2],stext[3],stext[4]))
        elif(n==3):
            sentance_dict[w]=tranning_4_word_dict_prob.get((stext[0],stext[1],stext[2],stext[3]))
        else:
            break
    if(len(sentance_dict)==0):
        print("can't predicate")
        return
    sentance_dict=change_dict_value(sentance_dict)
    sentance_dict=sorted(sentance_dict.items(),key=lambda kv:kv[1],reverse=True)
   # print(text+" "+max(sentance_dict,key=lambda key:sentance_dict.values()))
    frist=True
    for w in sentance_dict:
        if(frist):
            print('the mose predciated one is:')
            print(text+" "+w[0])
            frist=False
            print("others:")
        else:
            print(text+" "+w[0])
    #print(sentance_dict)
   # print(max(sentance_dict,key=lambda key:sentance_dict[key]))

predicet('so am i',3)