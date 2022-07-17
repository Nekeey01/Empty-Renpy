init:
    image yuika text = Text("{size=150}{color=#930000}{font=fonts/prison.ttf}YuiKa Games Studio{/size}{/color}{/font}")
    image pred text = Text("{size=150}{color=#930000}{font=fonts/prison.ttf}представляет{/size}{/color}{/font}")
    image projekt text = Text("{size=170}{color=#930000}{font=fonts/prison.ttf}проект{/size}{/color}{/font}")


    image roof = Text("{size=170}{color=#930000}{font=fonts/prison.ttf}крыша{/size}{/color}{/font}")
    image kitchen = Text("{size=170}{color=#930000}{font=fonts/prison.ttf}кухня{/size}{/color}{/font}")
    image floor = Text("{size=170}{color=#930000}{font=fonts/prison.ttf}первый этаж{/size}{/color}{/font}")
    image kab_dir = Text("{size=170}{color=#930000}{font=fonts/prison.ttf}кабинет директора{/size}{/color}{/font}")


transform plav:
    yalign 0.0
    linear 4.0 yalign 1.0

screen code:
    button background None keyboard_focus False xysize (0,0) action Call("kod") keysym("shift_K_a") 



label splashscreen:
    # show screen code(_layer='overlay')
    
    
    if persistent.prolog:
        
        $ renpy.pause(1.0, hard=True)
        play music m1
        
        show splash with random_02_r_3
        pause 3.0
        hide splash with random_02_3 
        pause 0.5
        
        scene white with dissolve
        pause 1.0
        
        show adc1 with dissolve
        pause 2.0 
        
        show adc2 with dissolve
        pause 2.0 

        
        show adc3 with dissolve
        pause 2.0 

        "Извини...{w}что так получилось...{w}мы обязательно...{w}скоро снова встретимся..."
        
        show adc4 with dissolve
        pause 2.0
        
        scene adc with dissolve:
            yalign 0.0
            linear 7.0 yalign 1.0
            
        pause 8.0
        
        scene white 
        pause 0.5
        
        show adc5 at plav with dissolve
        pause 4.5
        
        scene white 
        pause 0.5
        
        show adc6 at plav with dissolve
        pause 4.5
        
        scene adc7 with dissolve
        pause 4.5
        
        vopros "Ну что я за неудачник..."
        vopros "Вчера с работы уволили...{w}Бросила девушка...{w}Большие долги, котрые я не смогу оплатить...{w}Еще и одставили..."
        scene adc8 with dissolve
        pause 2.0
        
#       % черный, затем пауза и арт (пустые)
        stop music fadeout 2
        pause 2.1
        
        $ persistent.logo = True
        $ persistent.prolog = False
        return
        
        
    if persistent.logo:
        pause 1.0 


        $ sil_play("music/muzon/Silver Lights")

        show splash with random_02_r_3
        pause 3.0
        hide splash with random_02_3 




    # if persistent.splash:
    #     if not persistent.logo:
    #         $ sil_play("music/muzon/Silver Lights")
    #     else:
    #         $ silver_music = True
             
    #     scene menushka with random_04
    #     pause 1.0
        
    #     show yuika text with bg_effect_13:  
    #         align (.5,.2)
    #     pause 1.5
       
    #     show pred text with bg_effect_13:  
    #         align (.5,.5)
    #     pause 1.5

    #     show projekt text with bg_effect_13:  
    #         align (.5, .84)
    #     pause 1.5

    #     hide yuika text 
    #     hide pred text 
    #     hide projekt text 

    #     with bg_effect_13_r

    #     show text "{size=260}{cps=1}{color=#930000}{font=fonts/prison.ttf}''п у с т ы е''{/size}{/cps}{/color}{/font}" with bg_effect_13: 
    #         align(.5, .5)

        
    #     $ sil_pause()
        

    ## Снимаем с паузы, если была заставка
    
    return

