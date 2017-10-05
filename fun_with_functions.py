def odd_even():
    for i in range(1,2001):
        if (i%2 == 0):
            print ("Number is: "+str(i)+". This is an even number.")
        else:
            print ("Number is: "+str(i)+". This is an odd number.")

def multiply(arr,multiplier):
    new_arr = []
    for i in arr:
        new_arr.append(i*multiplier)
    return new_arr

def layered_multiples(arr):
    new_arr = []
    print(arr)
    for i in range(len(arr)):
        print(i)
        new_arr.append([])
        curr_num = arr[i]
        for j in range(curr_num):
            new_arr[i].append(1)
    return new_arr

odd_even()

a = [2,4,10,16]
b = multiply(a,5)
print(b)

x = layered_multiples(multiply([2,4,5],3))
print(x)
