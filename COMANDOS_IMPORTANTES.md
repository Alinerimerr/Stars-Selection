comandos importantes:

define ex = Character("personagem exemplo")
image ex1 = "images/exempol.png"
scene ex_fundo
show ex
hide ex
ex "oi, eu sou um exemplo."

============= ajuste de img ====================
(com show, scene ...)

show ex:
	zoom 0.5

============= transicoes =======================
(com show, scene ...)

with dissolve
with fade
with pixellate
with zoomin

============= posicoes ==========================
(com show, scene, hide)

at center
at right
at truecenter

------- ajuste manual --------

show ex:
xaling 0.5
yaling 0.5

============= musica ==========================

play music "audio/ex_musica.mp3" 	(toca em loop até a segunda ordem)
queue music "audio/ex_musica2.mp3" 	(toca após a primeira)
noloop (toca sem loop)
play sound  				(para efeitos sonoros)
stop music

============ Menu ==================================

menu:
  opcao1:
    ...

  opcao2:
    ...
