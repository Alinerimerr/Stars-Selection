label cap2_1:


    # a sequencia de dias a seguir servem apenas p/ treinamento e pequenas conversas com as personagens
    # lembrando que roko nunca se interessa por treinar muito


    # dia 2
    # musiquinha de toque de alarme (musica de kpop:)
    "{i}Ah... O alarme... Que sono...{/i}"
    "{i}Mais um dia, mais uma luta.{/i}"
    "{i}Tenho muito o que fazer hoje.{/i}"
    "Ao me levantar e lavar o rosto, lembro-me dos eventos do dia anterior."
    "{i}Hmm... Como será que estão as coisas na casa?{/i}"
    "{i}Espero que o clima não esteja tão ruim.{/i}"
    "Saio do quarto e observo o corredor, está silencioso como sempre, mas pelas luzes acesas alguém mais deve estar acordada."
    j "Oh, bom dia, Moon!"
    "Me assusto brevemente ao vê-la e percebo que Nadia também está lá."
    "Juni parece estar em um bom humor apesar da tensão."
    m "Bom dia!"
    # treino com roko na parte da manhã
    if treino_roko:
        "Tinha combinado com Roko que iríamos treinar juntas hoje."
        "Será que ela ainda está disposta... mesmo com os acontecimentos de ontem?"
        "Bem... acho que só vou descobrir se ela aparecer."
        if roko>3:
            "Após algum tempo, Roko aparece na academia."
            m "Roko, você veio!"
            r "Perdão pelo atraso..."
            r "É que eu... eu estava..."
            "Ela está nitidamente abalada."
            m "Tá... tudo bem?"
            r "Estou bem!"
            r "E-estou ótima! he he..."
            r "Não acha melhor nós começarmos?"
            m "Claro..."
            "Ficamos em silêncio durante os exercícios."
            r "..."
            "Hmm... isso é estranho."
            "Roko tem o costume de falar muito..."
            r "Ei, Moon."
            r "Acredito que..."
            r "Sabe... Talvez eu..."
            r "..."
            r "E-eu te devo desculpas!"


            menu(nvl=True):
                "Pelo que exatamente?":
                    m "Desculpas por...?"
                    r "Hã? "
                    r "Não é óbvio? Pela nota que eu dei ao seu prato!"
                    #r "Acho que no final ficou meio injusto..."
                    r "Pensei que você ficaria chateada..."
                    menu(nvl=True):
                        "Por que fez aquilo?":
                            m "Eu só queria saber o motivo dessa decisão."
                            r "Oh, bem... Não é nada contra você..."
                            r "Mas, eu não SUPORTO a ideia de dar a vitória para alguém como a Nádia!"
                            r "Você viu como ela reagiu? Totalmente fora de questão!"
                            r "E sabe... eu também fiquei bem amiga da Linne."
                            r "Ela disse que se quisermos manter nossa amizade, sempre temos que nos ajudar..."
                       
                "Não se preocupe com isso.":      
                    m "Tá tudo bem, eu não ligo pra isso."
                    r "Ah, não mesmo?"
                    r "Ufa! Que bom."
                    r "Assim eu não devo satisfação pra ninguém!"
                #"Deve mesmo!":
    #


    # dia 3


    # Final do dia 3
    "Acho que vou encerrar os treinos de hoje."
    "Amanhã já é a nossa primeira apresentação oficial..."
    "Ah, que emoção!"
    "Devo treinar mais um pouco para garantir?"
    "Não, não posso pensar assim!"
    "Fiz tudo o que podia..."
    "Eu acho."


    # dia da apresentacao
label cap2_2:
    "Hã?"
    "Acordo com o despertador me incomodando de novo."
    "Mal me levanto da cama..."
    "E já escuto barulhos vindos do lado de fora do quarto."    
    l "Ai! Toma cuidado!"
    j "Desculpa! E-eu não quis te machucar."
    "Ouço passos apressados se afastando."
    "Ahhh... Parece que o dia não começou tão bem."


    "Saio do quarto para ver o que houve."
    m "Bom dia, Linne."
    l "Oh, bom dia!"
    m "Aconteceu... alguma coisa?"
    l "Ah, não, não."
    l "Era só a Juni. Ela esbarrou em mim..."
    l "E acabou machucando meu pé."


    menu(nvl=True):
        "Foi de propósito!":
            #m "Aposto que foi de propósito!"
            m "Machucar a participante mais habilidosa do programa justo no dia da apresentação..."
            m "É no mínimo suspeito... Não?"
            "Linne ri baixinho."
            l "Ora, não podemos incrimina-lá de nada..."
            $ linne += 3
            $ karma += 5


        "Você está bem?":
            m "Nossa, eu sinto muito."
            m "Foi muito grave?"
            l "Não. Eu dou um jeito."
            l "Como sempre..."
            "..."


    l "Oh! Estou me demorando aqui."
    l "Será um dia cheio."
    m "Sim... Temos a apresentação à tarde e os resultados à noite."


    # fim desse pequeno dialogo.


    # inicio da apresentacao
    # participantes nos bastidores


    Sr "Boa noite à todos!"
    Sr "Sejam bem-vindos de volta ao reality Star's Selection!"
    Sr "E hoje, senhoras e senhores..."
    Sr "Será a primeira apresentação do programa!"
    "Luzes se acendem no palco."
    Sr "As nossas queridas participantes serão avaliadas de acordo com seus devidos desempenhos."
    Sr "Aquela que ficar em último no ranking..."
    Sr "Será, infelizmente, desqualificada do reality."
    # bla bla bla
    Sr "Começaremos com a promissora moonie!"
    "Eu!!"
    # Minigame


    "Aplausos soaram ao final da apresentação."
    Sr "Foi uma ótima apresentação!"
    # apresentacao das outras.


    # saida dos resultados
    # definir local
    Sr "Estamos de volta ao programa!"
    Sr "Espero que não tenham sentido saudades, ha ha!"
    Sr "Chegou o tão esperado..."
    Sr "O tão aguardado..."
    Sr "Momento dos resultados!"
    "A música se intensifica."
    Sr "Aparecerá no telão o ranking das performances."
    Sr "Como dito anteriormente..."
    Sr "A trainee com a menor pontuação estará fora do programa."
    Sr "A eliminada é..."
    l "É isso meninas..."
    l "Boa sorte."
    j_m "B-boa sorte."
    "Após o que parece ser uma eternidade, o ranking aparece no telão."
    "Parece que Roko ficou em último."