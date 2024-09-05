label cap1_1:
    "..."
    "Ah!"
    "Acordo assustada como som do despertador"
    "Hmmm..."
    "O relógio marca 6:30"
    "queria dormir só mais um pouquinho..."
    "Mas nossa presença foi solicitada no pátio às 8:30"
    "E faremos uma pequena performance durante a tarde."
    "É melhor eu começar a me preparar"
    "Não quero estragar tudo logo no primeiro dia."

    "Saindo para o corredor dou de cara com as outras"
    "Todas estavam saindo de seus quartos parecendo ter acordado agora também"
    "Exceto Linne."
    "Percebemos isso quando passamos pela cozinha"
    "Onde a encontro tomando o seu café da manhã graciosamente."
    l "Bom dia, garotas!"
    m "Bom dia."
    "Juni boceja alto."
    j "Bom diaah."
    n " 'Dia."
    "Roko apenas acena para nós a se dirige ao banheiro."
    "E as outras garotas continuam seus preparativos."
    "..."
    "Linne já está pronta."
    "Mas ainda há tempo até nosso compromisso..."

    menu(nvl=True):
        "Questionar Linne":
            m "Linne?? Que horas você levantou?"
            m "Parece estar acordada há horas!"
            l "Ah, que isso!"
            l "Nem estou de pé há tanto tempo."
            l "E eu também já estou acostumanda a acordar cedo."
            m "Nossa…"
            menu(nvl=True):                
                "Elogiar Linne pela sua atitude":
                    m "Você parece tão disposta, Linne"
                    m "Admiro que consiga acordar tão cedo e ainda estar com um sorrizo no rosto!"
                    l "Haha... Agora fiquei até sem graça"
                    l "Mas muito obrigada, Moon!"
                    "Ela está realmente contente."
                    $ linne += 1
                    l "Enfim... Não é melhor você se aprontar?"
                    m "Ah! Sim, é verdade!"
                    m "Nos encontramos mais tarde!"
                "Estranhar essa atitude":
                    m "Mas... Ainda há muito tempo até às 8."
                    m "Precisava mesmo estar pronta com tanta antecedencia?"
                    l "..." 
                    l "Não gosto de deixar as coisas pra última hora."
                    "Não sei se isso responde minha pergunta."
                    m "Bom... Vou voltar a me preparar."
                    m "Até mais!"

        "Continiar minhas tarefas"
            "Não acho que isso deve ser questionado..."

label cap1_2:
    "Dado 8:30, estávamos todas presentes no pátio."
    "O apresentador e a equipe de produção se preparava para a gravação."
    Sr "Começamos em alguns instantes!"
    Sr "E não se preocupem! Dessa vez não será ao vivo."
    "Mas... Essa demora está me deixando anciosa."
    "e observando bem, juni também está tensa."
    menu(nvl=True):
        "tentar acalmá-la":
            m "Hey, Juni"
            "Ela olha para mim confusa e surpresa."
            j "Ahn??"
            m "Calma. Você vai se sair bem"
            m "Acrdito no seu potencial!"
            j "Ah... T-tudo bem."
            "Seu olhar se desvia."
            j "..."
            $ ajuda_j = True
            $ juni += 1

        "Não fazer nada":
            "Também estou nervosa"
            "Então, talvez tentar ajudar tenha o efeito contrário."

    Sr "Começamos em 3..."
    Sr "2..."
    Sr "E..."
    Sr "Sejam muito bem vindos de volta ao reality Star's Selection!"
    Sr "Chegou o momento de esclarecermos alguns pontos do programa."
    Sr "Todos devem saber que em em realitys d sobrevivencia"
    Sr "Os participantes vão sendo declassificados ao decorrer dos testes."
    Sr "A pior das performances, infelizmente, terá que arrumar suas malas"
    Sr "E voltar para casa."
    Sr "As participantes também estão sujeitas ao julgamento do público"
    Sr "Pois, caso algum comportamento não os agrade..."
    Sr "Vocês poderam entrar em nosso site para exigir uma punição!"
    "Parando pra pensar... Isso é bem pesado."
    "E o Sr. Star ainda anuncia isso com um sorriso no rosto..."
    Sr "Agora, sobre os testes:"
    Sr "Eles serão aplicados periodicamente"
    Sr "E são fundamentais tanto para decidir quem sai,"
    Sr "Quanto para avalir as performances em geral e axaltar a melhor!"
    Sr "E, obviamente"
    Sr "Após o período de testes haverá um descanso para nossas pequenas estrelas."
    Sr "O espaço do reality possui o alojamento das garotas"
    Sr "Espaços de treinamento, como a sala de dança, estúdio e academia."
    Sr "E espaços de lazer, como a sala de estar, a área externa e a cozinha."
    Sr "Então, respondendo sua pergunta, senhorita Nádia"
    Sr "Vocês são livres para fazerem o que quiserem nesses espaços."
    n "Ah... Sim."
    Sr "Bom... Creio que esclareci tudo o que precisava."
    Sr "Alguma pergunta?"
    "..."
    Sr "Parece que não!"
    Sr "Então é isso!"
    Sr "Agora vocês acompanharão as participantes em suas atividades antes da performance"
    Sr "E ficarão sabendo mais sobre elas de pertinho!"
    Sr "Eu sou o Sr. Star, e você está acompanhando o reality Star's Selection!"
    "A gravação encerra."
    Sr "Muito bem, equipe!"
    Sr "Agora é com vocês."

    # aq as participantes sao entrevistadas em suas atividades
    # e acontece o primeiro minigame
label cap1_3:
    # apos o minigame, as personagens podem descançar
    "Ufa! Finalmente acabou!"
    "Estou livre para descansar."
    "???"
    "Escuto alguém se aproximar de mim."

    if reconh:
        j "Hey, Moon!"
        "Juni!!"

        if ajuda_j:
            j "Não tive oportunidade de te agradeçer naquela hora!"
            m "Agradecer por...?"
            j "P-por me apoiar hoje mais cedo!"
            j "Eu... não estava me sentindo muito bem naquele momento"
            j "E você também parecia nervosa..."
            "Ah! Ela notou!"
            j "Mas, mesmo assim você decidiu me ajudar!"
            
        j ""

