import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
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
#Extract Proper Nouns in the given user query
def extractNouns(tagged):
    nounList=[]
    for word, tag in tagged:
        if tag in ('NN') or tag in ('NNS') :
            nounList.append(word)
    return nounList

#Extract Integer Values in the given user query
def extractIntegerValues(tagged):
    integerValueList=[]
    for word, tag in tagged:
        if tag in ('CD') :
            integerValueList.append(word)
    return integerValueList

def tockenize(sentence):
    tockenized=nltk.word_tokenize(sentence)
    tagged =nltk.pos_tag(tockenized)
    print(tagged)
    nounList=extractNouns()
    return nounList


#nounList =extractNouns(tagged)
#print("Noun List : ",nounList)
#nounList=extractNouns(tagged)
#print("Noun List : ",nounList)
#integerValueList=extractIntegerValues(tagged)
#print("Integer Value List : ",integerValueList)





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
print('\n')

t17=nltk.word_tokenize("Retrieve a list of employees and the projects each works in, ordered by the employee's department, and within each department ordered alphabetically by employee last name.")
print(nltk.pos_tag(t17))
print('\n')

t18=nltk.word_tokenize("")
print(nltk.pos_tag(t18))

"""

