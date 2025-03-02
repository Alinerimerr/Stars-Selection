init python:

    # variaveis do dia
    dia = 0
    periodo = "Noite"
    atividade = "Apresentação"

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
    tradicional = False
    parmesao = False
    frango = False
    aceitavel = False

    # variaveis cap2
    presente = False
    conjunto = False

    # variaveis cap3
    aceitar = False
    treino_juni = False

    # variaveis cap5
    pressao = False
    vitoria = False

    # variaveis do timer
    timer_range = 0
    timer_jump = 0

define lh = Character(("Linne"), kind=nvl, color="#fff387", window_background="images/txtbox/linnie-happy.png")   #feliz
define ln = Character(("Linne"), kind=nvl, color="#fff387", window_background="images/txtbox/linnie-neutral.png") #medo e nervoso
define la = Character(("Linne"), kind=nvl, color="#fff387", window_background="images/txtbox/linnie-angry.png")   #raiva
define li = Character(("Linne"), kind=nvl, color="#fff387", windowba_ckground="images/txtbox/linnie-angry.png")   #irritada

define jh = Character(("Juni"), kind=nvl, color="#ffc1ec", window_background="images/txtbox/junni-happy.png")       #feliz
define jn = Character(("Juni"), kind=nvl, color="#ffc1ec", window_background="images/txtbox/junni-neutral.png")     #normal
define ja = Character(("Juni"), kind=nvl, color="#ffc1ec", window_background="images/txtbox/junni-neutral.png")     #fazerr brava*** e nervosa
define js = Character(("Juni"), kind=nvl, color="#ffc1ec", window_background="images/txtbox/junni-sad.png")         #triste
define jnv = Character(("Juni"), kind=nvl, color="#ffc1ec", window_background="images/txtbox/junni-neutral.png")    #nervosa

define Srh = Character(("Sr. Star"), kind=nvl, color="#ff879b", window_background="images/txtbox/srstar-happy.png")      #feliz
define Srn = Character(("Sr. Star"), kind=nvl, color="#ff879b", window_background="images/txtbox/srstar-neutral.png")    #normal
define Sra = Character(("Sr. Star"), kind=nvl, color="#ff879b", window_background="images/txtbox/srstar-angry.png")      #bravo
define Srsu = Character(("Sr. Star"), kind=nvl, color="#ff879b", window_background="images/txtbox/srstar-surprise.png")  #surpreso
define Srsc = Character(("Sr. Star"), kind=nvl, color="#ff879b", window_background="images/txtbox/srstar-scary.png")     #assustador

define nh = Character(("Nádia"), kind=nvl, color="#db93ff", window_background="images/txtbox/nadia-happy.png")      #feliz
define nsm = Character(("Nádia"), kind=nvl, color="#db93ff", window_background="images/txtbox/nadia-smile.png")     #sorrindo
define nn = Character(("Nádia"), kind=nvl, color="#db93ff", window_background="images/txtbox-nadia-neutra.png")     #normal
define na = Character(("Nádia"), kind=nvl, color="#db93ff", window_background="images/txtbox/nadia-angry.png")      #brava
define nsr = Character(("Nádia"), kind=nvl, color="#db93ff", window_background="images/txtbox-nadia-neutra.png")    #seria/determinada
define nsu = Character(("Nádia"), kind=nvl, color="#db93ff", window_background="images/nadia-surprise.png")         #surpresa

define rh = Character(("Roko"), kind=nvl, color="#81ffb1", window_background="images/txtbox/roko-neutral.png")   #feliz  e smile  e zangada e triste/irritada  fazer***
define rn = Character(("Roko"), kind=nvl, color="#81ffb1", window_background="images/txtbox/roko-neutral.png")   #normal
define ra = Character(("Roko"), kind=nvl, color="#81ffb1", window_background="images/txtbox/roko-angry.png")     #brava
define rc = Character(("Roko"), kind=nvl, color="#81ffb1", window_background="images/txtbox/roko-confident.png") #confiante
define ri = Character(("Roko"), kind=nvl, color="#81ffb1", window_background="images/txtbox/roko-neutral.png")   #(ri - irritada)
define rnv = Character(("Roko"), kind=nvl, color="#81ffb1", window_background="images/txtbox/roko-neutral.png")  #nervosa
define rsu = Character(("Roko"), kind=nvl, color="#81ffb1", window_background="images/txtbox/roko-neutral.png")  #surpresa

define m = Character(("Moonie"), kind=nvl, color="#a8a7ff", window_background="images/txtbox5-2.png", what_xpos=0.07, who_xpos=0.08, what_width=0.8, font_size=120)
define p = Character(("Pensamento"), kind=nvl, whatxpos=0.1, what_xpos=0.07, who_xpos=0.08, what_width=1) #{/i}
define narrator = Character(None, kind=nvl, what_xpos=0.1)
#define tempo = Character(None, what_ypos=3.5, font_size=20)

define config.nvl_page_ctc = True

image bg = "images/bg.png"
image lo = "images/lo2.png"

define audio.maintheme = "audio/choosen_by_stars.mp3"

screen daydisplay:
    text "Dia: [dia]" ypos 0.78 xpos 0.05
    text "Período: [periodo]" ypos 0.83 xpos 0.05 
    text "Atividade: [atividade]" ypos 0.88 xpos 0.05

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

    show screen daydisplay

    #tempo "Bom dia"

    #$ time = 5
    #$ timerrange = 5
    #$ timerjump = 'menu1slow'
    #show screen countdown
        # hide screen countdown
  
  
    jump prologo1_i
