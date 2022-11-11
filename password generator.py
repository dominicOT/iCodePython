import random

lower_case = "abcde23456fghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJK()-+;][{LMNOPQRSTUVWXYZ"
numbers = "1234567jklmnop890"
symbols = "@:!$£ABCDEFGHI%^&*()-+;][{/"

use_for = lower_case + upper_case + numbers + symbols

length_for_pass = 17

password = "".join(random.sample(use_for, length_for_pass))

print(password)
#print(Your generated password is: )
