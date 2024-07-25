init python:
    # must be persistent to be able to record the scores
    # after adding new songs, please remember to delete the persistent data

    rhythm_game_songs = [
    Song('Isolation', 'audio/Isolation.mp3', 'audio/Isolation.beatmap.txt'),
    Song('Positivity', 'audio/Positivity.mp3', 'audio/Positivity.beatmap.txt'),
    Song('Pearlescent', 'audio/Pearlescent.mp3', 'audio/Pearlescent.beatmap.txt'),
    Song('Pearlescent - trimmed', 'audio/Pearlescent - trimmed.mp3', 'audio/Pearlescent - trimmed.beatmap.txt'), # 22 sec, easy to test 
    Song('Thoughts', 'audio/Thoughts.mp3', 'audio/Thoughts.beatmap.txt')
    ]

    # # init
    # if persistent.rhythm_game_high_scores:
    #     for song in songs:
    #         if not song in persistent.rhythm_game_high_scores:
    #             persistent.rhythm_game_high_scores[song] = (0, 0)

# map song name to high scores
default persistent.rhythm_game_high_scores = {
    song.name: (0, 0) for song in rhythm_game_songs
}

# the song that the player chooses to play, set in `choose_song_screen` below
#image nadia = "images/side_nadia_happy.png"
default selected_song = None

define l = Character(_("Linne"), kind=nvl, color="#fff422")
define j = Character(_("Juni"), kind=nvl, color="#deb2d1")
define Sr = Character(_("Sr. Star"), kind=nvl, color="#e93c59")
define n = Character(_("Nadia"), kind=nvl, color="#871abe", image="nadia")
define r = Character(_("Roko"), kind=nvl, color="#54ff95")
define m = Character(_("Moonie"), kind=nvl, color="#5754ff")
define narrator = Character(None, kind=nvl)

define config.nvl_page_ctc = True

#define menu = nvl_menu

image linne = "images/sylvie blue normal.png"
image juni = "images/sylvie green giggle.png"
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

            label test:
                Sr "Welcome to the Ren'Py Rhythm Game! Ready for a challenge?"
                window hide
                $ quick_menu = False

                # avoid rolling back and losing chess game state
                $ renpy.block_rollback()

                $ song = Song('Isolation', 'audio/Isolation.mp3', 'audio/Isolation.beatmap.txt', beatmap_stride=0.1)
                $ rhythm_game_displayable = RhythmGameDisplayable(song)
                call screen rhythm_game(rhythm_game_displayable)

                # avoid rolling back and entering the chess game again
                $ renpy.block_rollback()

                # restore rollback from this point on
                $ renpy.checkpoint()

                $ quick_menu = True
                window show

                return
        "Prologo":
            menu:
                "parte 1":
                    jump prologo1

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

        "Textbox":
            jump textbox

label textbox:
    #n happy "feliz"
    #n sad "triste"
    nvl clear
    jump teste
label jogo:
    #Inicio do jogo

label Prologo:
    label prologo1:
    
    show bg
    show lo
   
    #show palco at truecenter:
    #    zoom 2
    #with dissolve"""
    "Os sets de gravação estão prontos e é neste momento que somos avisadas que o show vai começar."
    Sr "Senhoras e senhores, sejam bem vindos!"
    "Tô tão nervosa... Nem acredito que isso realmente tá acontecendo..."
    Sr "Eu sou o Sr. Star e este é o primeiro episódio do REALITY STAR'S SELECTION!"
    Sr "A partir de uma seleção prévia, temos aqui cinco treinees com sublime potencial para debutar..."
    Sr "No entanto, apenas uma delas irá ser capaz de se superar e mostrar ao mundo suas habilidades!"
    Sr "Agora, eu sei que vocês devem estar curiosos para conhecer elas, então vamos conferir as nossas candidatas!"
    Sr "Começando por..."
    "As câmeras e as luzes viram para o palco e apontam para a primeira candidata, dando destaque a uma garota de aparência milimetricamente impecável."
    Sr "Srta. Moonie!"
    #ela entra na tela
    Sr "Com suas habilidades excepcionais de canto e visuais incríveis, apesar da idade, é definitivamente um charme para os fans!"
    Sr "Srta. Linne, gostaria de compartilhar algo sobre suas expectativas com o programa?"
    l "Primeiramente, boa noite a todos!"
    "Ela sorri e posa para a câmera fazendo um gesto de aegio."
    l "E segundamente, gostaria de agradecer a todos os fans que me deram a oportunidade de estar aqui, sem seu apoio eu não seria capaz de ir tão longe!"
    "Ainda com um sorriso no rosto ela fecha os olhos e junta as mãos em um gesto de gratidão."
    l "Eu prometo que não irei decepcionar vocês!"
    Sr "Ahhhh! Como ela é encantadora, muito obrigado pelas suas palavras! Sente-se aqui, por favor."
    "Ela acena de forma fofa para o apresentador, indo para uma das cadeiras dispostas no palco."
    Sr "Agora, nossa próxima candidata."
    # Luzes apontam para Nadia
    Sr "Eu lhes apresento: Srta. Nadia!"
    Sr "Essa já esteve envolvida em algumas polemicas..."
    Sr "Mas o que é um reality sem um pouco de encrenca, não é mesmo? heheheh"
    n "Como é?!!"
    #ela parece imcomodada
    Sr "Nada, querida! Era só brincadeira!"
    Sr "Fique à vontade para falar com o público."
    Sr "Mas cuidado com o que diz, mocinha, pois está todo mundo escutando!"
    n "Hump! Muito bem, nesse caso..."
    #ela olha p/ camera
    n "Sei que muitos de vocês me conhecem pelos motivos errados e já têm uma opinião formada sobre mim..."
    n "Mas eu mudei, e conquistei uma vaga nesse grande reality!"
    n "Essa é uma grande oportunidade e eu não irei disperdiça-la. Vou lutar até o fim!"
    Sr "Quanta determinação! É assim que se fala, Nadia! Agora, pode se dirigir ao seu assento."
    #Luzes de nadia apagam
    Sr "A nossa próxima convidada é um doce de pessoa!"

    
    #hide palco
    #with fade

    label prologo2:
    # Cena apos apresentacao
    # As participantes conversam entre si
    

    # o jogador pode ou nao falar com as personagens

    "Após a apresentação, todas as participantes se reuniram nos bastidores"
    "Elas estão conversando... devo me juntar a elas?"

    menu (nvl=True):
        "Se juntar a conversa":
            show linne at truecenter:
                zoom 1.5
                
            l "Tô tão animada! Mal posso esperar pra começar"

            "Ela abre um sorriso confiante e alegre"

            l "E vocês? Como se sentem?"

            hide linne
            show juni at truecenter:
                zoom 1.5
            j "... Me sinto enjooada "


        "Nao falar com ninguem":

            "Ta maluco vo eh dormi kkkkk"


    label fimprologo:
    "Após a conversa, as participantes são dirijidas até sua moradia durante o período do Jogo."
    "Moonie analisa o local e se instala em seu dormitório ao final do dia, dando início ao primeiro capítulo"

label Capitulo1:

    label cap1_1:
        "O paresentador explica o método de cíclos e das avaliações por apresentação para o público."
        "As avaliações seram feitas por meio da pontuação nos minigames"

    label cap1_2:
        "Hoje teremos o nosso primeiro teste de desempenho..."
        "O que será que nos espera?"

        Sr "Fique à vontade para escolher a música quem preferir"

label Capitulo2:
    
label end:

    #if pts == 25:
    #   "parabens! [pts]"
        
    return
