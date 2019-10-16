import nltk

from nltk.corpus import wordnet
nltk.download('wordnet')
from nltk.corpus import wordnet as wn
import re
import extractor
import knowledgebase
import preProcessor
import queryGenerator

#create Knowledge Base
tableSynset=knowledgebase.createKnowledgeBase('table', extractor.readTableNames())
attributeSynset=knowledgebase.createKnowledgeBase('attribute', extractor.readAttributeNames())

def getTableNames(nouns, tables):
    tableList=[]
    duplicateTableList=[]
    for noun in nouns:
        for table in tables:
            if(noun==table):
                tableList.append(table)
                nouns.remove(noun)
            else:
                s1Lemmas = set(wordnet.all_lemma_names())
                if (table in s1Lemmas and noun in s1Lemmas):
                    #print("true")
                    s1 = wn.synsets(table)[0]
                    s2 = wn.synsets(noun)[0]
                    sim = s1.wup_similarity(s2)
                    if sim >= 0.8:
                        tableList.append(table)
                        nouns.remove(noun)

    for x in tableList:
        if x not in duplicateTableList:
            duplicateTableList.append(x)
    return duplicateTableList

def getAttributeNames(nouns,attributes,tables, taggedList):
    duplicateAttributeList=[]
    attributeList=[]
    keyWords=['of','from']
    pdt=''
    wordList=[]
    for word,tag in taggedList:
        if(tag=='PDT' and word=='all'):
            return
        wordList.append(word)
    for word in wordList:
        if(word in tables):
            index=wordList.index(word)
            if(wordList[index-1] in keyWords):
                    for i in range(0,index-1):
                        n=nouns[i]
                        for attribute in attributes:
                            if(nouns[i]==attribute):
                                attributeList.append(nouns[i])

    for x in attributeList:
        if x not in duplicateAttributeList:
            duplicateAttributeList.append(x)
    return duplicateAttributeList


userInput=("show me first_name, salary of employee")
#can you give me employee names who earn salary more than 400000

taggedWordList=preProcessor.tockenize(userInput)

filterdSentence=preProcessor.removeStopWords(taggedWordList)
print("filtered :",filterdSentence)

nounList=preProcessor.extractNouns(taggedWordList) #filterdSentence
print(nounList)

attributeValues=preProcessor.extractIntegerValues(taggedWordList)
print(attributeValues)

adjectivesNouns=preProcessor.extractAdjectivesAndNouns(taggedWordList) #filterdSentence
print("adjectives ",adjectivesNouns)

adverbs=preProcessor.extractAdverbs(taggedWordList)
print("adverbs ",adverbs)

adjectives=preProcessor.extractAdjectives(taggedWordList)
print("adjectives ",adjectives)

lemmatizedWords=preProcessor.lemmatizing(nounList)
print("lemmatized Words :",lemmatizedWords)

symbol=knowledgebase.operatorKnowledgeBase(adjectivesNouns,adverbs)
print("Symbols :",symbol)

tables=extractor.readTableNames()

attributes=extractor.readAttributeNames()

tableNames=getTableNames(lemmatizedWords,tables)
print("table names :",tableNames)

attributeNames=getAttributeNames(adjectivesNouns,attributes,tableNames,taggedWordList)
print("attribute Names :",attributeNames)

conditionAttributeName=preProcessor.extractConditionAttribute(adjectivesNouns,attributes)
print("condition Att :",conditionAttributeName)

concatenatingOperator=preProcessor.extractConditionConcatenatingOperator(nounList,attributeValues,taggedWordList)
print("concat",concatenatingOperator)
#process natural language query

condition=queryGenerator.conditionConcatenator(conditionAttributeName,symbol,attributeValues,concatenatingOperator)
print("concat condition :",condition)

#queryGenerator.generateSqlQuery(attributeNames,tableNames,conditionAttributeName,symbol, attributeValues)
queryGenerator.generateSqlQuery(attributeNames,tableNames,condition)