#21/01/2023
#Author: dominicOT

str_with_symbols = "I! love C#, &Python, and Java.?"
str_without_symbols = str_with_symbols.replace("!", "").replace("&", "").replace("?", "")

print("Initial String:", str_with_symbols)

print("Modified String :", str_without_symbols)
