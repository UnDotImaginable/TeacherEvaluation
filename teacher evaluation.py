# 4 50
firstInput = input()

store = firstInput.split(" ")
students = int(store[0])
desired_avg = float(store[1])


secondInput = input()
scores = (secondInput.split(" "))

scores_integer = [eval(i) for i in scores]

current_avg = sum(scores_integer) / students

i = 0 
additional_score = 100


while(True):
    if (desired_avg == 100):
        print("impossible")
        exit(0)
        

    scores_integer.append(additional_score)
    students += 1
    current_avg = sum(scores_integer) / students
    i += 1

    if (current_avg > desired_avg):
        scores_integer.pop()
        additional_score -= 1
        i -= 1
        students -= 1
    
    if ((current_avg == desired_avg) or additional_score == 0):
        break




print(i)
