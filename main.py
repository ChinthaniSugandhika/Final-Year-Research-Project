import extractor
import knowledgebase
import preProcessor
import queryGenerator

#create Knowledge Base
tableSynset=knowledgebase.createKnowledgeBase('table', extractor.readTableNames())
attributeSynset=knowledgebase.createKnowledgeBase('attribute', extractor.readAttributeNames())
#print("TableSynset: ",tableSynset)
#print("AttributeSynset", attributeSynset)

tables=[]

def getTableNames(nouns, tables):
    tableList=[]
    for noun in nouns:
        for table in tables:
            if(noun==table):
                tableList.append(table)
                nouns.remove(noun)
    return tableList

def getAttributeNames(nouns,attributes,tables, taggedList):
    attributeList=[]
    keyWords=['of','from']
    #attributeList=[]
    wordList=[]
    for word,tag in taggedList:
        wordList.append(word)
    for word in wordList:
        if(word in tables):
            index=wordList.index(word)
            if(wordList[index-1] in keyWords):
                    for i in range(0,index-1): #change index-1 to index -2
                        for attribute in attributes:
                            if(nouns[i]==attribute):
                                attributeList.append(nouns[i])
    #for noun in nouns:
       # for attribute in attributes:
            #if(noun==attribute):
                #if (noun in attributeList):
                    #continue
                #attributeList.append(attribute)
    return attributeList

#userInput=("give me first_name and salary from female employee whose salary greater than 50000 and department_number equals 6")
userInput=("list all employee whose whose salary greater than 50000 ")

taggedWordList=preProcessor.tockenize(userInput)

filterdSentence=preProcessor.removeStopWords(taggedWordList)
print("filtered :",filterdSentence)

nounList=preProcessor.extractNouns(taggedWordList)
print(nounList)

attributeValues=preProcessor.extractIntegerValues(taggedWordList)
print(attributeValues)

adjectivesNouns=preProcessor.extractAdjectivesAndNouns(filterdSentence)
print("adjectives ",adjectivesNouns)

adverbs=preProcessor.extractAdverbs(taggedWordList)
print("adverbs ",adverbs)

adjectives=preProcessor.extractAdjectives(taggedWordList)
print("adjectives ",adjectives)

symbol=knowledgebase.operatorKnowledgeBase(adjectivesNouns,adverbs)
print("Symbols :",symbol)

tables=extractor.readTableNames()

attributes=extractor.readAttributeNames()

tableNames=getTableNames(nounList,tables)

adjectveAttributes=preProcessor.getAdjectveAttribute(tableNames,adjectives,taggedWordList)
print("adjectveAttributes  : ",adjectveAttributes)

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