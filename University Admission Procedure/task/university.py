""" This program acts as a University admissions enrollment tool. This first iteration simply takes
the first three exam scores, creates an average, checks to see if you're average is high enough
and responds accordingly """

exam1 = float(input())
exam2 = float(input())
exam3 = float(input())

avg_score = (exam1 + exam2 + exam3) / 3
print(float(avg_score))

if avg_score > 60 or avg_score == 60:
    print("Congratulations, you are accepted!")
else:
    print("We regret to inform you that we will not be able to offer you admission.")