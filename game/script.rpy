
   ################ ВЫБОР ЗАСТАВКИ 
init python:
    ### ПЕРЕМЕННЫЕ

    if persistent.vibor_36 == None:
        persistent.vibor_36 = False 


    if persistent.prolog == None:
        persistent.prolog = True

    if persistent.logo == None:
        persistent.logo = False

    if persistent.false_schet_chek == None:
        persistent.false_schet_chek = False


    if persistent.false_schet == None:
        persistent.false_schet = 0


    if persistent.f == None:
        persistent.f = False
    

    if persistent.stone == None:
        persistent.stone = 0


    if persistent.maz == None:
        persistent.maz = False

    ## Splashscreen
    if persistent.splash == None:
        persistent.splash = False
        splash = False
    else:
        splash = persistent.splash
    
    ## Логотип
    if persistent.logo == None:
        persistent.logo = False
        logo = False
    else:
        logo = persistent.logo

    if persistent.notify == None:
        persistent.notify = False
    
    #if prolog == None:
    prolog = True

    ## Выборы
    vibor_1 = False
    vibor_1_1 = False

    vibor_2 = False
    vibor_2_1 = False
    vibor_2_01 = False

    vibor_3 = False

    vibor_4 = False
    vibor_4_01 = False
    vibor_4_02 = False
    vibor_4_03 = False

    vibor_5 = False
    vibor_5_01 = False
    vibor_5_02 = False
    vibor_5_02_em = False
    vibor_5_02_nothing = False
    vibor_5_02_nothing_st = False

    vibor_6 = False

    vibor_7 = False
    vibor_7_1 = False

    vibor_8 = False
    vibor_8_0 = False
    vibor_8_01 = False
    vibor_8_1_1 = False
    vibor_8_1 = False
    vibor_8_2 = False

    vibor_9 = False

    vibor_10 = False
    vibor_10_1 = False
    vibor_10_2 = False
    vibor_10_3 = False
    vibor_10_4 = False

    vibor_11 = False
    vibor_11_1 = False
    vibor_11_2 = False

    vibor_12 = False
    vibor_12_1 = False

    vibor_13 = False
    vibor_13_1 = False

    vibor_14 = False
    vibor_14_1 = False
    vibor_14_2 = False

    vibor_15 = False
    vibor_15_1 = False
    vibor_15_2 = False
    vibor_15_3 = False

    vibor_16 = False
    vibor_16_1 = False

    vibor_17 = False
    vibor_17_1 = False
    vibor_17_2 = False
    vibor_17_3 = False

    vibor_18 = False
    vibor_18_1 = False

    vibor_19 = False
    vibor_19_1 = False
    vibor_19_2 = False
    vibor_19_2_1 = False
    vibor_19_3 = False
    vibor_19_4 = False
    vibor_19_5 = False
    vibor_19_6 = False
    vibor_19_7 = False
    vibor_19_8 = False
    vibor_19_9 = False
    vibor_19_chet = 0

    vibor_20 = False
    vibor_20_1 = False

    vibor_21 = False
    vibor_21_1 = False
    vibor_21_2 = False
    vibor_21_3 = False

    vibor_22 = False
    
    vibor_23 = False
    vibor_23_1 = False
    vibor_23_2 = False

    vibor_24 = False
    vibor_24_1 = False
    vibor_24_schet = 0
    vibor_24_schet_1 = False

    vibor_25 = False

    vibor_26 = False

    vibor_27 = False
    vibor_27_1 = False

    vibor_28 = False
    vibor_28_1 = False
    vibor_28_2 = False
    vibor_28_3 = False
    vibor_28_4 = False

    vibor_29 = False

    vibor_30 = False
    vibor_30_1 = False

    vibor_31 = False
    vibor_31_1 = False

    vibor_32 = False
    vibor_32_1 = False
    vibor_32_2 = False
    vibor_32_3 = False

    vibor_33 = False
    vibor_33_1 = False

    vibor_34 = False
    vibor_34_0 = False
    vibor_34_1 = False

    vibor_35 = False

    vibor_36 = False



    dont_go_with_miu =False

    die = False

    day2_nothing = False
    day2_nothing_2 = False

    choice_01_01 = False
    choice_01 = False
    choice_02 = False

    avtor_huyasno = False





    poln_ekr = False


    ##Персонажи
    th = Character(u'', what_color="#3c8dfe", what_prefix='"', what_suffix='"')
    # qu = Character(u'', what_color="#008000")
    vopros = Character(u"???", who_color="#808080")
    iok = Character(u"Иошикезу Курода", who_color="#808080")
    ac = Character(u"Акацуки Сею", who_color="#808080")
    sk = Character(u"Шизуко Кеншин", who_color="#808080")
    sch = Character(u"Сузумо Чо", who_color="#808080")
    ts = Character(u"Танака-Сан", who_color="#808080")
    ink = Character(u"Инабэ Котомуцу", who_color="#808080")
    you = Character(u"Юки Мацуро", who_color="#808080")
    md = Character(u"Миюки Данго", who_color="#808080")
    sao = Character(u"Сао Тян", who_color="#808080")
    si = Character(u"Сайка Ишиикензо", who_color="#808080")
    kub = Character(u"Куб", who_color="#808080")

    avtor = Character(u"Создатель всего и вся", who_color="#010101", what_color="#F90000")
    

    ## МУЗЫКА
    PS_theme = "music/muzon/PS_theme.mp3"
    m1 = "music/muzon/m1.mp3"
    hope = "music/muzon/hope.mp3"
    mm = "music/muzon/mm.mp3"
    battle = "music/muzon/battle.mp3"
    ending = "music/muzon/ending.mp3"
    night = "music/muzon/night.mp3"
    fan = "music/muzon/Fan.mp3"
    prir = "music/muzon/prir.mp3"
    ka = "music/muzon/Ka.mp3"
    truth = "music/muzon/truth.mp3"
    le = "music/muzon/Level Editor.mp3"
    l_t = "music/muzon/L_theme.mp3"
    master_plan = "music/muzon/master_plan.mp3"
    ika = "music/muzon/ika.mp3"


    korol = "music/muzon/KiS.wav"

    ##Звуки
    tlprt = "music/sfx/tlprt.wav"
    door = "music/sfx/door.mp3"
    horror = "music/sfx/horror.mp3"
    zip = "music/sfx/zip.mp3"
    knife = "music/sfx/knife.mp3"
    knife_loop = "music/sfx/knife_loop.mp3"
    open_resh = "music/sfx/open_resh.wav"
    sirena = "music/sfx/sirena.wav"
    shursh = "music/sfx/shursh.wav"
    top = "music/sfx/top.wav"
    elektr = "music/sfx/elektro.wav"
    electr = "music/sfx/elektro.wav"
    vzriv = "music/sfx/vzriv.mp3"
    
    


    ## ПЕРЕХОДЫ
    blind_02 = ImageDissolve("eff/002-Blind02.png", 2.0, 50, reverse=False)
    
    
    random_02 = ImageDissolve("eff/010-Random02.png", 2.0, 200, reverse=False)
    random_02_r = ImageDissolve("eff/010-Random02.png", 2.0, 200, reverse=True)

    random_02_3 = ImageDissolve("eff/010-Random02.png", 3.0, 50, reverse=False)
    random_02_r_3 = ImageDissolve("eff/010-Random02.png", 3.0, 50, reverse=True)
    
    random_04 = ImageDissolve("eff/012-Random04.png", 2.5, 100, reverse=False)

    bg_effect_13 = ImageDissolve("eff/108_BG_EFFECT_13.png", 3.0, 100, reverse=False)
    bg_effect_13_r = ImageDissolve("eff/108_BG_EFFECT_13.png", 2.0, 100, reverse=True)

    bg_effect_14 = ImageDissolve("eff/109_BG_EFFECT_14.png", 2.0, 100, reverse=False)
    
    kagura_12 = ImageDissolve("eff/kagura (12).jpg", 1.5, 30, reverse=False)
    
    kagura_16 = ImageDissolve("eff/kagura (16).jpg", 2.0, 30, reverse=False)
    
    kagura_17 = ImageDissolve("eff/kagura (17).jpg", 3.5, 30, reverse=False)
    
    kagura_04 = ImageDissolve("eff/kagura (4).jpg", 1.0, 100, reverse=False)
    
    Line01 = ImageDissolve("eff/007-Line01.png", 2.5, 100, reverse=False)

init:

    ## ПРОСТО АРТЫ
    image splash = "img/menu/splash.jpg"
    
    image hover = "img/menu/pref/Sett_hover.png"
    image idle = "img/menu/pref/Sett_idle.png"

    image bd = "img/bd.png"


    ## МЕНЮ
    image menushka = "img/menu/menu.jpg"


    
    ## СПРАЙТЫ
    image abc1 = "img/spr/abc1.png"
    image abc2 = "img/spr/abc2.png"
    image abc3 = "img/spr/abc3.png"
    image abc4 = "img/spr/abc4.png"
    image abc5 = "img/spr/abc5.png"
    image abc6 = "img/spr/abc6.png"
    image abc7 = "img/spr/abc7.png"
    image abc8 = "img/spr/abc8.png"
    image abc9 = "img/spr/abc9.png"
    image abc10 = "img/spr/abc10.png"
    image abc11 = "img/spr/abc11.png"
    
    image akts = "img/spr/akts.png"
    image akts1 = "img/spr/akts1.png"
    image akts2 = "img/spr/akts2.png"
    image akts3 = "img/spr/akts3.png"
    image akts5 = "img/spr/akts5.png"

    image inab = "img/spr/inab.png"

    image khk = "img/spr/khk.png"
    image khk1 = "img/spr/khk1.png"

    image miu1 = "img/spr/miu1.png"
    image miu2 = "img/spr/miu2.png"
    image miu3 = "img/spr/miu3.png"
    image miu4 = "img/spr/miu4.png"
    image miu5 = "img/spr/miu5.png"
    image miu6 = "img/spr/miu6.png"
    image miu7 = "img/spr/miu7.png"
    image miu9 = "img/spr/miu9.png"
    image miu10 = "img/spr/miu11.png"
    image miu11 = "img/spr/miu11.png"
    image miu12 = "img/spr/miu12.png"

    image saik = "img/spr/saik.png"
    image saik1 = "img/spr/saik1.png"
    image saik2 = "img/spr/saik2.png"
    
    image suz = "img/spr/suz.png"
    image suz0 = "img/spr/suz0.png"
    image suz1 = "img/spr/suz1.png"
    image suz4 = "img/spr/suz4.png"

    image tsr = "img/spr/tsr.png"
    image tsr1 = "img/spr/tsr1.png"
    image tsr3 = "img/spr/tsr3.png"

    image yuki = "img/spr/uki.png"

    image kub = "img/spr/kub.png"




    ## CG
    
    image adc = "img/cg/adc.png"
    image adc1 = "img/cg/adc1.png"
    image adc2 = "img/cg/adc2.png"
    image adc3 = "img/cg/adc3.png"
    image adc4 = "img/cg/adc4.png"
    image adc5 = "img/cg/adc5.png"
    image adc6 = "img/cg/adc6.png"
    image adc7 = "img/cg/adc7.png"
    image adc8 = "img/cg/adc8.png"
    
    image AKmio = "img/cg/AKmio.png"

    image aksL = "img/cg/aksL.png"
    image aksL2 = "img/cg/aksL2.png"
    
    image badend = "img/cg/badend.png"
    image badend0 = "img/cg/badend0.png"
    
    image bod = "img/cg/bod.png"

    image ghj = "img/cg/ghj.png"

    image hj = "img/cg/hj.png"
    image hjc = "img/cg/hjc.png"
    image hjcp = "img/cg/hjcp.png"
    
    image knh1 = "img/cg/knh1.png"
    image knh2 = "img/cg/knh2.png"
    
    image plan1 = "img/cg/plan1.png"
    image plan2 = "img/cg/plan2.png"
    image plan3 = "img/cg/plan3.png"

    image miud = "img/cg/miud.png"

    image rpg = "img/cg/rpg.png"
    image rpg1 = "img/cg/rpg1.png"
    image rpg2 = "img/cg/rpg2.png"
    image rpg5 = "img/cg/rpg3.png"

    image sai = "img/cg/sai.png"
    
    image tanH = "img/cg/tanH.png"
    image tanH2 = "img/cg/tanH2.png"

    image tsD = "img/cg/tsD.png"
    
    image hand = "img/cg/hand.png"
    
    image white = "img/cg/white.png"
    image black = "img/cg/black.png"
    
    image dvor1 = "img/dvor/no1.png"
    image dvor2 = "img/dvor/no2.png"
    image dvor3 = "img/dvor/no3.png"
    image dvor4 = "img/dvor/no4.png"

    image work = "img/cg/work.png"

    image Empty = "img/cg/Empty.jpg"

    image ending2 = "img/cg/ending2.png"

    image fire = "img/cg/fire.png"

    image God = "img/cg/God.png"

    image Inab = "img/cg/inab.png"
    image Inab1 = "img/cg/inab1.png"

    image kht1 = "img/cg/kht1.png"
    image kht2 = "img/cg/work.png"

    image MiuOhi = "img/cg/MiuOhi.jpg"

    image night1 = "img/cg/night1.png"
    image night2 = "img/cg/night2.png"
    image night3 = "img/cg/night3.png"

    image people = "img/cg/people.png"

    image sayD = "img/cg/sayD.png"

    image splash2 = "img/cg/splash2.png"
    
    image tnk = "img/cg/tnk.png"
    image tnk2 = "img/cg/tnk2.png"

    image zpi1 = "img/cg/zpi1.jpg"

    image kub1 = "img/cg/куб1.png"

    image dieK = "img/cg/dieK.png"

    image ending3 = "img/cg/ending3.jpg"
    


    ## BG 

    image dick = "img/bg/dick.png"

    image dayR = "img/bg/dayR.jpg"
    image nightR = "img/bg/nightR.jpg"
    
    image hool = "img/bg/hool.png"
    image hool3 = "img/bg/hool3.jpg"
    
    image prisn = "img/bg/prisn.jpg"

    image kitsh = "img/bg/kitch.png"

    image MD = "img/bg/MD.png"
    image MD2 = "img/cg/MD2.png"

    image turm = "img/bg/turm.png"

    image priem = "img/bg/priem.png"

    image room = "img/bg/room.png"

    image sideR = "img/bg/sideR.jpg"

    image sil = "img/bg/sil.jpg"

    image pol = "img/bg/pol.jpg"


    ## Секретики

    image trun = "img/trun.jpg"
    
    
## Глитч
init python:
    import random

    nonunicode = "◘♦•○▬▬▬▬♂♂♂7♠cX○▐╪Є╗₽℠º°?¤?¦§?©?«¬®?°±??µ¶·?»?ЙйЦцУуКкЕеНнГгШшЩщЗзХхЪъФфЫыВвАаПпРрОоЛлДдЖжЭэЯяЧчСсМмИиТтЬьБбЮюAAAAAA?CEEEEIIII?NOOOOO?OUUUUY??aaaaaa?ceeeeiiii?nooooo?ouuuuy?yAaAaAaCcCcCcCcDdDdEeEeEeEeEeGgGgGgGgHhHhIiIiIiIiIJjKk?LlLlLl??LlNnNnNn???OoOoOo??RrRrRrSsSsSsSsTtTtTtUuUuUuUuUuUuWwYyYZzZzZz"

    def glitchtext(length):
        output = ""
        for x in range(length):
            output += random.choice(nonunicode)
        return output


## ТРАНСФОРМЫ

transform badend0:
    zoom 1.05 anchor (48,27)

    ease 0.1 pos (0, 0)
    ease 0.1 pos (0,25)
    ease 0.1 pos (0, 0)
    ease 0.1 pos (-0,25)
    ease 0.1 pos (0, 0)
    ease 0.1 pos (0,25)
    ease 0.1 pos (0, 0)
    ease 0.1 pos (-0,25)

    ease 0.2 pos (0, 0)
    ease 0.2 pos (0,25)
    ease 0.2 pos (0, 0)
    ease 0.2 pos (-0,25)
    ease 0.2 pos (0, 0)
    ease 0.2 pos (0,25)
    ease 0.2 pos (0, 0)
    ease 0.2 pos (-0,25)

    block:

        ease 0.3 pos (0, 0)
        ease 0.3 pos (0,25)
        ease 0.3 pos (0, 0)
        ease 0.3 pos (-0,25)    
        ease 0.3 pos (0, 0)
        ease 0.3 pos (0,25)
        ease 0.3 pos (0, 0)
        ease 0.3 pos (-0,25) 

        repeat 



### РЕГИСТРАЦИЯ МУЗ.КАНАЛОВ
init python:

## silver_lights
    def sil_play(silver_lights, chan = "music", fin = 1.0, fout = 1.0):
        renpy.play(silver_lights + ".mp3", channel = chan, loop = True, fadein = fin, fadeout = fout)
    # канал на паузу
    def sil_pause(channel = "music"):
        c = renpy.audio.audio.get_channel(channel)
        c.pause()
    # снять с паузы
    def sil_un_pause(channel = "music"):
        c = renpy.audio.audio.get_channel(channel)
        c.unpause()
    def sil_stop(chan = "music", fout=1.0):
        renpy.music.stop(channel = chan, fadeout = fout)





