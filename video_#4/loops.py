### while loops
# count = 0
# while count<=5:
#     print(count)
#     count +=1

### for loops
# fruits = ["Apples", "Banana", "Cherry"]
# for fruit in fruits:
#     print(fruit)

### break 
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in numbers:
#     if number == 8:
#         break
#     print(number) # output: 1, 2, 3, 4, 5, 6, 7

# for number in range(20):
#     if number == 8:
#         break
#     print(number) # output: 0, 1, 2, 3, 4, 5, 6, 7

### continue
for number in range(10):
    if number % 2 == 0:
        continue
    print(number) # output: 1, 3, 5, 7, 9