
print("Welcome to Love calculator")
boy_name = input("What's the name of the boy/man\n")
girl_name = input("What's the name of the girl/woman\n")

combined_name = boy_name+ girl_name
lower_case = combined_name.lower()

t=lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")
true = t+r+u+e

l=lower_case.count("l")
o=lower_case.count("o")
v=lower_case.count("v")
e=lower_case.count("e")

love = l+o+v+e

total_score = str(true)+str(love)
total_score1 =int(total_score)
total_score
if 10>total_score1 or total_score1>90:
    print(f"Your score is {total_score1}, you go together like coke and mentos.")
elif 40<total_score1<50:
    print(f"Your score is {total_score1}, you are alright together.")
else:
    print(f"Your score is {total_score1}.")
