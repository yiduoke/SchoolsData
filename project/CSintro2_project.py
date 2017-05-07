# Code to read a csv file into a dictionary (from hw)
def csvToDict( fileName):
    source = open ( fileName, 'rU')
    contents = source.read()
    source.close()
    listOfStrings = contents.split('\n')
    titles = listOfStrings.pop(0).split(',')
    d = {}
    for oneYearsStats in listOfStrings:
        listOfStats = oneYearsStats.split(',')
	# Floatify portion
	listOfStats2 = []
	for part in listOfStats:
		try:
			listOfStats2.append(float(part))
		except ValueError:
			listOfStats2.append(part)
	# End of floatify portion
	remainingFields = {}
	titleIndex = 1
	while titleIndex < len( titles):
		remainingFields[ titles[titleIndex]] = listOfStats2[titleIndex]
		titleIndex += 1
	d[listOfStats[0]] = remainingFields
    return d

# Binds each new dictionary to a variable
grad1 = csvToDict('graduation1.csv')
progress = csvToDict('progressReport.csv')
sat = csvToDict('sat.csv')
ela = csvToDict('elaGeneral.csv')
math = csvToDict('mathGeneral.csv')
elaEthnicity = csvToDict('elaEthnicity.csv')
elaGender = csvToDict('elaGender.csv')
mathEthnicity = csvToDict('mathEthnicity.csv')
mathGender = csvToDict('mathGender.csv')


# Test to see if it works
# print grad1
# '''...should have this inside:
# '14K478': {'Local Pct of grads': 2007.0, 'Cohort Year': ' BUSINESS & TECHNOLOGY"', 'School Name': '"HIGH SCHOOL OF ENTERPRISE'},'''


def rank(schools):
    return sorted(schools, key=lambda x:x[1],reverse=True)
    
def intoList(dictionary):
    y=[]
    for key in dictionary:
        y.append([key,dictionary[key]['Total Grads Pct of cohort'],dictionary[key]['School Name']])
    return y

def ridSign(string):
    try:
        string=string.replace('%','')
        return string
    except AttributeError:
        string=string

def nameComma(dictionary):
    for key in dictionary:
        if ',' in dictionary[key]['School Name']:
            dictionary[key]['School Name']=dictionary[key]['School Name'].replace(',','')
    return dictionary
        
def isFloat( string):
    try:
        return float( string)
    except ValueError: 
        return string

def floatOrNah(thing):
    try:
        float(thing)
        return True
    except ValueError:
        return False
        
def normal(dictionary):
    for key in dictionary:
        dictionary[key]['Total Grads Pct of cohort']=ridSign(dictionary[key]['Total Grads Pct of cohort'])
        if dictionary[key]['Total Grads Pct of cohort']=='s':
            dictionary[key]['Total Grads Pct of cohort']=100
    return dictionary

def intefy(dictionary):
    for key in dictionary:
        dictionary[key]['Total Grads Pct of cohort']=isFloat(dictionary[key]['Total Grads Pct of cohort'])
    return dictionary

noComma=nameComma(grad1)
grad1Norm=normal(noComma)
grad1Legit=intefy(grad1Norm)
listOfDict = intoList(grad1Legit)
orderedLoD = rank(listOfDict)

def table(listy):
    print '<table border="1" style="width:100%"> <tr> <th> Rank </th> <th> School Name </th> <th> School Code </th> <th> Graduation Rate (%) </th> <tr>'
    x=0
    while x<len(listy):
        print '<tr><td>'+str(x+1)+'</td><td>'+listy[x][2]+'</td><td>'+listy[x][0]+'</td><td>'+str(listy[x][1])+'</td></tr>'
        x+=1
    print '</table>'

def intoListProgress(dictionary):
    y=[]
    for key in dictionary:
        y.append([key,dictionary[key]['ENVIRONMENT RATING'],dictionary[key]['SCHOOL'],dictionary[key]['SCHOOL LEVEL']])
    return y

def progressTable(listy):
    print '<table border="1" style="width:100%"> <tr> <th> Rank </th> <th> School Name </th> <th> School Code </th> <th> School Level </th> <th> School Environment</th> </tr>'
    x=0
    while x<len(listy):
        print '<tr><td>'+str(x+1)+'</td><td>'+listy[x][2]+'</td><td>'+listy[x][0]+'</td><td>'+listy[x][3]+'</td><td>'+str(listy[x][1])+'</td></tr>'
        x+=1
    print '</table>'
progressList=intoListProgress(progress)
orderedProgress=rank(progressList)
#table(orderedLoD)
#progressTable(orderedProgress)

def compare(grad,environment):
    y=''
    for key in grad:
        try:
            y+=str(grad[key]['Total Grads Pct of cohort'])+','+str(environment[key]['ENVIRONMENT RATING'])+'\n'
        except KeyError:
            y+=''
    return y
    
compareData = compare(grad1, progress)

def genderToDict(csv):
    data = open(csv, 'rU')
    thing= data.read()
    data.close()
    numSchool = 0
    dictionary={'Male':[],'Female':[]}
    y=[]
    thing=thing.split('\n')
    thing=thing[1:]
    for something in thing:
        x=[]
        x.append(something[:something.index(',')])
        x.append(something[something.index(',')+1:])
        y+=x
    z=0
    while z<len(y):
        if y[z]=='Female':
            dictionary['Female'].append(isFloat(y[z+1])) 
        else:
            dictionary['Male'].append(isFloat(y[z+1])) 
        z+=2
    return dictionary

def ethnicityToDict(csv):
    data = open(csv, 'rU')
    thing= data.read()
    data.close()
    numSchool = 0
    dictionary={'Asian':[],'Black':[],'White':[],'Hispanic':[]}
    y=[]
    thing=thing.split('\n')
    thing=thing[1:]
    for something in thing:
        x=[]
        x.append(something[:something.index(',')])
        x.append(something[something.index(',')+1:])
        y+=x
    z=0
    while z<len(y):
        if y[z]=='Asian':
            dictionary['Asian'].append(isFloat(y[z+1])) 
        elif y[z]=='Black':
            dictionary['Black'].append(isFloat(y[z+1]))   
        elif y[z]=='White':
            dictionary['White'].append(isFloat(y[z+1]))
        else:
            dictionary['Hispanic'].append(isFloat(y[z+1]))
        z+=2
    return dictionary

elaGenderDict=genderToDict('elaGender.csv')
mathGenderDict=genderToDict('mathGender.csv')
elaEthnicityDict=ethnicityToDict('elaEthnicity.csv')
mathEthnicityDict=ethnicityToDict('mathEthnicity.csv')

def average(dictionary):
    x=0
    y=0
    averages={}
    for key in dictionary:
        for number in dictionary[key]:
            if floatOrNah(number):
                x+=number
                y+=1
        averages[key]=float(x)/y
    return averages

averageElaGender=average(elaGenderDict)
averageMathGender=average(mathGenderDict)
averageElaEthnicity=average(elaEthnicityDict)
averageMathEthnicity=average(mathEthnicityDict)
#####################

def intoList1(dictionary):
    x=[]
    for thing in dictionary:
        x.append([thing,dictionary[thing]['Mean Scale Score']])
    return x

rankedMath=rank(intoList1(math))
rankedEla=rank(intoList1(ela))
    
def table1(listy):
    print '<table border="1" style="width:100%"> <tr> <th> Rank </th> <th> School Code </th> <th> Mean Scale Score </th> <tr>'
    x=0
    while x<len(listy):
        print '<tr><td>'+str(x+1)+'</td><td>'+listy[x][0]+'</td><td>'+str(listy[x][1])+'</td></tr>'
        x+=1
    print '</table>'

#############
def satSubjectList(subject):
    x=[]
    for key in sat:
        x.append([key,sat[key]['SCHOOL NAME'],sat[key][subject]])
    return x

def rank1(schools):
    return sorted(schools, key=lambda x:x[2],reverse=True)
    
rankedSatWriting=rank1(satSubjectList('Writing'))
rankedSatReading=rank1(satSubjectList('Reading'))
rankedSatMath=rank1(satSubjectList('Math'))

def satSubjectTable(listy,subject):
    print '<table border="1" style="width:100%"> <tr> <th> Rank </th> <th> School Code </th> <th> School Name </th> <th>'+subject+'</th> <tr>'
    x=0
    while x<len(listy):
        print '<tr><td>'+str(x+1)+'</td><td>'+listy[x][0]+'</td><td>'+listy[x][1]+'</td>'+'</td><td>'+str(listy[x][2])+'</td></tr>'
        x+=1
    print '</table>'

#print satSubjectTable(rankedSatWriting, 'Writing')
#print satSubjectTable(rankedSatReading, 'Reading')
#print satSubjectTable(rankedSatMath, 'Math')

def sumSat(dictionary):
    x=[]
    for key in dictionary:
        y=0
        if floatOrNah(dictionary[key]['Reading']):
            y+=dictionary[key]['Reading']+dictionary[key]['Writing']+dictionary[key]['Math']
            x.append([key,y,dictionary[key]['SCHOOL NAME']])
    return x
rankedSumSat = rank(sumSat(sat))

def satTotalTable(listy):
    print '<table border="1" style="width:100%"> <tr> <th> Rank </th> <th> School Code </th> <th> School Name </th> <th> SAT Score </th> <tr>'
    x=0
    while x<len(listy):
        print '<tr><td>'+str(x+1)+'</td><td>'+listy[x][0]+'</td><td>'+listy[x][2]+'</td>'+'</td><td>'+str(listy[x][1])+'</td></tr>'
        x+=1
    print '</table>'
    
#satTotalTable(rankedSumSat)

def bar():
    source = open('bar.html', 'rU')
    navBar = source.read()
    source.close()
    print navBar