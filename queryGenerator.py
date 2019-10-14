tableList=['department', 'student']
attributeList=['fname', 'bDate']
symbol =['>']
value = ['40', '60']
prv_attribute=['age']
condition_list=['a','b']
operator =['and']

def conditionConcatenator(conditionAttributeList,operatorSymbolList,conditionValueList,concatenatingOperatorList):
    length=len(conditionValueList)
    count=0
    condition=''
    while(count<length):
        attribute=conditionAttributeList[count]
        symbol=operatorSymbolList[count]
        value=conditionValueList[count]
        if(not(len(concatenatingOperatorList)==count)):
            concatenatingOperator = concatenatingOperatorList[count]
            condition=condition+attribute+symbol+value+' '+concatenatingOperator+' '
        else:
            condition = condition + attribute + symbol + value
        count+=1
    return condition

def generateSqlQuery(attributeList,tableList, condition):
    if (attributeList and tableList and condition):
        #att_for_value = prv_attribute
        #sqlQuery = "SELECT " + ', '.join(attributeList) + " FROM " + ', '.join(tableList)+ " WHERE " + att_for_value[0] + symbol + value[0] + ";"
        sqlQuery = "SELECT " + ', '.join(attributeList) + " FROM " + ', '.join(tableList) + " WHERE " + condition + ";"
        print("\n\nFinal SQL Query :",sqlQuery)

    if (not value and attributeList and tableList):
        sqlQuery = "SELECT " + ','.join(attributeList) + " FROM " + ','.join(tableList) + ";"
        print("\n\nFinal SQL Query :",sqlQuery)

    if (not attributeList):
        sqlQuery = "SELECT * FROM " + ','.join(tableList) + ";"
        print("\n\nFinal SQL Query :",sqlQuery)
    #print("basic sql",sqlQuery)
    #return sqlQuery

    """
    
        if value and attributeList:
       # att_for_value = prv_attribute
       #att_for_value=condition_list
       basciSQL = "SELECT " + ', '.join(attributeList) + " FROM " + ', '.join(tableList) + " WHERE " + condition_list[0][0] + symbol[0][0] + value[0][0] + operator[0][0]+ " "+ condition_list[1] + symbol[1] + value[1] + ";"
    print("basic sql", basciSQL)
    return basciSQL
    
    if value and attributeList:
        att_for_value = prv_attribute
        basciSQL = "SELECT " + ', '.join(attributeList) + " FROM " + ', '.join(tableList)+ " WHERE " + att_for_value[0] + symbol[0] + value[0] + operator[0] +att_for_value[1] + symbol[1] + value[1]+ ";"
    print("basic sql",basciSQL)
    return sqlQuery;

    if value and len(condition_list) >= 2:
        basciSQL = "SELECT " + ', '.join(attributeList) + " FROM " + ', '.join(tableList)+ " WHERE " + condition_list[0][0] + condition_list[0][1] + value[0] + operator[0].upper() + " " +condition_list[1][0] + condition_list[1][1] + value[1] + ";"
        print(basciSQL)


    for a in condition_list and b in symbol and c in value:
        st="statement" + condition_list[a] + " " + symbol[b] + " " + value[c] + " "
        print(st)
"""
#generateSqlQuery(attributeList,tableList, condition_list, symbol, value,operator)