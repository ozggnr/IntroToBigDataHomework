import os.path

if os.path.isfile('/Users/ozgecaylioglu/python_notebook/housing.data'):
    print('I have a file to process')
else:
    print('Boo, no file for me')
file = open('/Users/ozgecaylioglu/python_notebook/housing.data','r')
data = file.read()
print(data + '\n')
new_data = data.split('\n')
#print(new_data)
for line in new_data:
    new_line = []
    for element in line.split(' '):
        if len(element) == 0:
            continue
        new_line.append(element)
    print(new_line)
