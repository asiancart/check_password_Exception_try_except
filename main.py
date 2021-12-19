import re


def check_password(psw):
    if len(psw) < 8:
        raise Exception("parola en az 7 karakter olmalidir")
    elif not re.search("[a-z]",psw):
        raise Exception("parola kücük harf icermelidir")
    elif not re.search("[A-Z]",psw):
        raise Exception("parola büyük harf icermelidir")
    elif not re.search("[0-9]",psw):
        raise Exception("parola rakam icermelidir")
    elif re.search("\s",psw):
        raise Exception("parola bosluk karakteri iceremez")

password ="123asdAa"

try:
    check_password(password)
except Exception as e:
    print(e)
