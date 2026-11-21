import string 

allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + "*-#"

print("Ввод: ")
Password = input()

if len(Password) != 8:
    print("Длина пороля не равна 8 ")

if Password == Password.lower():
    print("в пароле отсутствуют заглавные буквы")

if Password == Password.upper():
    print("В пароле остутствует строчные буквы")

if (not any(num in string.digits for num in Password )) :
    print("В пароле отсутсвуют цифры ")

if (not (symbol in allowed for symbol in Password)):
    print("В пароле ипсользуются не предусмотренные символы ")

if (not any(symbol in "#-*" for symbol in Password)):
    print("В пароле не используются предусмотренные символы ")

else :
    print("Надежный пароль ")

