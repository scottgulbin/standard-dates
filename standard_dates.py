import re, os

def monthToNumber(month):
    month = month[0:3].lower()
    if month == ('jan'):
        return '01'
    elif month == ('feb'):
        return '02'
    elif month == ('mar'):
        return '03'
    elif month == ('apr'):
        return '04'
    elif month == ('may'):
        return '05'
    elif month == ('jun'):
        return '06'
    elif month == ('jul'):
        return '07'
    elif month == ('aug'):
        return '08'
    elif month == ('sep'):
        return '09'
    elif month == ('oct'):
        return '10'
    elif month == ('nov'):
        return '11'
    elif month == ('dec'):
        return '12'
    else:
        return '00'

fileOfDates = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname('dates.txt')))
listOfDates = open(fileOfDates+'\dates.txt')
dates = listOfDates.read()

#Extract date YYYY-MM-DD
dateRegex1 = re.compile(r'''(
    (\d{4})
    (-|\.|\/)
    (\d{2})
    (-|\.|\/)
    (\d{2})
)''', re.VERBOSE)
match = []
mo = dateRegex1.findall(dates)
for group in mo:
    oneDate = '/'.join([group[3],group[5],group[1]])
    match.append(oneDate)

#Extract date MM-DD-YYYY
dateRegex2 = re.compile(r'''(
    (\d{1,2})
    (-|\.|\/)
    (\d{1,2})
    (-|\.|\/)
    (\d{4})
)''', re.VERBOSE)
groups = (dateRegex2.findall(dates))
for group in groups:
    item1 = group[1]
    item2 = group[3]
    if len(group[1]) < 2:
        item1 = '0'+item1
    if len(group[3]) < 2:
        item2 = '0' + item2
    oneDate = '/'.join([item1,item2,group[5]])
    match.append(oneDate)


 #Extract format MONTH DD YYYY (December 4, 2019)
dataRegex3 = re.compile('''
    (Jan.*|Feb.*?|Mar.*?|Apr.*?|May|Jun.*?|Jul.*?|Aug.*?|Sep.*?|Oct.*?|Nov.*|Dec.*?)
    (\s)
    (\d{1,2})
    \w{0,3}?
    (\s|,)
    (\s{0,2})?
    (\d{4})
''', re.VERBOSE)
items = dataRegex3.findall(dates)

for item in items:
    month = monthToNumber(item[0])
    day = item[2]
    if len(item[2]) < 2:
        day = '0'+item[2]
    oneDate = '/'.join([month,day,item[5]])
    match.append(oneDate)

output = ''
for line in match:
    output += f'{line}\n'
print(output)

outputFile = open('output.txt', 'w')
outputFile.write(output)
outputFile.close

