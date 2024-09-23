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
    "Todas estavam saindo de seus quartos parecendo ter acordado agora também."
    "Exceto Linne."
    "Percebemos isso quando passamos pela sala."
    "Onde a encontramos escrevendo algo em um caderninho."
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
        "Falar com Linne":
            m "Linne?? Que horas você levantou?"
            m "Parece estar acordada há horas."
            l "Ah, que isso!"
            l "Nem estou de pé há tanto tempo."
            l "E eu também já estou acostumanda a acordar cedo."
            m "Nossa..."
            menu(nvl=True):                
                "Quanta determinação":
                    m "Você parece tão disposta, Linne"
                    m "Admiro que consiga acordar tão cedo e ainda estar com um sorrizo no rosto!"
                    l "Haha... Agora fiquei até sem graça"
                    l "Mas muito obrigada, Moon!"
                    "Ela está realmente contente."
                    $ linne += 1
                    l "Enfim... Não é melhor você se aprontar?"
                    m "Ah! Sim, é verdade!"
                    m "Nos encontramos mais tarde!"
                "Ainda é muito cedo":
                    m "Mas... Ainda há muito tempo até às 8."
                    m "Precisava mesmo estar pronta com tanta antecedencia?"
                    l "Hmm" 
                    l "Não gosto de deixar as coisas pra última hora."
                    "Não sei se isso responde minha pergunta..."
                    m "Bom... Vou voltar a me preparar."
                    l "Até logo."

        "Continuar minhas tarefas":
            "Bom, é melhor eu me cuidar."
            l "Moonie?"
            "Linne chama meu nome assim que viro as costas."
            l "Te desejo boa sorte."

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
            "Talvez tentar ajudar tenha o efeito contrário."

    Sr "Começamos em 3..."
    Sr "2..."
    Sr "E..."
    Sr "Sejam muito bem vindos de volta ao reality Star's Selection!"
    Sr "Chegou o momento de esclarecermos alguns pontos do programa."
    Sr "Todos devem saber que em em realitys de sobrevivencia"
    Sr "Os participantes vão sendo declassificados ao decorrer dos testes."
    Sr "A pior das performances, infelizmente, será eliminada"
    Sr "E voltará para casa."
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
    Sr "Parece que não."
    Sr "Então é isso!"
    Sr "Agora vocês acompanharão as participantes em suas atividades antes da performance"
    Sr "E ficarão sabendo mais sobre elas de pertinho."
    Sr "Ah, e não se esqueçam que hoje à noite teremos um grande evento!"
    Sr "Eu sou o Sr. Star, e você está acompanhando o reality Star's Selection!"
    "A gravação encerra."
    Sr "Muito bem, equipe."
    Sr "Agora, senhoritas"
    Sr "Vocês serão acompanhadas individualmente em suas atividades de treino."
    Sr "Espero que estejam preparadas."
    Sr "Estão dispensadas!"

    "Cada uma se dirige à uma área de treino diferente."
    "Hmmm..."
    "Melhor eu treinar dança."
    # espaco p primeiro minigame
    "Durante meu treinamento, tento não ficar nervosa com as câmeras que me acompanham."
    "Após um longo período, finalmente encerramos as gravações."

label cap1_3:
    # apos o treino, as personagens podem descançar
    "Ufa! Finalmente acabou!"
    "Estou livre para descansar."
    "Pelo menos até o evento."
    "???"
    "Escuto alguém se aproximar de mim."

    if reconh:
        j "Hey, Moon!"
        "É a Juni."

        if ajuda_j:
            j "Não tive oportunidade de te agradeçer naquela hora."
            m "Agradecer por...?"
            j "P-por me apoiar hoje mais cedo."
            j "E sabe..."
            j "Você também parecia nervosa."
            #"Ah, Ela notou"
            j "E-então... Quero que saiba que está se saindo bem!"
            #menu de possiveis respostas
            #menu(nvl=True):

            #Apos o termino desse assunto    
            j "Ah! Mais uma coisinha..."      
        j "Uhh..."
        j "Naquele hora, no dia da primeira apresentação"
        j "O que você disse algo sobre ser alguém importante..."
        j "Achei interessante..."
        "Ela olha no fundo dos meus olhos."
        menu(nvl=True):
            "...":
                m "..."
                "Nos encaramos por um tempo."           
                j "..."
                "Constrangida, ela desvia olhar."
                j "Enfim... Era só isso que queria dizer."
                $ juni -= 1

            "É mesmo?":
                m "Oh!"
                m "você achou mesmo?"
                j "... Ahan."
                "Ela finalmente desvia os olhos."
                m "Isso é ótimo!"
                m "Obrigada, você é muito gentil."
                j "Ah, imagina."
                j "Bem..."

            "O que quer dizer?":
                m "Interessante? Como?"
                j "..."
                "Ela continua me encarando."
                "Isso é estranho."
                m "Por que está me olhando assim?..."
                "Ela percebe que estava me encarando."
                j "Ah, meu Deus!"
                j "Eu n-não percebi que estava de deixando nervosa."
                j "Nossa, me desculpa mesmo."
                if ajuda_j:
                    m "Não precisa se desculpar."
                    m "Eu entendo."
                    $ juni += 1
                j "É só que... Foi muito legal o que disse."
                j "Então queria saber se realmente..."
                m "Sim?"
                j "Hmm... Bem..."
                "Ela reflete por um momento."
                j "Ah... Deixa pra lá." 

        j "Acho que precisamos ir andando agora."
        j "Afinal, temos um evento para protagonizar."
        j "Hehe.."
        j "T-te vejo mais tarde."
        "Ela se vira para "
        m "Foi um prazer!"

    else:
        r ""
