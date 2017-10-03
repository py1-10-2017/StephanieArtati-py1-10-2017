# Multiples Part 1
print("Multiples - Odd Numbers")
odd_numbers = []
for i in range(0,1001):
    if (i%2!=0):
        odd_numbers.append(i)
print(odd_numbers)

# Multiples Part 2
print("Multiples - Multiples of 5")
multiples_numbers = []
for i in range(5,1000001):
    if (i%5==0):
        multiples_numbers.append(i)
print(multiples_numbers)

# Sum
print("Sum")
a = [1, 2, 5, 10, 255, 3]
total = 0
for i in a:
    total += i
print(total)

# Average
print("Average")
print(total/len(a))
