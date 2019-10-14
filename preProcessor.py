from typing import List, Any

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
nltk.download('stopwords')
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
        if (tag in ('CD') or tag=='NNP') :
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

def getAdjectveAttribute(tableNames,adjectives,tagged):
    words=[]
    attribute=[]
    list=[]
    list=tableNames
    #attribute={}
    for word, tag in tagged:
        #if tag in ('CD') or tag in ('NNP') or tag in ('NNPS'):
        words.append(word)
    lengthOfAdjectivesIndexList = len(tableNames)
    lengthOfWordsList = len(words)
    lengthOfAdjectives =len(adjectives)
    count = 0
    tableNameIndex=0
    if len(tableNames)==1:
        for i in range(lengthOfWordsList):
            x=words[i]
            y='employee'
            #if words[i]==words[0]:
            if x==y:
                tableNameIndex=i
        for j in range(lengthOfAdjectives):
            if words[tableNameIndex-1]==adjectives[j]:
                attribute=adjectives[j]
    else:
        while (count < lengthOfAdjectivesIndexList):
            chunkStartIndex = count
            chunkEndIndex = chunkStartIndex + 1
            count += 1
            chunkStart = words.index(tableNames[chunkStartIndex])
            if (chunkStart != lengthOfWordsList - 1):
                chunkEnd = words.index(tableNames[chunkEndIndex])
            #for i in range(chunkStart, chunkEnd):
                for j in adjectives:
                    if adjectives[j]==words[chunkEnd-1]:
                        attribute.append(adjectives[j])
                    #attribute.update(tableNames[],adjectives[j])
    return attribute


def tockenize(sentence):
    tockenized=nltk.word_tokenize(sentence)
    print("tockens",tockenized)
    tagged =nltk.pos_tag(tockenized)
    print("tagged ",tagged)
    return tagged

#def generateConditionList():






"""
tockenized=nltk.word_tokenize("For every project located in 'Stafford', list the project number, the controlling department number, and the department managerslastname, address, and birthdate")
print('\n')

t1=nltk.word_tokenize("Retrieve the birthdate and address of the employee whose name is 'John B. Smith'.")
print(nltk.pos_tag(t1))
print('\n')

t2=nltk.word_tokenize("Retrieve the name and address of all employees who work for the 'Research' department.")
print(nltk.pos_tag(t2))
print('\n')

t3=nltk.word_tokenize("For each employee, retrieve the employee's name, and the name of his or her immediate supervisor.")
print(nltk.pos_tag(t3))
print('\n')

t4=nltk.word_tokenize("Retrieve the SSN values for all employees.")
print(nltk.pos_tag(t4))
print('\n')

t5=nltk.word_tokenize("Retrieve the name of each employee who has a dependent with the same first name as the employee.")
print(nltk.pos_tag(t5))
print('\n')

t6=nltk.word_tokenize("Retrieve the social security numbers of all employees who work on project number 1, 2, or 3.")
print(nltk.pos_tag(t6))
print('\n')

t7=nltk.word_tokenize("Retrieve the names of all employees who do not have supervisors.")
print(nltk.pos_tag(t7))
print('\n')

t8=nltk.word_tokenize("Find the maximum salary, the minimum salary, and the average salary among all employees.")
print(nltk.pos_tag(t8))
print('\n')

t9=nltk.word_tokenize("Find the maximum salary, the minimum salary, and the average salary among employees who work for the 'Research' department.")
print(nltk.pos_tag(t9))
print('\n')

t10=nltk.word_tokenize("Retrieve the total number of employees in the company")
print(nltk.pos_tag(t10))
print('\n')

t11=nltk.word_tokenize("Retrieve the number of employees in the 'Research' department ")
print(nltk.pos_tag(t11))
print('\n')

t12=nltk.word_tokenize("Retrieve all employees whose address is in Houston, Texas. Here, the value of the ADDRESS attribute must contain the substring 'Houston,TX'")
print(nltk.pos_tag(t12))
print('\n')

t13=nltk.word_tokenize("Show the effect of giving all employees who work on the 'ProductX' project a 10% raise.")
print(nltk.pos_tag(t13))
print('\n')

t14=nltk.word_tokenize("For each department, retrieve the department number, the number of employees in the department, and their average salary.")
print(nltk.pos_tag(t14))
print('\n')

t15=nltk.word_tokenize("For each project, retrieve the project number, project name, and the number of employees who work on that project")
print(nltk.pos_tag(t15))
print('\n')

t16=nltk.word_tokenize("For each project on which more than two employees work , retrieve the project number, project name, and the number of employees who work on that project.")
print(nltk.pos_tag(t16))
pint('\n')

t17=nltk.word_tokenizef"Retrieve a list of employees and the projects each works in, ordered by the employee's department, and within each department ordered alphabetically by employee last name.")
print(nltk.pos_tag(t17h)
print('\n')

t18=nltk.word_tokenize("")
print(nltk.pos_tag(t18))

"""

