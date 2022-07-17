
## Файл   


init:
    $ kod_my = False  
    $ kod_setchik = 0

############################## Сделать вывод в экарн confirm с Да и Нет, но заменить этот экран


label kod:


    $ kod_my = renpy.input (u"Введите код")

    if kod_my.lower() == "пустые":
        "Молодец"
        return
        ##Показ достижения

    if kod_my.lower() == "эллиот" or kod_my.lower() == "эллиот алдерсон":
        
        avtor "Молодец"

        # if persistent.maz:
        #     ## Прыжок на лейбл. Показ поняшек
            
        
        # else:
        #     avtor "Не молодец"
        #     ## Прыжок на лейбл. Показ страшной картинки
        return
            
    if kod_my == "":
        avtor "Ты серьезно? Введи хоть что-нибудь."

    if kod_my.lower() != "эллиот" and kod_my.lower() != "эллиот Алдерсон" and kod_my.lower() != "пустые":
        avtor "Код не правильный. Проверьте правильность фразы."

    $ kod_setchik += 1
    
    if kod_setchik == 3:
        avtor "Вы превысили число попыток за эту сессию. Вернитесь сюда позже."
        return


    

