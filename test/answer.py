from models.database import database
from models.games import Zodiac, Pirates, Digital, HarryPotter

user_answer = "mutable,water,earth,fixed"
anum = 1
real_answer = database.query(Zodiac).filter_by(qnum=anum).one().answer

user_answer_list = set(user_answer.split(","))
real_answer_list = set(real_answer.split(","))

if user_answer_list == real_answer_list:
    print("Correct")
else:
    print("Incorrect")

print(user_answer_list)
print(real_answer_list)
