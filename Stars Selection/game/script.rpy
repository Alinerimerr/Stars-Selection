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

define audio.maintheme = "audio/choosen_by_stars.mp3"

define lh = Character(("Linne"), kind=nvl, color="#fff387", windowbackground="images/txtbox/linnie-happy.png")
define ln = Character(("Linne"), kind=nvl, color="#fff387", windowbackground="images/txtbox/linnie-neutral.png") #medo e nervoso irritada
define la = Character(("Linne"), kind=nvl, color="#fff387", windowbackground="images/txtbox/linnie-angry.png")
define li = Character(("Linne"), kind=nvl, color="#fff387", windowbackground="images/txtbox/linnie-angry.png") #irritada
define lsu = Character(("Linne"), kind=nvl, color="#fff387", windowbackground="images/txtbox/linnie-angry.png") #nervosa/assustada/surpresa

define jh = Character(("Juni"), kind=nvl, color="#ffc1ec", windowbackground="images/txtbox/junni-happy.png")       #feliz
define jn = Character(("Juni"), kind=nvl, color="#ffc1ec", windowbackground="images/txtbox/junni-neutral.png")     #normal
define ja = Character(("Juni"), kind=nvl, color="#ffc1ec", windowbackground="images/txtbox/junni-neutral.png")     #fazerr brava*** e nervosa, surpresa
define js = Character(("Juni"), kind=nvl, color="#ffc1ec", windowbackground="images/txtbox/junni-sad.png")         #triste
define jnv = Character(("Juni"), kind=nvl, color="#ffc1ec", windowbackground="images/txtbox/junni-neutral.png")   

define Srh = Character(("Sr. Star"), kind=nvl, color="#ff879b", windowbackground="images/txtbox/srstar-happy.png")      #feliz
define Srn = Character(("Sr. Star"), kind=nvl, color="#ff879b", windowbackground="images/txtbox/srstar-neutral.png")    #normal
define Sra = Character(("Sr. Star"), kind=nvl, color="#ff879b", windowbackground="images/txtbox/srstar-angry.png")      #bravo
define Srsu = Character(("Sr. Star"), kind=nvl, color="#ff879b", windowbackground="images/txtbox/srstar-surprise.png")  #surpreso
define Srsc = Character(("Sr. Star"), kind=nvl, color="#ff879b", windowbackground="images/txtbox/srstar-scary.png")     #assustador

define nh = Character(("Nádia"), kind=nvl, color="#db93ff", windowbackground="images/txtbox/nadia-happy.png")       #feliz
define nsm = Character(("Nádia"), kind=nvl, color="#db93ff", windowbackground="images/txtbox/nadia-smile.png")      #sorrindo
define nn = Character(("Nádia"), kind=nvl, color="#db93ff", windowbackground="images/txtbox/nadia-neutral.png")     #normal
define na = Character(("Nádia"), kind=nvl, color="#db93ff", windowbackground="images/txtbox/nadia-angry.png")       #brava
define nsr = Character(("Nádia"), kind=nvl, color="#db93ff", windowbackground="images/txtbox/nadia-serious.png")    #seria/determinada
define nsu = Character(("Nádia"), kind=nvl, color="#db93ff", windowbackground="images/txtbox/nadia-surprise.png")   #surpresa

define rh = Character(("Roko"), kind=nvl, color="#81ffb1", windowbackground="images/txtbox/roko-confident.png")   #feliz  e smile  e zangada e triste/irritada  fazer***
define rn = Character(("Roko"), kind=nvl, color="#81ffb1", windowbackground="images/txtbox/roko-neutral.png")   #normal 
define ra = Character(("Roko"), kind=nvl, color="#81ffb1", windowbackground="images/txtbox/roko-angry.png")     #brava
define rc = Character(("Roko"), kind=nvl, color="#81ffb1", windowbackground="images/txtbox/roko-confident.png") #confiante (confiante nervosa)
define ri = Character(("Roko"), kind=nvl, color="#81ffb1", windowbackground="images/txtbox/roko-neutral.png")   #(ri - irritada)
define rnv = Character(("Roko"), kind=nvl, color="#81ffb1", windowbackground="images/txtbox/roko-neutral.png")  #nervosa
define rsu = Character(("Roko"), kind=nvl, color="#81ffb1", windowbackground="images/txtbox/roko-neutral.png")  #surpresa


define m = Character(("Moonie"), kind=nvl, color="#a8a7ff", windowbackground="images/txtbox52.png", whatxpos=0.06, whoxpos=0.57, whatwidth=0.7)
define p = Character(("Pensamento"), kind=nvl, whatxpos=0.1) #{/i}
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
