string_upper = input("enter a string in uppercase to hide: ")
upp_ = string_upper.upper()
ord_ = []
for char_ in upp_:
    print(ord(char_), end="")
    ord_.append(char_)


