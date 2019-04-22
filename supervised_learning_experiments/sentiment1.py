from nltk.corpus import opinion_lexicon
from nltk.tokenize import treebank
import pandas as pd
import numpy
#import nltk
#nltk.download('opinion_lexicon')

def importd():
    df = pd.read_csv("DC.csv")
    title = df["name"]
    description = df["description"]
    df["namepos"] = 0
    df["nameneg"] = 0
    df["nametotal"] = 0
    df["despos"] = 0
    df["desneg"] = 0
    df["destotal"] = 0
    for index,row in df.iterrows():
        rownum = index
        title1 = row["name"]
        ##print(type(title1))
        des1 = row["description"]
        try:
            posnum1 = posopinion(title1)
            print(posnum1)
            negnum1 = negopinion(title1)
            totnum1 = neuopinion(title1)
            posnum2 = posopinion(des1)
            print(posnum2)
            negnum2 = negopinion(des1)
            totnum2 = neuopinion(des1)
            df.loc[rownum,"namepos"]=posnum1
            df.loc[rownum,"nameneg"] =negnum1
            df.loc[rownum,"nametotal"] = totnum1
            df.loc[rownum,"despos"] = posnum2
            df.loc[rownum,"desneg"] = negnum2
            df.loc[rownum,"destotal"] = totnum2
        except:
            continue

    print(df)

    df.to_csv("dataDC.csv",header=True)
        
        
        
        
        
        
        
        
    

def posopinion(sentence):
    tokenizer = treebank.TreebankWordTokenizer()
    pos1 = 0
    tokenized = [word.lower() for word in tokenizer.tokenize(sentence)]
    for word in tokenized:
        if word in opinion_lexicon.positive():
            pos1+=1
    return pos1
        
def negopinion(sentence):
    tokenizer = treebank.TreebankWordTokenizer()
    neg1 = 0
    tokenized = [word.lower() for word in tokenizer.tokenize(sentence)]
    for word in tokenized:
        if word in opinion_lexicon.negative():
            neg1+=1
    return neg1

def neuopinion(sentence):
    tokenizer = treebank.TreebankWordTokenizer()
    tokenized = [word.lower() for word in tokenizer.tokenize(sentence)]
    total =len(tokenized)
    return total



            
