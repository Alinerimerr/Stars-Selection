define j = Character("Jolie")
define apresentador = Character("Apresentador")
define y = Character("Yara")

image jolie = "images/homem1.png"
image yara = "images/shrek1.png"
image palco = "images/palco1.jpg"
image bastidores = "images/bastidores.jpg"



# The game starts here.

label start:

#suponha q aq comeca a apresentacao das participantes

    play music "audio/Catwoman (from The Batman).mp3"

    show palco:
        zoom 0.5
    with dissolve

    apresentador "BOAS VINDAS AO GRANDE REALITY PROJECT_IDOL!"
    apresentador "Aqui voce ira conher personalidades marcantes que buscam o sucesso das maiores estrelas."
    apresentador "Porem, apenas uma brilhara por definitivo nesse grande reality!"
    apresentador "Qual dessas pequenas estrelas sera a vncedora? Eh o que vamos descobrir aqui em PROJECT_IDOL!"

    "{b}A apresentacao das personages comeca e acaba logo em seguida{/b}."

    apresentador "Muito bem... isso eh tudo por hoje. Ate a proxima."
    # Cena apos apresentacao
    hide palco
    with fade

    show bastidores
    with dissolve
    # o jogador pode ou nao falar com as personagens

    "Ufa! Essa apresentacao estava me matando"
    "Todas as concorrentes estao conversando nos bastidores... devo me juntar a elas?"

    menu:
        "Se juntar a conversa":
            show jolie at truecenter:
                zoom 0.4
            j "Oie!"

            hide jolie

            show jolie at right:
                zoom 0.4

            show yara at left:
                zoom 0.7

            y "CADE MEU CHOCOLATE!!??"

        "Nao falar com ninguem":
            "Ta maluco vo eh dormi kkkkk"

    # This ends the game.
    stop music

    return
