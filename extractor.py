import xml.etree.ElementTree as ET

tree = ET.parse('dataNew2.xml')
root = tree.getroot()

tableInfoDic={}

#Reads the xml file and stores table names, trribute names and attribute values in a dictionary
for table in root.findall('table'):
    tableName=table.get('name')
    valueDic = {}
    for column in table.findall('column'):
        name=column.get('name')
        value=column.get('value')
        valueDic.update({name:value})

    tableInfoDic[tableName]=valueDic

#Reads the keys(table names) from a dictinary and stores in a list
def readTableNames():
    tableList = []
    for key,value in tableInfoDic.items():
        tempKey = key
        tableList.append(tempKey)
    #print("tables :",tableList)
    return tableList



#Reads the keys(attribute names) in dictionary inside another dictionary and converts it into a list
def readAttributeNames():
    attributeList = []
    duplicateAttributeList = []
    for key, value in tableInfoDic.items():
        #tempKey= key
        tempValue = value
        tempDic=tempValue
        for key1 in tempDic.keys():
            attributeList.append(key1)
    #print("attributes", attributeList)
    for x in attributeList:
        if x not in duplicateAttributeList:
            duplicateAttributeList.append(x)
    return duplicateAttributeList

def createTableAttributeDic(tableList):
    attributeList = []
    duplicateAttributeList = []
    n=len(tableList)
    matrix=[]
    for i in range(n):
        rowMatrix=[]
        for j in range(4):
            for table in tableList:
                for key, value in tableInfoDic.items():
                    if table==key:
                        rowMatrix.append(table)
                        tempValue = value
                        tempDic = tempValue
                        pkFkList = []
                        attributeList = []
                        for key1,value1 in tempDic.items():
                            if value1=='primary_key' or value1=='foreign_key':
                                pkFkList.append(key1)
                            else:
                                attributeList.append(key1)
                        rowMatrix.append(attributeList)
                        rowMatrix.append(pkFkList)
                        matrix.append(rowMatrix)

    for x in range(n):
        for y in range(4):
            print(matrix[x][y])
    return matrix

tableList=readTableNames()
mat=createTableAttributeDic(['employee','department'])
#print("matrix :",mat)
#print("table names :", readTableNames())
#print("attribute names :",readAttributeNames())
#print("Table info dic :", tableInfoDic)

