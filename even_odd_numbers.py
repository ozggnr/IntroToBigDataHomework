list = [1,2,3,4,5,6,7,8,9]
even_list = []
odd_list = []
for x in list:
    if x % 2 == 0 :
        even_list.append(x)
    else:
        odd_list.append(x)
print(f'even list =  {even_list}')
print(f'odd list =  {odd_list}')
