
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
define j = Character(_("Juni"), kind=nvl, color="#deb2d1", window_background="images/frame_persona.png")
define Sr = Character(_("Sr. Star"), kind=nvl, color="#e93c59", window_background="images/frame_persona.png")
define n = Character(_("Nadia"), kind=nvl, color="#871abe", window_background="images/txtbox.png")
define r = Character(_("Roko"), kind=nvl, color="#54ff95")
define m = Character(_("Moonie"), kind=nvl, color="#5754ff", window_background="images/txtbox2.png", what_xpos=0.06, who_xpos=0.57)
define narrator = Character(None, kind=nvl, what_xpos=0.1)

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
    "Som, som, testando… E-hem…"
    Sr "Boa noite, senhoras e senhores telespectadores!"
    Sr "Agradeço sua sublime companhia que nos permite estar neste palco tão acolhedor"
    "{i}Eu estou tão nervosa. Não acredito que isso realmente tá acontecendo…{/i}"
    Sr "Eu sou o Sr. Star e este é o primeiro episódio de {i}STAR'S SELECTION!{/i}"
    Sr "A partir de uma avaliação prévia, haverão cinco trainees com potencial para debutar."
    Sr "No entanto, apenas uma delas irá ser capaz de superar e mostrar ao mundo suas habilidades!"
    #mudar para sorriso arrogante
    Sr "Agora, eu sei que vocês devem estar curiosos para conhecer elas… Hehe, eu também estou!"
    Sr "Então vamos conferir as nossas candidatas!"
    Sr "Começando por..."
    Sr "Srta. Linnie!"
    Sr "Com suas habilidades excepcionais de canto e visuais incríveis, mesmo tão jovem, é definitivamente um charme para os fãs!"
    Sr "Srta. Linne, gostaria de compartilhar algo sobre suas expectativas com o programa?"
    #colocar piscadinha
    l "Primeiramente, boa noite a todos!"
    #colocar sorriso falso
    l "Gostaria de agradecer a todos os fãs que me deram a oportunidade de estar aqui, sem seu apoio eu não seria capaz de ir tão longe!"
    l "Eu prometo que não irei decepcionar vocês!"
    #colocar hiperreação do Sr Star
    Sr "Ahhhh! Como ela é encantadora, muito obrigado pelas suas palavras!"
    Sr "Sente-se aqui, por favor."
    l "Obrigada."
    Sr "Agora, nossa próxima candidata."
    # Luzes apontam para Nadia
    Sr "Eu lhes apresento: Srta. Nadia!"
    n "Olá, mundo! Preparem-se pois eu vou com tudo!"
    Sr "Caramba, e que baita personalidade…"
    #risadas programadas do público
    Sr "Mas o que é um reality sem um pouco de encrenca, não é mesmo? Hehehe"
    n "Como é?!"
    #ela parece incomodada
    Sr "Nada, minha querida! Era só brincadeira!"
    Sr "Fique à vontade para falar com o público."
    Sr "Mas cuidado com o que diz, senhorita, pois todos estão ouvindo!"
    n "Humpf! Muito bem..."
    #ela olha para a câmera
    n "Sei que poucas pessoas me conhecem e esta será sua primeira impressão de mim..."
    #olhar determinado
    n "Mas eu quero deixar claro quem eu sou e que não me deixarei perder pelo caminho."
    n "Esta é uma grande oportunidade e eu não vou desperdiçá-la. Irei lutar até o fim!"
    #falso sorriso do sr star
    Sr "Quanta determinação! É assim que se fala, Nadia! Agora, pode se dirigir ao seu assento."
    Sr "A nossa próxima convidada ganhou o olhar dos nossos jurados à primeira vista, uma pérola rara!"
    Sr "Apresento-lhes: Srta. Junnie!"
    #junnie tímida
    j "O-Olá, pessoal…!"
    Sr "Vamos lá, não seja tímida, certamente há muito que você queira dizer."
    j "Certo, bem… Meu nome é Junnie e e-eu realmente quero conseguir debutar…"
    j "Conto com o apoio de todos vocês!"
    Sr "Obrigada, querida, espero que possamos vê-la evoluir na sua timidez…"
    Sr "A próxima candidata tem um nome relativamente conhecido…"
    Sr "Não para a indústria da música muito embora, e sim para a de cosméticos!"
    Sr "Com vocês, Srta. Roko!"  
    r "Boa noite, Sr. Star! Boa noite, todo mundo!"
    Sr "Olá, querida! Há muito tempo que não vejo seu rosto por aqui."
    #o sr star faz cara de confuso
    Sr "Perdoe-me pela deselegância, se me cabe a pergunta, mas o que traz você aqui?"
    r "Oh, Sr. Star, sinto que devo correr atrás dos meus sonhos, devo viver o mundo eu mesma!"
    #faz cara de drama
    r "Sei que muitos acreditam que o dinheiro me garante um futuro, mas não é assim! Eu tenho que conquistar por mim mesma!"
    r "Portanto, estou aqui para provar meu valor."
    #Sr. star faz cara de choro
    Sr "Oh, meu Deus, que comovente! Seja bem-vinda para mostrar seu talento…"
    Sr "Bem, o show deve continuar…"
    Sr "Por último mas não menos importante,"
    "{i}É minha vez, é agora ou nunca…{/i}"
    Sr "Um rosto novo nas câmeras, com um potencial de desenvolvimento em todas as habilidades!"
    Sr "Aqui vem Srta. Moonie!"
    m "Boa noite!"

    
    #hide palco
    #with fade

    label prologo2:
    # Cena apos apresentacao
    # As participantes conversam entre si

    hide lo    

    # o jogador pode ou nao falar com as personagens

    m "Após a apresentação, todas as participantes se reuniram nos bastidores"
    m "Elas estão conversando... devo me juntar a elas?"

    
    menu (nvl=True):
        "Se juntar a conversa":
            show linne at left:
                zoom 1.5
                
            l "Tô tão animada! Mal posso esperar pra começar"

            "Ela abre um sorriso confiante e alegre"

            l "E vocês? Como se sentem?"

            hide linne
            show juni at left:
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
