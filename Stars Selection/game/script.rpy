
init python:

    #pts de amizade
    linne = 0
    nadia = 0
    juni = 0
    roko = 0
    star = 0

    # pts karma
    karma = 0
    # variaveis p/ dialogo prologo
    familia = False
    fama = False
    reconhecimento = False

    # variaveis p/ dialogo cap1
    ajuda_j = False
    vermelho = False
    ignorante = False
    treino_roko = False
    linguine = False
    parmesao = False
    frango = False

    # variaveis cap2
    aceitar = False

    # variaveis do timer
    time = 0
    timer_range = 0
    timer_jump = 0

define l = Character(_("Linne"), kind=nvl, color="#fff422", window_background="images/txtbox-feliz.png")
define l_t = Character(_("Linne"), kind=nvl, color="#fff422", window_background="images/txtbox-triste.png")
define l_n = Character(_("Linne"), kind=nvl, color="#fff422", window_background="images/txtbox-neutro.png")
define l_r = Character(_("Linne"), kind=nvl, color="#fff422", window_background="images/txtbox-raiva.png")
define l_m = Character(_("Linne"), kind=nvl, color="#fff422", window_background="images/txtbox-medo.png")

define j = Character(_("Juni"), kind=nvl, color="#deb2d1", window_background="images/txtbox-junni.png")
define j_t = Character(_("Juni"), kind=nvl, color="#deb2d1", window_background="images/txtbox-triste.png")
define j_n = Character(_("Juni"), kind=nvl, color="#deb2d1", window_background="images/txtbox-neutro.png")
define j_r = Character(_("Juni"), kind=nvl, color="#deb2d1", window_background="images/txtbox-raiva.png")
define j_m = Character(_("Juni"), kind=nvl, color="#deb2d1", window_background="images/txtbox-medo.png")

define Sr = Character(_("Sr. Star"), kind=nvl, color="#e93c59", window_background="images/txtbox-feliz.png")
define Sr_t = Character(_("Sr. Star"), kind=nvl, color="#e93c59", window_background="images/txtbox-triste.png")
define Sr_n = Character(_("Sr. Star"), kind=nvl, color="#e93c59", window_background="images/txtbox-neutro.png")
define Sr_r = Character(_("Sr. Star"), kind=nvl, color="#e93c59", window_background="images/txtbox-raiva.png")
define Sr_m = Character(_("Sr. Star"), kind=nvl, color="#e93c59", window_background="images/txtbox-medo.png")

define n_f = Character(_("Nadia"), kind=nvl, color="#871abe", window_background="images/txtbox-nadia.png")
define n = Character(_("Nadia"), kind=nvl, color="#871abe", window_background="images/txtbox-nadia.png")
define n_t = Character(_("Nadia"), kind=nvl, color="#871abe", window_background="images/txtbox-triste.png")
define n_n = Character(_("Nadia"), kind=nvl, color="#871abe", window_background="images/txtbox-nadia-neutra.png")
define n_r = Character(_("Nadia"), kind=nvl, color="#871abe", window_background="images/txtbox-nadia-brava.png")
define n_m = Character(_("Nadia"), kind=nvl, color="#871abe", window_background="images/txtbox-medo.png")

define r = Character(_("Roko"), kind=nvl, color="#54ff95", window_background="images/txtbox-roko.png")
define r_t = Character(_("Roko"), kind=nvl, color="#54ff95", window_background="images/txtbox-triste.png")
define r_n = Character(_("Roko"), kind=nvl, color="#54ff95", window_background="images/txtbox-neutro.png")
define r_r = Character(_("Roko"), kind=nvl, color="#54ff95", window_background="images/txtbox-raiva.png")
define r_m = Character(_("Roko"), kind=nvl, color="#54ff95", window_background="images/txtbox-medo.png")

define m = Character(_("Moonie"), kind=nvl, color="#5754ff", window_background="images/txtbox5-2.png", what_xpos=0.06, who_xpos=0.57, what_width=0.7)
define narrator = Character(None, kind=nvl, what_xpos=0.1)
define tempo = Character(None, what_ypos=3.5, font_size=20)

define config.nvl_page_ctc = True

image bg = "images/bg.png"
image lo = "images/lo2.png"

image exc = "images/exclamation.png"

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

screen countdown:
    timer 1 repeat True action If(time > 0, true=SetVariable('time', time - 1), false=[Hide('countdown'), Jump(timer_jump)])
    if time <= 2:
        text str(time) xpos .1 ypos .1 color "#FF0000" at alpha_dissolve
    else:
        text str(time) xpos .1 ypos .1 at alpha_dissolve

# The game starts here.

label start:
    #Inicio do jogo

      
    show bg
    show lo

    #tempo "Bom dia"

    #$ time = 5
    #$ timer_range = 5
    #$ timer_jump = 'menu1_slow'
    #show screen countdown
        # hide screen countdown
   


    jump prologo1_i

   
label end:
    Sr "Aqui termina a versão Demo de Star's Selection."
    Sr "Mas não pense que acaba por aqui!"
    Sr "Fique ligado para as próximas atualizações!"
    Sr "Obrigada por jogar!"
    
    return
