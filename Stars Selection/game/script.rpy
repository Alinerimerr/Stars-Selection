init python:

    # variaveis do dia
    dia = 0
    periodo = "Noite"
    evento = True

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
    ajudaj = False
    vermelho = False
    ignorante = False
    treinoroko = False

    # variaveis cap2
    aceitar = False

    # variaveis do timer
    time = 0
    timerrange = 0
    timerjump = 0

define lh = Character(("Linne"), kind=nvl, color="#fff422", windowbackground="images/novas txtbox/linniehappy.png")
define ln = Character(("Linne"), kind=nvl, color="#fff422", windowbackground="images/novas txtbox/linnienormal.png")
define la = Character(("Linne"), kind=nvl, color="#fff422", windowbackground="images/novas txtbox/linnieangry.png")

define jh = Character(("Juni"), kind=nvl, color="#deb2d1", windowbackground="images/novas txtbox/junnihappy.png")
define jn = Character(("Juni"), kind=nvl, color="#deb2d1", windowbackground="images/novas txtbox/junninormal.png")
define ja = Character(("Juni"), kind=nvl, color="#deb2d1", windowbackground="images/novas txtbox/junniangry.png")

define Srh = Character(("Sr. Star"), kind=nvl, color="#e93c59", windowbackground="images/novas txtbox/srstarhappy.png")
define Srn = Character(("Sr. Star"), kind=nvl, color="#e93c59", windowbackground="images/novas txtbox/srstarnormal.png")
define Sra = Character(("Sr. Star"), kind=nvl, color="#e93c59", windowbackground="images/novas txtbox/srstarangry.png")
define Srsu = Character(("Sr. Star"), kind=nvl, color="#e93c59", windowbackground="images/novas txtbox/srstarsurprise.png")
define Srsc = Character(("Sr. Star"), kind=nvl, color="#e93c59", windowbackground="images/novas txtbox/srstarscary.png")

define nh = Character(("Nádia"), kind=nvl, color="#871abe", windowbackground="images/novas txtbox/nadiahappy.png")
define nn = Character(("Nádia"), kind=nvl, color="#871abe", windowbackground="images/novas txtbox/nadianormal.png")
define na = Character(("Nádia"), kind=nvl, color="#871abe", windowbackground="images/novas txtbox/nadiaangry.png")
define nsu = Character(("Nádia"), kind=nvl, color="#871abe", windowbackground="images/novas txtbox/nadiasurprise.png")

define rh = Character(("Roko"), kind=nvl, color="#54ff95", windowbackground="images/novas txtbox/rokohappy.png")
define rn = Character(("Roko"), kind=nvl, color="#54ff95", windowbackground="images/novas txtbox/rokonormal.png")
define ra = Character(("Roko"), kind=nvl, color="#54ff95", windowbackground="images/novas txtbox/rokoangry.png")


define m = Character(("Moonie"), kind=nvl, color="#5754ff", windowbackground="images/txtbox52.png", whatxpos=0.06, whoxpos=0.57, whatwidth=0.7)
define p = Character(("Pensamento"), kind=nvl, whatxpos=0.1)
define narrator = Character(None, kind=nvl, whatxpos=0.1)
define tempo = Character(None, whatypos=3.5, fontsize=20)

define config.nvlpagectc = True

image bg = "images/bg.png"
image lo = "images/lo2.png"

transform alphadissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

screen daydisplay:
    text "Dia: [dia]" ypos 0.85 xpos 0.05
    text "Período: [periodo]" ypos 0.9 xpos 0.05 

screen countdown:
    timer 1 repeat True action If(time > 0, true=SetVariable('time', time  1), false=[Hide('countdown'), Jump(timer_jump)])
    if time <= 2:
        text str(time) xpos .1 ypos .1 color "#FF0000" at alphadissolve
    else:
        text str(time) xpos .1 ypos .1 at alphadissolve

# The game starts here.

label start:
    #Inicio do jogo

      
    show bg

    show lo

    show screen daydisplay

    #tempo "Bom dia"

    #$ time = 5
    #$ timerrange = 5
    #$ timerjump = 'menu1slow'
    #show screen countdown
        # hide screen countdown
  
  
    jump prologo1_i
