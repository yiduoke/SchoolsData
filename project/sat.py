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
sat = CSintro2_project.csvToDict('sat.csv')
rankedSumSat = CSintro2_project.rank(CSintro2_project.sumSat(sat))
CSintro2_project.satTotalTable(rankedSumSat)
