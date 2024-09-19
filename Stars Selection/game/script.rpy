﻿
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

    #pts de amizade
    linne = 0
    nadia = 0
    juni = 0
    roko = 0
    star = 0

    # variaveis p/ dialogo prologo
    familia = False
    fama = False
    reconh = False

    # variaveis p/ dialogo prologo
    ajuda_j = False

# map song name to high scores
default persistent.rhythm_game_high_scores = {
    song.name: (0, 0) for song in rhythm_game_songs
}

# the song that the player chooses to play, set in `choose_song_screen` below
#image nadia = "images/side_nadia_happy.png"
default selected_song = None

define l = Character(_("Linne"), kind=nvl, color="#fff422", window_background="images/txtbox3.png")
define j = Character(_("Juni"), kind=nvl, color="#deb2d1", window_background="images/txtbox-junni.png")
define Sr = Character(_("Sr. Star"), kind=nvl, color="#e93c59", window_background="images/txtbox3.png")
define n = Character(_("Nadia"), kind=nvl, color="#871abe", window_background="images/txtbox-nadia.png")
define r = Character(_("Roko"), kind=nvl, color="#54ff95", window_background="images/txtbox-roko.png")
define m = Character(_("Moonie"), kind=nvl, color="#5754ff", window_background="images/txtbox3.png", what_xpos=0.06, who_xpos=0.57, what_width=0.7)
define narrator = Character(None, kind=nvl, window_background="images/txtbox3.png", what_xpos=0.1)

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
