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
ela = CSintro2_project.csvToDict('elaGeneral.csv')
rankedEla=CSintro2_project.rank(CSintro2_project.intoList1(ela))
CSintro2_project.table1(rankedEla)