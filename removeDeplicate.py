numbers = [1,5,5,2,7,3,10,5]
removedNum = []
for num in numbers:
    if num not in removedNum:
        removedNum.append(num)
print(removedNum)
