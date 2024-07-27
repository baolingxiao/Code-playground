# loop

# while loop

i = 1
while i < 6:
    if i == 3:
        print("True")
        break   #stope at here 
    i += 1

# True



i = 0

while i < 6:
    i += 1
    if i == 3:
        continue # skip step while i = 3
    print(i)

#1 2 4 5 6


i = 1
while i < 6:
  print(i)
  i += 1
else:
    print("i is no longer less than 6")

# 1 2 3 4 5 i is no longer less than 6




# for loop

fruits = ["apple", "banana", "cherry"]
for character in fruits:
    print(character)

# apple banana cherry

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# apple cherry

for x in range(6):
  print(x)

# 0 1 2 3 4 5

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#基于条件的嵌套循环（Nested Loop）
# Nested loop example
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

''''

red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry

'''

### for-else 结构
# for-else structure
for x in range(6):
    print(x)
else:
    print("Loop completed without break")

# Output:
# 0
# 1
# 2
# 3
# 4
# 5
# Loop completed without break


#列表推导式 (List Comprehensions)
#虽然严格来说不算是循环，但列表推导式是处理循环的一种简洁方法。
# List comprehension example
squares = [x**2 for x in range(10)]
print(squares)

# Output:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


#迭代字典（Iterating over dictionaries）
# Iterating over dictionary keys and values
student = {'name': 'John', 'age': 20, 'courses': ['Math', 'CompSci']}

for key in student:
    print(key, student[key])

# Output:
# name John
# age 20
# courses ['Math', 'CompSci']

# Or using items() method
for key, value in student.items():
    print(key, value)

# Output:
# name John
# age 20
# courses ['Math', 'CompSci']


# enumerate 函数
# Using enumerate to get index and value
fruits = ["apple", "banana", "cherry"]

for index, value in enumerate(fruits):
    print(index, value)

# Output:
# 0 apple
# 1 banana
# 2 cherry


# zip 函数 用于并行迭代多个序列。
# Using zip to iterate over multiple lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Output:
# Alice is 25 years old
# Bob is 30 years old
# Charlie is 35 years old


# 使用 iter 和 next 自定义迭代
# Using iter and next for custom iteration
my_list = [1, 2, 3, 4, 5]
my_iter = iter(my_list)

while True:
    try:
        item = next(my_iter)
        print(item)
    except StopIteration:
        break

# Output:
# 1
# 2
# 3
# 4
# 5
