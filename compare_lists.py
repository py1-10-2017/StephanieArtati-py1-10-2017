def compare_lists(x,y):
    identical = True
    len1 = len(x)
    len2 = len(y)

    if(len1 == len2):
        for i in range(0,len1):
            if (x[i] != y[i]):
                identical = False
                break
    else:
        identical = False

    if (identical):
        print("The lists are the same")
    else:
        print("The lists are not the same")

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

list_three = [1,2,5,6,5]
list_four = [1,2,5,6,5,3]

list_five = [1,2,5,6,5,16]
list_six = [1,2,5,6,5]

list_seven = ['celery','carrots','bread','milk']
list_eight = ['celery','carrots','bread','cream']

compare_lists(list_one,list_two)
compare_lists(list_three,list_four)
compare_lists(list_five,list_six)
compare_lists(list_seven,list_eight)
