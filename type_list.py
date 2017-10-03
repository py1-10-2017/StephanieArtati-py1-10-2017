def type_list(x):
    string_concat = ""
    running_sum = 0
    string_exists = False
    number_exists = False
    for i in x:
        if (isinstance(i,int) or isinstance(i,float)):
            number_exists = True
            running_sum += i
        elif (isinstance(i,str)):
            string_exists = True
            string_concat = string_concat + " " + i

    if (string_exists and number_exists):
        print("The list you entered is of mixed type")
        print("String:",string_concat)
        print("Sum:",running_sum)
    elif (string_exists and not number_exists):
        print("The list you entered is of string type")
        print("String:",string_concat)
    else:
        print("The list you entered is of integer type")
        print("Sum:",running_sum)

l1 = ['magical unicorns',19,'hello',98.98,'world']
l2 = [2,3,1,7,4,12]
l3 = ['magical','unicorns']

type_list(l1)
type_list(l2)
type_list(l3)
