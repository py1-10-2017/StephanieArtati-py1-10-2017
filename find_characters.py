def find_characters(x,y):

    output = []
    for i in range(0,len(x)):
        if (x[i].find(y) != -1):
            output.append(x[i])
    print(output)

word_list = ['hello','world','my','name','is','Anna']
char = 'o'

find_characters(word_list,char)
