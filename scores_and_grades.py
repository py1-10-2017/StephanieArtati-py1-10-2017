import random

def scores_and_grades():
    print("Scores and Grades")
    for i in range(10):
        random_num = int(random.random() * 40) + 60
        if (random_num>=90):
            print("Score: "+str(random_num)+"; Your grade is "+"A")
        elif (random_num>=80):
            print("Score: "+str(random_num)+"; Your grade is "+"B")
        elif (random_num>=70):
            print("Score: "+str(random_num)+"; Your grade is "+"C")
        else:
            print("Score: "+str(random_num)+"; Your grade is "+"D")
    print("End of the program. Bye!")

scores_and_grades()
