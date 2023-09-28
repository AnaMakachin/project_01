# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):
    return s.replace("!", "")
print (remove_exclamation_marks('Hi! Hello!'))
print (remove_exclamation_marks(''))
print (remove_exclamation_marks('Oh, no!!!'))


# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    i = 0
    while i < 1 and s[-1]=="!":
        s = s[:-1]
        i += 1 
    return s

print (remove_last_em('Hi!'))
print (remove_last_em('Hi!!!'))
print (remove_last_em('!Hi'))