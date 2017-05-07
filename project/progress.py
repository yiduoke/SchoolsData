#! /usr/bin/python
print 'content-type: text/html\n'
import cgitb
cgitb.enable()

import CSintro2_project
print '''
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
progress = CSintro2_project.csvToDict('progressReport.csv')
progressList=CSintro2_project.intoListProgress(progress)
orderedProgress=CSintro2_project.rank(progressList)
CSintro2_project.progressTable(orderedProgress)