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
