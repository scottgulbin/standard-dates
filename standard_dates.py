import re

#Extract date YYYY-MM-DD
dateRegex1 = re.compile(r'''(
    (\d{4})
    (\s|-|\.|\/)
    (\d{2})
    (\s|-|\.|\/)
    (\d{2})
)''', re.VERBOSE)
match = []
mo = dateRegex1.findall('2019.01.02 2019/01/22 2019-22-33')
for group in mo:
    oneDate = '/'.join([group[3],group[5],group[1]])
    match.append(oneDate)

#Extract date MM-DD-YYYY
dateRegex2 = re.compile(r'''(
    (\d{1,2})
    (\s|-|\.|\/)
    (\d{1,2})
    (\s|-|\.|\/)
    (\d{4})
)''', re.VERBOSE)
groups = (dateRegex2.findall('01/22/2019 02.04.2019 05-99-0321 1.2.2019, 03.2.2019 3.09.2019'))
for group in groups:
    item1 = group[1]
    item2 = group[3]
    if len(group[1]) < 2:
        item1 = '0'+item1
    if len(group[3]) < 2:
        item2 = '0' + item2
    oneDate = '/'.join([item1,item2,group[5]])
    match.append(oneDate)

for item in match:
    print(item)
