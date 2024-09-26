def file(fm:chr):
    f = open("/home/bersbot/u.u", fm)
    if fm == 'w':
        user = ["Имя: " + input("Ввидите ваше имя: ") + ".\n", "Фамилия: " + input("Ввидите вашу Фамилию: ") + ".\n", "Год рождения: " + input("Ввидите ваш год рождения: ") + ".\n", "Номер телефона: " + input("Ввидите ваш номер телефона: ") + ".\n"]
        i = 0
        while i != len(user):
            f.write(user[i])
            i=i+1
        i = 0
    elif fm == 'r':
        print(f.read())
    f.close()
c = input("Ввидите что вы хотите сделать\"r = прочитать, w = изменить/создать\": ")
file(c)
