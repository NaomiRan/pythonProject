# find the largest number in a list
numbers=[2,8,1,0,12]
largest=numbers[0]
for num in numbers:
    if num>largest:
        largest=num
print(f"the largest number is {largest}")

