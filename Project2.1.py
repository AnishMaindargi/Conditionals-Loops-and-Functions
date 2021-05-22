list1=[12, -7, 5, 64, -14]
Output1=[]

list2=[12, 14, -95, 3]
Output2=[]

for num1 in list1:
    if num1>=0:
        Output1.append(num1)

for num2 in list2:
    if num2>=0:
        Output2.append(num2)

print(*Output1)
print(Output2)