import nltk

from nltk.corpus import wordnet
nltk.download('wordnet')
from nltk.corpus import wordnet as wn
import re
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.stem import WordNetLemmatizer

from operator import itemgetter
#from nltk.corpus import state_union
#from nltk.tokenize import PunktSentenceTokenizer

"""
#Extract Nouns in the given user query
def extractNouns(tagged):
    nounList=[]
    for word, tag in tagged:
        if (tag in ('NN') or tag in ('NNS')) :
            nounList.append(word)
    return nounList
"""
#Remove stop words
def removeStopWords(tagged):
    stopWords = set(stopwords.words('english'))
    filterdSentence=[]
    essenialWords=['or','and']
    for word,tag in tagged:
        if(not(word in stopWords) or word in essenialWords):
            filterdSentence.append(word)
    print("filtered", filterdSentence)
    posTaggedFilterdSentence=nltk.pos_tag(filterdSentence)
    print("postaggedFilterd :",posTaggedFilterdSentence)
    return posTaggedFilterdSentence


#Extract Nouns in the given user query
def extractNouns(tagged):
    nounList=[]
    for word, tag in tagged:
        if tag in ('NN') or tag in ('NNS') :
            nounList.append(word)
    return nounList

#Extract Integer Values in the given user query
def extractIntegerValues(tagged):
    taggedList=tagged
    integerValueList=[]
    for word, tag in taggedList:
        if (tag in ('CD') or tag=='NNP' or tag=='NNPS') :
            integerValueList.append(word)
    return integerValueList

#Extract adjectives and nouns in the given user query
def extractAdjectivesAndNouns(tagged):
    adjectiveNounList=[]
    for word, tag in tagged:
        if tag in ('NN') or tag in ('NNS') or tag in('JJ') or tag in ("JJR") or tag in ("JJS") or tag in ('VB') or tag in ('VBD') or tag in('VBG') or tag in ("VBN") or tag in ("VBZ") or tag in ("VBP") or tag in ("MD"):
            adjectiveNounList.append(word)
    return adjectiveNounList

#Extract adverbs in the given user query
def extractAdverbs(tagged):
    adverbList=[]
    for word, tag in tagged:
        if tag in ('RB') or tag in ('RBR') or tag in('RBS'):
            adverbList.append(word)
    return adverbList

#Extract adjectives in the given user query
def extractAdjectives(tagged):
    adjectivesList=[]
    for word, tag in tagged:
        if tag in ('JJ') or tag in ('JJR') or tag in('JJS'):
            adjectivesList.append(word)
    return adjectivesList

def extractConditionAttribute(nouns,attributesList):
    greaterThanList = ['greater', 'bigger', 'higher', 'great', 'more','lesser', 'smaller', 'lower', 'less']
    lesserThanList = ['lesser', 'smaller', 'lower', 'less']
    equalList = ['equal', 'equals', 'same']
    extractedWordsList=[]
    conditionAttributeList=[]
    for word in nouns:
        id=0
        if(word in greaterThanList or word in lesserThanList or word in equalList):
            id=nouns.index(word)
            attributeName=nouns[id-1]
            extractedWordsList.append(attributeName)
            nouns.remove(nouns[id])
    for word in extractedWordsList:
        if (word in attributesList):
            conditionAttributeList.append(word)
        else:
            for att in attributesList:
                lemmas = set(wordnet.all_lemma_names())
                if (att in lemmas and word in lemmas):
                    #print("true")
                    s1 = wn.synsets(att)[0]
                    s2 = wn.synsets(word)[0]
                    sim = s1.wup_similarity(s2)
                    if sim >= 0.8:
                        conditionAttributeList.append(att)
    return conditionAttributeList

def extractConditionConcatenatingOperator(nouns, cardinalDigits,taggedWords):
    andList=['and']
    orList=['or']
    cdIndexList=[]
    operatorList=[]
    print("nouns :", taggedWords)
    words=[]
    operator=[]
    if(len(cardinalDigits)>1):
        for word, tag in taggedWords:
            if tag in ('CD') or tag in ('NNP') or tag in ('NNPS'):
                cdIndexList.append(word)
            words.append(word)
        lengthOfCDIndexList=len(cdIndexList)
        lengthOfWordsList=len(words)
        count=0
        while(count<lengthOfCDIndexList):
            chunkStartIndex=count
            chunkEndIndex=chunkStartIndex+1
            count += 1
            chunkStart=words.index(cdIndexList[chunkStartIndex])
            if(chunkStart!=lengthOfWordsList-1):
                chunkEnd = words.index(cdIndexList[chunkEndIndex])
                for i in range(chunkStart, chunkEnd):
                    if (words[i] in andList or words[i] in orList):
                        operator = words[i]
                        operatorList.append(operator)
            else:
                continue
    return operatorList




def tockenize(sentence):
    tockenized=nltk.word_tokenize(sentence)
    print("tockens",tockenized)
    tagged =nltk.pos_tag(tockenized)
    print("tagged ",tagged)
    return tagged

def lemmatizing(tagged):
    lemmatizer = WordNetLemmatizer()
    lemmatizedWordList=[]
    for word in tagged:
        lemmatizedWord=lemmatizer.lemmatize(word)
        lemmatizedWordList.append(lemmatizedWord)
    return lemmatizedWordList