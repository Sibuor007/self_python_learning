first_name = input("Enter your name: ")
second_name = input("Enter name of partner: ")

combined_string = first_name + second_name
lower_str = combined_string.lower()

t = lower_str.count('t')
r = lower_str.count('r')
u = lower_str.count('u')
e = lower_str.count('e')
true = t + r + u + e

l = lower_str.count('l')
o = lower_str.count('o')
v = lower_str.count('v')
e = lower_str.count('e')
love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"Your love score is {love_score}, and you go together like coke and mentos")
elif 40 <= love_score <= 50:
    print(f"Your love score is {love_score}, and you are alright together")
else:
    print(f"Your love score is {love_score}")
