tableList = ['department', 'student']
attributeList = ['fname', 'bDate']
symbol = ['>']
value = ['40', '60']
prv_attribute = ['age']
condition_list = ['a', 'b']
operator = ['and']


def conditionConcatenator(conditionAttributeList, operatorSymbolList, conditionValueList, concatenatingOperatorList):
    length = len(conditionValueList)
    count = 0
    condition = ''
    while (count < length):
        attribute = conditionAttributeList[count]
        symbol = operatorSymbolList[count]
        value = conditionValueList[count]
        if (not (len(concatenatingOperatorList) == count)):
            concatenatingOperator = concatenatingOperatorList[count]
            condition = condition + attribute + symbol + value + ' ' + concatenatingOperator + ' '
        else:
            condition = condition + attribute + symbol + value
        count += 1
    return condition


def generateSqlQuery(attributeList, tableList, condition):
    if (attributeList and tableList and condition):
        sqlQuery = "SELECT " + ', '.join(attributeList) + " FROM " + ', '.join(tableList) + " WHERE " + condition + ";"
        print("\n\nFinal SQL Query :", sqlQuery)

    if (attributeList and tableList and not condition):
        sqlQuery = "SELECT " + ','.join(attributeList) + " FROM " + ','.join(tableList) + ";"
        print("\n\nFinal SQL Query :", sqlQuery)

    if (not attributeList and tableList and condition):
        sqlQuery = "SELECT * FROM " + ', '.join(tableList) + " WHERE " + condition + ";"
        print("\n\nFinal SQL Query :", sqlQuery)

    if (not attributeList and not condition):
        sqlQuery = "SELECT * FROM " + ','.join(tableList) + ";"
        print("\n\nFinal SQL Query :", sqlQuery)