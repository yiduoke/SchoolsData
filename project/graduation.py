#! /usr/bin/python
print 'content-type: text/html\n'
import cgitb
cgitb.enable()

import CSintro2_project
print '''
<!DOCTYPE html>
<html>
<head>
<style>
table {
    border-collapse: collapse;
    width: 50%;
}

th, td {
    text-align: left;
    padding: 8px;
}

tr:nth-child(even){background-color: #f2f2f2}

th {
    background-color: salmon;
    color: white;
}
</style>'''
CSintro2_project.bar()
grad1 = CSintro2_project.csvToDict('graduation1.csv')
noComma=CSintro2_project.nameComma(grad1)
grad1Norm=CSintro2_project.normal(noComma)
grad1Legit=CSintro2_project.intefy(grad1Norm)
listOfDict = CSintro2_project.intoList(grad1Legit)
orderedLoD = CSintro2_project.rank(listOfDict)
CSintro2_project.table(orderedLoD)