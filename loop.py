# FOR LOOP: If we want to execute some action for every element present in some sequence (it may be string or collection) use for loop
# To print Hello 10 times
for x in range(10):
    print("Hello")

# To display number from 0 to 10
for x in range(11):
    print(x)

for x in range(5, 11):
    print(x)

for x in range(5, 11, 2):
    print(x)

# To display odd number from 0 to 20
for x in range(21):
    if (x % 2 != 0):
        print(x)

# To print sum of numbers present in side list
list = eval(input('Enter List of numbers: '))
sum = 0
for x in list:
    sum = sum + x
    print('The Sum=', sum)

# WHILE LOOP: To execute a group of statement iteratively until some conditions false syntax
# To print numbers from 1 to 10 by using while loop
x = 1
while x <= 10:
    print(x)
    x += 1

# NESTED LOOPS
for i in range(4):
    for j in range(4):
        print('i=', i,  'j=', j)

# TRANSFER STATEMENT: BREAK & CONTINUE
# BREAK:Used to break loop in execution based on some condition
for i in range(10):
    if i == 7:
        break
print('processing is enough..plz break')

# CONTINUE:We can use continue statement to skip current iteration and continue next iteration
# To print odd numbers in the range 0 to 9
for i in range(10):
    if i % 2 == 0:
        continue

    print(i)
