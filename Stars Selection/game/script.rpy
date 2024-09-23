﻿
init python:

    #pts de amizade
    linne = 0
    nadia = 0
    juni = 0
    roko = 0
    star = 0

    # pts popularidade
    #popularidade = 0
    # variaveis p/ dialogo prologo
    familia = False
    fama = False
    reconh = False

    # variaveis p/ dialogo prologo
    ajuda_j = False

define l = Character(_("Linne"), kind=nvl, color="#fff422", window_background="images/txtbox5-2.png")
define j = Character(_("Juni"), kind=nvl, color="#deb2d1", window_background="images/txtbox-junni.png")
define Sr = Character(_("Sr. Star"), kind=nvl, color="#e93c59", window_background="images/txtbox5-2.png")
define n = Character(_("Nadia"), kind=nvl, color="#871abe", window_background="images/txtbox-nadia.png")
define r = Character(_("Roko"), kind=nvl, color="#54ff95", window_background="images/txtbox-roko.png")
define m = Character(_("Moonie"), kind=nvl, color="#5754ff", window_background="images/txtbox5-2.png", what_xpos=0.06, who_xpos=0.57, what_width=0.7)
define narrator = Character(None, kind=nvl, what_xpos=0.1)

define config.nvl_page_ctc = True

#define menu = nvl_menu

#image linne = "images/sylvie blue normal.png"
#image juni = "images/sylvie green giggle.png"
image bg = "images/bg.png"
image lo = "images/lo2.png"

image palco = "images/teste2.png"
image bastidores = "images/bastidores.jpg"

image side nadia happy = "images/side_nadia_happy.png"
image side nadia sad = "images/side_nadia_sad.png"


# The game starts here.

label start:

    menu:
        "Testar":
            jump teste
        "Início do Jogo":
            jump jogo

label teste:
    menu:
        "Minigame":
            window hide
            call rhythm_game_entry_label
            Sr "Mt bem"

            menu:
                "Sair":
                    return

                "Voltar":
                    jump teste

                "Desafio":
                    jump test    

        "Prologo":
            menu:
                "parte 1":
                    jump prologo1_m

                "parte 2":
                    jump prologo2

                "Fim prologo":
                    jump fimprologo

        "Capítulo 1":
            menu:
                "parte 1":
                    jump parte1

                "parte 2":
                    jump parte2

        "teste fa":
            jump testef


label jogo:
    #Inicio do jogo

      
    show bg
    show lo
    jump prologo1_i

   
label end:

    #if pts == 25:
    #   "parabens! [pts]"
        
    return
