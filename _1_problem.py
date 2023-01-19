size = int(input("Enter the size of elements you want in your list : "))

list = []
for i in range(size):
    element = str(input("Enter element : "))
    list.append(element)

print(list)

list.sort(key=lambda x:x[-2])
print(list)