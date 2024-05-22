init python:
    pts = 0

    import math

    def friendship(x):
        return x

    class Appearing(renpy.Displayable):

        def __init__(self, child, opaque_distance, transparent_distance, **kwargs):

            # Pass additional properties on to the renpy.Displayable
            # constructor.
            super(Appearing, self).__init__(**kwargs)

            # The child.
            self.child = renpy.displayable(child)

            # The distance at which the child will become fully opaque, and
            # where it will become fully transparent. The former must be less
            # than the latter.
            self.opaque_distance = opaque_distance
            self.transparent_distance = transparent_distance

            # The alpha channel of the child.
            self.alpha = 0.0

            # The width and height of us, and our child.
            self.width = 0
            self.height = 0

        def render(self, width, height, st, at):

            # Create a transform, that can adjust the alpha channel of the
            # child.
            t = Transform(child=self.child, alpha=self.alpha)

            # Create a render from the child.
            child_render = renpy.render(t, width, height, st, at)

            # Get the size of the child.
            self.width, self.height = child_render.get_size()

            # Create the render we will return.
            render = renpy.Render(self.width, self.height)

            # Blit (draw) the child's render to our render.
            render.blit(child_render, (0, 0))

            # Return the render.
            return render

        def event(self, ev, x, y, st):

            # Compute the distance between the center of this displayable and
            # the mouse pointer. The mouse pointer is supplied in x and y,
            # relative to the upper-left corner of the displayable.
            distance = math.hypot(x - (self.width / 2), y - (self.height / 2))

            # Base on the distance, figure out an alpha.
            if distance <= self.opaque_distance:
                alpha = 1.0
            elif distance >= self.transparent_distance:
                alpha = 0.0
            else:
                alpha = 1.0 - 1.0 * (distance - self.opaque_distance) / (self.transparent_distance - self.opaque_distance)

            # If the alpha has changed, trigger a redraw event.
            if alpha != self.alpha:
                self.alpha = alpha
                renpy.redraw(self, 0)

            # Pass the event to our child.
            return self.child.event(ev, x, y, st)

        def visit(self):
            return [ self.child ]

define j = Character(_("Jolie"), color="#f1e842")
define apresentador = Character(_("Apresentador"), color="#e93c59")
define y = Character("Yara")

image jolie = "images/homem1.png"
image yara = "images/shrek1.png"
image palco = "images/teste2.png"
image bastidores = "images/bastidores.jpg"

screen alpha_magic:
    add Appearing("shrek1.png", 100, 200):
        xalign 0.5
        yalign 0.5


# The game starts here.

label start:

#suponha q aq comeca a apresentacao das participantes

    #play music "audio/Catwoman (from The Batman).mp3"

    show palco at truecenter:
        zoom 2
    with dissolve

    apresentador "BOAS VINDAS AO GRANDE REALITY PROJECT_IDOL!"
    

    #"{b}A apresentacao das personages comeca e acaba logo em seguida{/b}."

    #apresentador "Muito bem... isso eh tudo por hoje. Ate a proxima."
    # Cena apos apresentacao
    hide palco
    with fade

    show bastidores
    with dissolve
    # o jogador pode ou nao falar com as personagens

    #"Ufa! Essa apresentacao estava me matando"
    #"Todas as concorrentes estao conversando nos bastidores... devo me juntar a elas?"

    $pts = friendship(5)

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

            y "AAAA!"

            $pts += friendship(20)


        "Nao falar com ninguem":

            "Ta maluco vo eh dormi kkkkk"
            #$pts = 20

            show screen alpha_magic

            "Can you find the logo?"

            return

            jump end

    # This ends the game.
    stop music

label end:

    #renpy.display(f"Pontos: {pts}")

    if pts == 25:
        "parabens! [pts]"
        
    return
