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
default selected_song = None
define l = Character(_("Linne"), color="#fff422")
define j = Character(_("Juni"), color="#deb2d1")
define Sr = Character(_("Sr. Star"), color="#e93c59")
define n = Character(_("Nadia"), color="#871abe")
define r = Character(_("Roko"), color="#54ff95")
define m = Character(_("Moonie"), color="#5754ff")

image linne = "images/sylvie blue normal.png"
image juni = "images/sylvie green giggle.png"
image palco = "images/teste2.png"
image bastidores = "images/bastidores.jpg"


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
            j "Mt bem"

            return

            label test:
                e "Welcome to the Ren'Py Rhythm Game! Ready for a challenge?"
                window hide
                $ quick_menu = False

                # avoid rolling back and losing chess game state
                $ renpy.block_rollback()

                $ song = Song('Isolation', 'audio/Isolation.mp3', 'audio/Isolation.beatmap.txt', beatmap_stride=2)
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

label jogo:
    #Inicio do jogo

label Prologo:
    label prologo1:
    #play music "audio/Catwoman (from The Batman).mp3"
    #show palco at truecenter:
    #    zoom 2
    #with dissolve"""
    "Os sets de gravação estão prontos e é neste momento que somos avisadas que o show vai começar."
    Sr "Senhoras e senhores, sejam bem vindos!"
    "Me sinto nervosa... Não acredito que isso realmente está acontecendo..."
    Sr "Eu sou o Sr. Star e este é o primeiro episódio do REALITY STAR'S SELECTION!"
    Sr "A partir de uma seleção prévia, temos aqui cinco treinees com sublime potencial para debutar..."
    Sr "No entanto, apenas uma delas irá ser capaz de se superar e mostrar ao mundo suas habilidades!"
    Sr "Agora, eu sei que vocês devem estar curiosos para conhecer elas, então vamos conferir as nossas candidatas!"
    Sr "Começando por..."
    "As câmeras e as luzes viram para o palco e a primeira garota da fila entra na cena."
    Sr "Srta. Moonie!"
    #ela entra na tela
    Sr "Com suas habilidades excepcionais de canto e visuais incríveis, apesar da tenra idade, é definitivamente um charme para os fans!"
    Sr "Srta. Moonie, gostaria de compartilhar algo sobre suas expectativas com o programa?"
    m "Primeiramente, boa noite a todos!"
    "Ela sorri e posa para a câmera fazendo um gesto de aegio."
    m "E segundamente, gostaria de agradecer a todos os fans que me deram a oportunidade de estar aqui, sem seu apoio eu não seria capaz de ir tão longe!"
    "Ainda com um sorriso no rosto ela fecha os olhos e junta as mãos em um gesto de gratidão."
    m "Eu prometo que não irei decepcionar vocês!"
    Sr "Ahhhh! Como ela é encantadora, muito obrigado pelas suas palavras! Sente-se aqui, por favor."
    "Ela acena de forma fofa para o apresentador, indo para uma das cadeiras dispostas no palco."
    Sr "Agora, nossa próxima candidata"
    #Sr "AQUI "

    
    #hide palco
    #with fade

    label prologo2:
    # Cena apos apresentacao
    # As participantes conversam entre si
    show bastidores
    with dissolve

    # o jogador pode ou nao falar com as personagens

    "Após a apresentação, todas as participantes se reuniram nos bastidores"
    "Elas estão conversando... devo me juntar a elas?"

    $pts += 5

    menu:
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


            $pts += 20


        "Nao falar com ninguem":

            "Ta maluco vo eh dormi kkkkk"
            #$pts = 20

    label fimprologo:
    "Após a conversa, as participantes são dirijidas até sua moradia durante o período do Jogo."
    "Moonie analisa o local e se instala em seu dormitório ao final do dia, dando início ao primeiro capítulo"

label Capitulo1:

    label parte1:
        "O paresentador explica o método de cíclos e das avaliações por apresentação para o público."
        "As avaliações seram feitas por meio da pontuação nos minigames"

    label parte2:
        "Antes dos testes haverá o peíodo de treino e após haverá o momento de descanso."

label Capitulo2:
    
label end:

    #if pts == 25:
    #   "parabens! [pts]"
        
    return
