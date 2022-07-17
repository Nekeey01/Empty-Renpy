## Шестеренка
init python:

    need_rot = 0
    now_rot = 0

    def my_rotate(d,t,s):
        global need_rot, now_rot
        if need_rot == 270 and now_rot != 270:
            now_rot += 1.5
            d.rotate = now_rot
        elif need_rot == 0 and now_rot != 0:
            now_rot -= 1.5
            d.rotate = now_rot
        return (1/90)   

init python:
    import random

    nonunicode = "◘♦•○▬▬▬▬♂♂♂7♠cX○▐╪Є╗₽℠º°?¤?¦§?©?«¬®?°±??µ¶·?»?ЙйЦцУуКкЕеНнГгШшЩщЗзХхЪъФфЫыВвАаПпРрОоЛлДдЖжЭэЯяЧчСсМмИиТтЬьБбЮюAAAAAA?CEEEEIIII?NOOOOO?OUUUUY??aaaaaa?ceeeeiiii?nooooo?ouuuuy?yAaAaAaCcCcCcCcDdDdEeEeEeEeEeGgGgGgGgHhHhIiIiIiIiIJjKk?LlLlLl??LlNnNnNn???OoOoOo??RrRrRrSsSsSsSsTtTtTtUuUuUuUuUuUuWwYyYZzZzZz"

    def glitchtext(length):
        output = ""
        for x in range(length):
            output += random.choice(nonunicode)
        return output


init:
    python:

#####################################################################
#                        Создание батника                           #
#####################################################################

        def create_console():

            txt_console = '''
color 4
title FUCK_SOCIETY FUCK_SOCIETY FUCK_SOCIETY FUCK_SOCIETY FUCK_SOCIETY FUCK_SOCIETY 
@echo off
echo  
ping -n 1 -w 500 10.10.254.254 >nul

type system.txt
@echo. 
@echo. 
echo  


  
ping -n 1 -w 500 10.10.254.254 >nul

@echo FUCK_SOCIETY FUCK_SOCIETY FUCK_SOCIETY FUCK_SOCIETY FUCK_SOCIETY FUCK_SOCIETY
@echo.
echo  
ping -n 1 -w 500 10.10.254.254 >nul

@echo FUCK_SOCIETY FUCK_SOCIETY FUCK_SOCIETY FUCK_SOCIETY FUCK_SOCIETY FUCK_SOCIETY 
@echo.
echo  
ping -n 1 -w 500 10.10.254.254 >nul

@echo    Private Sub MD5_HASH ()
@echo        Dim MD5 As New MD5CryptoServiceProvider
@echo        Dim BArr() As Byte = Encoding.Default.GetBytes("Text")
@echo        Dim HashArr() As Byte = MD5.ComputeHash(BArr)
@echo        Dim SB As New StringBuilder
@echo.
@echo        For Each B As Byte In HashArr
@echo            SB.Append(B.ToString("x2"))
@echo        Next
@echo.
@echo        MsgBox(SB.ToString)
@echo    End Sub
@echo.
echo  
ping -n 1 -w 800 10.10.254.254 >nul

@echo Dim outpost As Process() = Process.GetProcesses
@echo Dim o As Integer
@echo.
@echo   For o = 0 To outpost.Length - 1
@echo.
@echo   Debug.WriteLine(outpost(o).ProcessName)
@echo.
@echo   If Strings.UCase(outpost(o).ProcessName) =Strings.UCase("outpost")Then
@echo       outpost(o).Kill()
@echo   End If
@echo       Next
@echo.
echo  
ping -n 1 -w 900 10.10.254.254 >nul

dir
echo  
ping -n 1 -w 500 10.10.254.254 >nul

@echo FUCK_SOCIETY FUCK_SOCIETY FUCK_SOCIETY FUCK_SOCIETY FUCK_SOCIETY FUCK_SOCIETY 
@echo. 
echo  
ping -n 1 -w 500 10.10.254.254 >nul

@echo FUCK_SOCIETY FUCK_SOCIETY FUCK_SOCIETY FUCK_SOCIETY FUCK_SOCIETY FUCK_SOCIETY
@echo.
echo  
ping -n 1 -w 500 10.10.254.254 >nul

@echo FUCK_SOCIETY FUCK_SOCIETY FUCK_SOCIETY FUCK_SOCIETY FUCK_SOCIETY FUCK_SOCIETY 
@echo. 
echo  

ping -n 1 -w 500 10.10.254.254 >nul
@echo FUCK_SOCIETY FUCK_SOCIETY FUCK_SOCIETY FUCK_SOCIETY FUCK_SOCIETY FUCK_SOCIETY 
@echo. 
@echo.
echo  
ping -n 1 -w 500 10.10.254.254 >nul



python www.py
'''

            try: renpy.file("ff.bat") ## Проверка на нахождение файла
           
            except: open("ff.bat", "w").write("{}".format(txt_console)) 

#####################################################################
#                            Консолька                              #
#####################################################################

        def console():    

            ## Создаем файл
            txt_die = "YOU_DIE!!!"


            try: renpy.file("system.txt") ## Проверка на нахождение файла
        
            

            except: open("system.txt", "w").write("{} {}\n{} {}\n{} {}\n{} {}\n{} {}".format( txt_die, txt_die, txt_die, txt_die, txt_die, txt_die, txt_die, txt_die, txt_die, txt_die, )) ## Меняем содержимое xxx.txt 

            ######## Создаем питоновский вызов закодированного файла
            txt_www_py = '''


def fayl():    

    ttxx = "0KXQvtGH0LXRiNGMINC40L3RgtC10YDQtdGB0L3Rg9GOINCy0LXRidGMINC/0L7QutCw0LbRgz/QndCw0LbQuNC80LDQtdGI0Ywgc2hpZnQrYSAo0JTQvtC70LbQvdC+INC/0L7QutCw0LfQsNGC0YzRgdGPINC+0LrQvtGI0LrQvikg0Lgg0LLQstC+0LTQuNGI0Ywg0LjQvNGPINCz0LvQsNCy0L3QvtCz0L4g0LPQtdGA0L7RjyDRgdC10YDQuNCw0LvQsCDQvNC40YHRgtC10YAg0YDQvtCx0L7Rgi4K"

    open("I...txt...FUCK_SOCIETY", "w").write("{}".format(ttxx)) 

fayl()

            '''

            try: renpy.file("www.py") ## Проверка на нахождение файла
        
            

            except: open("www.py", "w").write("{}".format(txt_www_py))


            ## Запускаем консоль
            os.system("ff.bat") 

##!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#####################################################################
#                         Проверка файла                            #
#####################################################################

        def proverka_faila():
            # if not persistent.f:

            try: open("I.txt.FUCK_SOCIETY")

            except:
                if not persistent.f:
                    persistent.f = True ## Сюда можно всавить renpy.show вместо if
                    renpy.show('dayR') ## Показ достижения
                pass




#####################################################################
#                  Насильное премещение курсора                     #
#####################################################################

## КУРСОР СРАЗУ НАХОДИТЬСЯ НА ЕДИНСТВЕННОМ ВЫБОРЕ И ЕГО НЕЛЬЗЯ СДВИНУТЬ С ВЫБОРА

        def RigMouse_01():
            currentpos = renpy.get_mouse_pos()
            targetpos = [963, 351]
            if currentpos[1] > targetpos[1] or currentpos[1] < targetpos[1] or currentpos[0] > targetpos[0] or currentpos[0] < targetpos[0]:
                renpy.set_mouse_pos(targetpos[0], targetpos[1], 0.1)

## ПЕРЕВОДИТЬСЯ ТОЛЬКО ЕСЛИ КУРСОР НАВЕДЕН НА ДРУГОЙ ВЫБОР

        def RigMouse_02():
            currentpos = renpy.get_mouse_pos()
            targetpos = [963, 351] ## КООРДИНАТЫ НУЖНОГО ВЫБОРА
            sqw_l_up = [918, 428] ## КООРДИНАТЫ ЛЕВОЙ И ВЕРХНЕЙ ГРАНИЦЫ НЕ НУЖНОГО ВЫБОРА. ЕСЛИ ВЫБОРОВ БОЛЬШЕ, ЧЕМ 2, ВТОРЫЕ КООРДИНАТЫ НАМ НЕ НУЖНЫ 
            sqw_r_down = [1000, 459] ## КООРДИНАТЫ ПРАВОЙ И НИЖНЕЙ ГРАНИЦЫ НЕ НУЖНОГО ВЫБОРА
            if currentpos[0] > sqw_l_up[0] and currentpos[0] < sqw_r_down[0] and currentpos[1] > sqw_l_up[1] and currentpos[1] < sqw_r_down[1]: ## Проверка на нахождение курсора
                renpy.set_mouse_pos(targetpos[0], targetpos[1], 0.1) ## перетаскиваем курсор на нужный выбор


#####################################################################
#                  Нахождение курсора на одной точке                #
#####################################################################
screen rigged_choice_1(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

    timer 1.0/30.0 repeat True action Function(RigMouse_01)



#####################################################################
#                  Насильное премещение курсора                     #
#####################################################################
screen rigged_choice_2(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

    timer 1.0/30.0 repeat True action Function(RigMouse_02)






