
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
define m = Character(_("Moonie"), kind=nvl, color="#5754ff", window_background="images/txtbox2.png", what_xpos=0.06, who_xpos=0.57, what_width=0.7)
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

        "teste fa":
            jump testef


label jogo:
    #Inicio do jogo

      
    show bg
    show lo
    jump prologo1_i

    label prologo1_m:
        "Essa pode ser a minha chance de impressionar o Sr.Star."
        "O que devo fazer?"

        menu(nvl=true):
            "Compartilhar sobre sua jornada."
                
            "Falar sobre suas expectativas."

            "Apelar pro público."

    
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
