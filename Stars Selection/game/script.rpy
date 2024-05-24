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

    Sr "SENHORAS E SENHORES! SEJAM TODOS BEM VINDOS!!"
    "Que nervoso... não acredito que isso realmente está acontecendo..."
    Sr "EU SOU O SR. STAR E ESTE É O REALITY STAR'S SELECTION!"
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
