print("Find and Replace")
words = "It's thanksgiving day. It's my birthday,too!"
day_pos = words.find("day")
print("Position of day: ",day_pos)
new_words = words.replace("day","month")
print(new_words)

print("Min and Max")
x=[2,54,-2,7,12,98]
print(min(x))
print(max(x))

print("First and Last")
x = ["hello",2,54,-2,7,12,98,"world"]
print(x[0])
print(x[len(x)-1])

print("New List")
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
length = len(x)
first_list = []
second_list = []
for i in range(0,len(x)):
    if (i<length/2-1):
        first_list.append(x[i])
    else:
        second_list.append(x[i])
second_list.insert(0,first_list)
print(second_list)
