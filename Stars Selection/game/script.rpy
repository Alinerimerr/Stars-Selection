
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
    reconh = False

    # variaveis p/ dialogo cap1
    ajuda_j = False
    vermelho = False
    ignorante = False

    # variaveis cap2
    aceitar = False

define l = Character(_("Linne"), kind=nvl, color="#fff422", window_background="images/txtbox5-2.png")
define l_t = Character(_("Linne"), kind=nvl, color="#fff422", window_background="images/txtbox-triste.png")
define l_n = Character(_("Linne"), kind=nvl, color="#fff422", window_background="images/txtbox-neutro.png")
define l_r = Character(_("Linne"), kind=nvl, color="#fff422", window_background="images/txtbox-raiva.png")
define l_m = Character(_("Linne"), kind=nvl, color="#fff422", window_background="images/txtbox-medo.png")

define j = Character(_("Juni"), kind=nvl, color="#deb2d1", window_background="images/txtbox-junni.png")
define j_t = Character(_("Juni"), kind=nvl, color="#deb2d1", window_background="images/txtbox-triste.png")
define j_n = Character(_("Juni"), kind=nvl, color="#deb2d1", window_background="images/txtbox-neutro.png")
define j_r = Character(_("Juni"), kind=nvl, color="#deb2d1", window_background="images/txtbox-raiva.png")
define j_m = Character(_("Juni"), kind=nvl, color="#deb2d1", window_background="images/txtbox-medo.png")

define Sr = Character(_("Sr. Star"), kind=nvl, color="#e93c59", window_background="images/txtbox5-2.png")
define Sr_t = Character(_("Sr. Star"), kind=nvl, color="#e93c59", window_background="images/txtbox-triste.png")
define Sr_n = Character(_("Sr. Star"), kind=nvl, color="#e93c59", window_background="images/txtbox-neutro.png")
define Sr_r = Character(_("Sr. Star"), kind=nvl, color="#e93c59", window_background="images/txtbox-raiva.png")
define Sr_m = Character(_("Sr. Star"), kind=nvl, color="#e93c59", window_background="images/txtbox-medo.png")

define n = Character(_("Nadia"), kind=nvl, color="#871abe", window_background="images/txtbox-nadia.png")
define n_t = Character(_("Nadia"), kind=nvl, color="#871abe", window_background="images/txtbox-triste.png")
define n_n = Character(_("Nadia"), kind=nvl, color="#871abe", window_background="images/txtbox-neutro.png")
define n_r = Character(_("Nadia"), kind=nvl, color="#871abe", window_background="images/txtbox-raiva.png")
define n_m = Character(_("Nadia"), kind=nvl, color="#871abe", window_background="images/txtbox-medo.png")

define r = Character(_("Roko"), kind=nvl, color="#54ff95", window_background="images/txtbox-roko.png")
define r_t = Character(_("Roko"), kind=nvl, color="#54ff95", window_background="images/txtbox-triste.png")
define r_n = Character(_("Roko"), kind=nvl, color="#54ff95", window_background="images/txtbox-neutro.png")
define r_r = Character(_("Roko"), kind=nvl, color="#54ff95", window_background="images/txtbox-raiva.png")
define r_m = Character(_("Roko"), kind=nvl, color="#54ff95", window_background="images/txtbox-medo.png")

define m = Character(_("Moonie"), kind=nvl, color="#5754ff", window_background="images/txtbox5-2.png", what_xpos=0.06, who_xpos=0.57, what_width=0.7)
define narrator = Character(None, kind=nvl, what_xpos=0.1)

define config.nvl_page_ctc = True

image bg = "images/bg.png"
image lo = "images/lo2.png"

# The game starts here.

label start:
    #Inicio do jogo

      
    show bg
    show lo
    jump prologo1_i

   
label end:
    Sr "Aqui termina a versão Demo de Star's Selection."
    Sr "Mas não pense que acaba por aqui!"
    Sr "Fique ligado para as próximas atualizações!"
    Sr "Obrigada por jogar!"
    
    return
