init python:
    pts = 0

    import math

    def friendship(x):
        return x

    class Appearing(renpy.Displayable):

        def __init__(self, child, opaque_distance, transparent_distance, **kwargs):

            self.child = renpy.displayable(child)

            self.opaque_distance = opaque_distance
            self.transparent_distance = transparent_distance

            self.alpha = 0.0

            self.width = 0
            self.height = 0

        def render(self, width, height, st, at):

            t = Transform(child=self.child, alpha=self.alpha)

            child_render = renpy.render(t, width, height, st, at)

            self.width, self.height = child_render.get_size()

            render = renpy.Render(self.width, self.height)

            render.blit(child_render, (0, 0))

            return render

        def event(self, ev, x, y, st):

            distance = math.hypot(x - (self.width / 2), y - (self.height / 2))

            if distance <= self.opaque_distance:
                alpha = 1.0
            elif distance >= self.transparent_distance:
                alpha = 0.0
            else:
                alpha = 1.0 - 1.0 * (distance - self.opaque_distance) / (self.transparent_distance - self.opaque_distance)

            if alpha != self.alpha:
                self.alpha = alpha
                renpy.redraw(self, 0)

            return self.child.event(ev, x, y, st)

        def visit(self):
            return [ self.child ]


define j = Character(_("Jolie"), color="#f1e842")
define c = Character(_("Coco"), color="#deb2d1")
define Sr = Character(_("Sr. Star"), color="#e93c59")
define n = Character(_("Nadia"), color="#871abe")
define m = Character(_("Moonie"), color="#54eeff")

image jolie = "images/sylvie blue normal.png"
image coco = "images/sylvie green giggle.png"
image palco = "images/teste2.png"
image bastidores = "images/bastidores.jpg"

screen alpha_magic:
    add Appearing("shrek1.png", 100, 200):
        xalign 0.5
        yalign 0.5


# The game starts here.

label start:

#Inicio da apresentacao

    #play music "audio/Catwoman (from The Batman).mp3"

    show palco at truecenter:
        zoom 2
    with dissolve
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
    "Ela sorri e posa para a câmera fazendo um gesto de ""aegio""."
    m "E segundamente, gostaria de agradecer a todos os fans que me deram a oportunidade de estar aqui, sem seu apoio eu não seria capaz de ir tão longe!"
    "Ainda com um sorriso no rosto ela fecha os olhos e junta as mãos em um gesto de gratidão."
    m "Eu prometo que não irei decepcionar vocês!"
    Sr "Ahhhh! Como ela é encantadora, muito obrigado pelas suas palavras! Sente-se aqui, por favor."
    "Ela acena de forma fofa para o apresentador, indo para uma das cadeiras dispostas no palco."
    Sr "Agora, nossa próxima candidata"
    #Sr "AQUI "

    
    hide palco
    with fade

    # Cena apos apresentacao
    show bastidores
    with dissolve

    # o jogador pode ou nao falar com as personagens

    "Após a apresentação, todas as participantes se reuniram nos bastidores"
    "Elas estão conversando... devo me juntar a elas?"

    $pts = friendship(5)

    menu:
        "Se juntar a conversa":
            show jolie at truecenter:
                zoom 1.5
                
            j "Tô tão animada! Mal posso esperar pra começar"

            "Ela abre um sorriso confiante e alegre"

            j "E vocês? Como se sentem?"

            hide jolie
            show coco at truecenter:
                zoom 1.5
            c "... Me sinto enjooada, "


            $pts += friendship(20)


        "Nao falar com ninguem":

            "Ta maluco vo eh dormi kkkkk"
            #$pts = 20

            show screen alpha_magic

            "Encontre Shrek."

            return

            jump end

    # fim do jogo
    stop music

label end:

    #renpy.display(f"Pontos: {pts}")

    if pts == 25:
        "parabens! [pts]"
        
    return
