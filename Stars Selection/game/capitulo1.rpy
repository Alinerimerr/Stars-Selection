label cap1_1:

    #hide daydisplay

    $ dia += 1
    $ periodo = "Manhã"


    D "[dia]"


    show daydisplay


    "TRRIN TRRIN TRRIN TRRIN TRRIN TRRIN"
    m "Ah!"
    "Acordo assustada como som do despertador"
    m "Hmmm..."
    "O relógio marca 6:30"
    m "Queria dormir só mais um pouquinho..."
    "Mas nossa presença foi solicitada no pátio às 8:30"
    "É melhor eu começar a me preparar"
    "Não quero estragar tudo logo no primeiro dia."

    "Saindo para o corredor dou de cara com as outras."
    "Todas estavam saindo de seus quartos parecendo ter acordado agora também."
    "Exceto Linne."
    "Percebemos isso quando passamos pela sala, onde a encontramos escrevendo algo em um caderninho."
    l "Bom dia, garotas!"
    m "Bom dia."
    "Juni boceja alto."
    j "Bom dia."
    n " 'Dia."
    "Roko apenas se dirige ao banheiro."
    "E as outras garotas continuam seus preparativos."
    l "Algum problema, Moon? Você está com uma cara horrível."
    m "N-Não... Nenhum problema..."
    m "É só que... Eu tenho problemas em acordar cedo."
    l "Entendi. O despertador deve ser o seu maior inimigo, né? hi hi."
    m "Heh... Sim, sim."
    "Gostaria que isso não fosse verdade..."

    menu(nvl=True):
        "Falar com Linne":
            m "Linne, que horas você levantou?"
            m "Parece estar acordada há horas."
            l "Ah, não... Nem estou de pé há tanto tempo."
            l "E também já estou acostumada a acordar cedo."
            m "Nossa..."
            menu(nvl=True):                
                "Quanta determinação":
                    m "Você parece tão disposta, Linne."
                    m "Admiro que consiga acordar tão cedo e ainda estar com um sorriso no rosto."
                    l "Muito obrigada, Moon... Nossa, fiquei até sem graça."
                    "Ela está realmente contente."
                    $ linne += 1
                    l "Enfim... Não é melhor você se aprontar?"
                    m "Ah! Sim, é verdade!"
                    m "Nos encontramos mais tarde!"
                "Ainda é muito cedo":
                    m "Mas... Ainda há muito tempo até às 8:00."
                    m "Precisava mesmo estar pronta com tanta antecedência?"
                    l "Hmm..."
                    l "Não gosto de deixar as coisas pra última hora."
                    "Não sei se isso responde minha pergunta..."

        "Continuar minhas tarefas":
            m "Bom, é melhor me apressar..."
            l "Ah, claro."
            l "Boa sorte hoje."
    #jump end

label cap1_2:
    $ periodo = "Manhã"
    $ atividade = "Entrevista"
    #transicao foda
    Sr "Começamos em alguns instantes!"
    Sr "E não se preocupem! Dessa vez não será ao vivo."
    "..."
    "Essa demora está me deixando ansiosa."
    "E observando bem... Juni também está tensa."
    menu(nvl=True):
        "tentar acalmá-la":
            m "Ei, Juni!"
            #"Ela olha para mim confusa e surpresa."
            j "Ahn??"
            m "Não precisa ficar assim... Sei que vai se sair bem!"
            j "Ah... T-tudo bem."
            j "..."
            $ ajuda_j = True
            $ juni += 1

        "Não fazer nada":
            "..."

    Sr "Começamos em 3..."
    Sr "2..."
    Sr "E..."
    Sr "Sejam muito bem vindos de volta ao reality Star's Selection!"
    Sr "Chegou o momento de esclarecermos alguns pontos do programa."
    Sr "Todos devem saber que em em realitys de sobrevivência"
    Sr "Os participantes vão sendo declassificados ao decorrer dos testes."
    Sr "A pior das performances, infelizmente, será eliminada"
    Sr "E voltará para casa."
    Sr "As participantes também estão sujeitas ao julgamento do público"
    Sr "Pois, caso algum comportamento não os agrade..."
    Sr "Vocês poderão entrar em nosso site para exigir uma punição!"
    "Parando pra pensar... Isso é bem pesado."
    "E ele ainda anuncia isso com um sorriso no rosto..."
    Sr "Agora, sobre os testes:"
    Sr "Eles serão aplicados periodicamente."
    Sr "São fundamentais para decidir quem sai..."
    Sr "E para avaliar as performances em geral e exaltar a melhor!"
    Sr "E, obviamente..."
    Sr "Após o período de testes haverá um descanso para nossas pequenas estrelas."
    Sr "O espaço do reality possui o alojamento das garotas"
    Sr "Espaços de treinamento, como a sala de dança, estúdio e academia."
    Sr "E espaços de lazer, como a sala de estar, a área externa e a cozinha."
    Sr "Então, respondendo sua pergunta, senhorita Nádia"
    Sr "Vocês são livres para fazerem o que quiserem nesses espaços."
    n "Ah..."
    Sr "Bom... Creio que esclareci tudo o que precisava."
    Sr "Agora vocês acompanharão as participantes em suas atividades antes da performance"
    Sr "E ficarão sabendo mais sobre elas de pertinho!"
    Sr "Ah, e não se esqueçam que hoje à noite teremos um grande evento!"
    Sr "Eu sou o Sr. Star, e você está acompanhando o reality Star's Selection!"
    "A gravação encerra."
    Sr "Muito bem, equipe!"
    Sr "Agora, senhoritas..."
    Sr "Vocês serão entrevistadas individualmente em suas atividades de treino."
    Sr "Espero que estejam preparadas."


    # entrevista particular
    "Vejo muitas cameras aponatadas para mim e o sr.Star."
    "Ele fala animadamente com uma delas."
    Sr "Finalmente, chegou a vez de Moonie falar um pouco sobre si."
    Sr "Adimito que estava bem animado para ouvir mais sobre você, querida."
    m "Hã? Quer dizer... Muito obrigada Sr.Star."
    "Será que é só um modo de falar... Ou ele realmente acha isso?"
    Sr "Gostaria de compartilhar sua rotina?"
    m "C-claro!"
    m "Logo de manhã eu faço minha skincare e tomo meu café da manhã-"
    Sr "Ahh, sim, sim! Não deve ser fácil manter esse rostinho bonito, não é mesmo?"
    "E mais uma vez, ele me interrompe."
    "Parece que vou ter que me acostumar..."
    Sr "Oh, me perdoe senhorita."
    Sr "Por favor continue, querida."
    m "Bem... ainda na parte da manhã eu faço pilates e treino canto."
    m "Já no início da tarde eu almoço e, logo após, tiro uns 30 minutos para mim."
    m "Treino dança e fortaleço minha resistência no restante da tarde."
    m "Ah, eu também gosto muito de tomar um chá da tarde quando sinto fome..."
    m "Enfim, durante a noite faço novamente minha skincare, cuido do meu cabelo e unhas."
    m "Janto e me preaparo para dormir."
    Sr "*bosejo*"
    # ele é mt bom em destrir a moral das participantes
    Sr "Bem, não vi nada de mais... Existem rotinas melhores por aí..."
    Sr "Por um momento, eu esperei algo mais interesante."
    "C-Como assim ele esperava mais? Isso já não é o suficiente?"
    Sr "Mas quem sou eu para julgar, não é?"
    Sr "Agora, me deixe perguntar o que todos querem saber..."
    Sr "Qual é..."
    Sr "O seu segredo?"
    m "S-Segredo... ?"
    Sr "Como faz para ter essa pele de porcelana?"
    Sr "E esse cabelo Impecável? Ou esse corpão violão?"
    m "Hmmm... N-não sei..."
    Sr "Ora, deixe de suspense, querida. Diga logo!"
    Sr "O público precisa saber!"
    m "A-Acho que não faço nada de mais..."
    Sr "Nem um procedimento estético? Ou produtos milagrosos?"
    m "O que? Nada disso."
    Sr "..."
    m "Hmm... P-Perdão se eu disse alguma cois-"
    Sr "Ha ha! Isso é ótimo!"
    Sr "Saiba que, mesmo tendo essa personalidade beeem sem sal ao meu ver..."
    Sr "Todo mundo adora um rostinho bonito!"
    "S-Sem sal?!"
    Sr "Eu APOSTO que vai se dar bem no programa!"
    Sr "Era só isso mesmo que tinha para conversar com você, querida."
    Sr "Muito obrigado e boa sorte com os seus treinos."
    Sr "E não se atrase para o evento de hoje à noite, viu?"
    Sr "Está dispensada."
    "Ainda não posso acreditar que ele me chamou de sem sal..."
    "Será que todo mundo pensa assim?"


label cap1_3:


    $ periodo = "Tarde"
    "Hora do almoço."
    "Finalmente. Estou morreeendo de fome."


    if reconhecimento:
        "???"
        "Escuto alguém se aproximar de mim."
        j "Ei, Moon!"
        "É a Juni."


        if ajuda_j:
            j "Não tive oportunidade d-de te agradecer naquela hora."
            m "Agradecer por...?"
            j "Por me apoiar hoje mais cedo."
            j "E sabe..."
            j "Você também parecia nervosa."
            j "E-então... Quero que saiba que está se saindo bem!"  
            j "Ah! Mais uma coisinha..."      
        j "Hm..."
        j "Naquele hora, no dia da primeira apresentação"
        j "O que você disse algo sobre ser alguém importante..."
        j "Achei interessante..."


        menu(nvl=True):
            "...":
                m "..."
                "Nos encaramos por um tempo."          
                j "..."
                j "Enfim... Era só isso que queria dizer."
                $ juni -= 1


            "É mesmo?":
                m "Oh!"
                m "você achou mesmo?"
                j "... Ahan."
                m "Isso é ótimo!"
                m "Obrigada, você é muito gentil."
                j "Ah, imagina."
                j "Bem..."


            "O que quer dizer?":
                m "Interessante? Como?"
                j "..."
                "Ela tá me deixand nervosa..."
                m "Por que está me olhando assim?..."
                "Ela percebe que estava me encarando."
                j "Ah, meu Deus!"
                j "Eu n-não percebi que estava te deixando nervosa."
                j "Nossa, me desculpa..."
                j "É só que... Foi muito legal o que disse."
                j "Então queria saber se realmente..."
                m "Sim?"
                j "Hmm... Bem..."
                "Ela reflete por um momento."
                j "Ah... Deixa pra lá."


        j "Acho que precisamos ir, agora..."
        j "Afinal, temos um evento p-para protagonizar mais tarde."
        j "He he..."
        j "Err... T-Tchau."
        "Ela se vira rapidamente e vai embora."
        m "Foi um prazer!"
        "Acho que ela nem escutou..."
        "Caramba... Não achei que fosse encontrar uma pessoa tão ansiosa quanto eu..."
        "Talvez eu converse melhor com ela depois."
        "Agora, eu tenho que comer algo antes que eu desmaie."


    # hr do almoço
    "Chegando no refeitório, encontro Linne almoçando."
    l "Olá, Moon."
    l "Você viu o restante das meninas?"
    m "Não. Só vi a Juni..."
    m "Cadê ela, afinal?"
    j "E-Estou aqui."
    "Não tinha reparado nela bem atrás de mim."
    l "Venham. Juntem-se à mesa."
    "Nos juntamos a ela na mesa para almoçar."
    l "O que acharam da entrevista, meninas?"
    j "Acho q-que não foi nada de mais..."
    l "Não precisa ser tímida. Pode falar."
    j "..."
    l "Bem, já que é assim..."
    l "O que achou Moon?"
    menu(nvl=True):
        "Foi bom.":
            m "Apesar de algumas coisinhas... Acredito que ocorreu tudo muito bem."
            l "Ah... Eh, isso é bom."
            l "Não é todo mundo que consegue se manter otimista nessas horas."
            jump cap1_al


        "Foi péssimo.":
            m "Não sei..."
            m "Talvez o Sr.Star tenha uma péssima impressão sobre mim."
            l "Poxa, que chato..."
            l "Mas... Tenho a impressão de que você está sendo pessimista, Moon."
            jump cap1_al




        "Tanto faz.":
            m "Na verdade, não tenho nada a comentar."
            l "Nada? Nenhuma impressão ou opinião?"
            m "Err... Não."
            l "... Então, tá."
            l "Já que vocês não querem conversar comigo... Eu vou me retirar."
            "Ela se levanta de maneira dramática."
            l "Até logo."
            "Será que ela ficou magoada? Mas essa não era minha intenção..."
            "Eu só queria comer meu almoço em paz."
            j "..."
            "Juni também não parece querer conversar agora"
            "Termino meu almoço sem trocar uma palavra com Juni."
            jump cap1_4




label cap1_al:
    l "Tente tomar cuidado... Esse pensamento pode te arruinar um dia, sabia?"
    m "É mesmo? por que?"
    # tentativa de linne de diminuir moon e exaexaltar a si mesma
    l "Você ainda é muito iniciante e não tem experiência suficiente para julgar algumas coisas, ora!"
    l "Por isso você corre o risco de passar por muitos micos! acredite em mim!"
    j "M-Micos?!"
    m "Nunca tinha pensado nisso..."
    l "Melhor vocês começarem a se preocupar sobre. Já que isso envolve suas imagens."
    j "Uhg... Não gosto nem de pensar..."
    # potencializa uma insegurança das duas
    l "Eu tenho alguma experiência na área e acreditem, eu já notei vários comportamentos problemáticos em vocês."
    l "Hihi! Chega até a ser meio engraçado."
    "Ela se levanta da mesa graciosamente."
    l "Preciso ir agora, meninas."
    # mesmo se esse dialogo n acontecer, juni vai procurar por "ajuda" da linne
    l "Mas se quiserem conversar mais sobre o assunto alguma hora, estarei disposta a ajudar."
    l "Até logo!"
    "Linne sai."
    j "... M-Moon?"
    j "Acha mesmo q-que eu t-tenho... Co-comportamentos problemáticos?"
    "Juni tenta disfarçar sua tremedeira sem sucesso."
    "Confesso que isso me pegou desprevenida... Não achei que estava indo tão mal..."
    m "..."
    j "Não estou mais com fome..."
    "Ela sai correndo, deixando metade de um prato de salada para trás."




label cap1_4:
    # dps dos treinos da tarde
    $ atividade = "Depois dos treinos"


    "Resolvi dar uma olhada no jardim depois dos meus treinos da tarde."
    "Enquanto passava pelo jardim, encontrei Roko observando as flores."
    "Seria uma boa ideia conversar com ela?"
    menu(nvl=True):
        "Sim":
            "Me aproximo para conversar com ela."
            m "Olá, Roko!"
            r "AAAH!"
            r "Pelos céus! Você me assustou!"
            r "Onde estão seus modos??!"
            m "Ah, me desculpa."
            m "Não foi minha intenção..."
            r "Hump!"
            r "O que quer comigo, afinal?"
            m "Eh..."
            m "Só queria perguntar como foi a sua performance..."
            r "Ah, sobre isso..."
            r "Foi ótima, se quer saber a minha opinião."
            r "Parece até que nasci pra isso."
            m "Caramba!"
            m "Fiquei sem palavras diante de tanta confiança."
            r "Isso acontece com os menos afortunados, de fato."
            "Bem humilde..."
            r "É como eu sempre digo:"
            r "Para se tornar uma verdadeira estrela"
            r "Primeiro você deve acreditar que já é!"
            r "Afinal, é a minha opinião que importa."
            "Ela estufa o peito e empina o nariz."
            menu(nvl=True):
                "Não é bem assim que funciona.":
                    m "Entendo que autoconfiança é importante..."
                    m "Mas, não acho que seja bom ter em excesso."
                    r "Como?"
                    m "Sabe... Você pode acabar perdendo a noção da realidade..."
                    m "E prejudicando tanto a si mesma quanto os outros a sua volta."
                    r "Prejudicando?"
                    r "Não, não... Você entendeu errado."
                    r "Ahf... Não vou discutir."
                    r "Você não entenderia de qualquer forma..."
                    "Acho que VOCÊ não entenderia de qualquer forma."




                "Tem razão.":
                    m "Faz sentido..."
                    m "Acho que tem razão!"
                    r "Tenho, sim!"
                    r "Viu? Foi assim que te convenci."
                    r "Se você acredita em algo fielmente"
                    r "As outras pessoas vão acreditar também!"
                    "UAU!"
                    $ roko += 3
   
            # termino do assunto
            r "..."
            m "..."
            "Observamos o jardim em silêncio por um tempo."
            r "É um belo jardim."
            m "Sim..."
            r "Ele me lembra de casa..."
            r "Claro que o de lá é bem maior."
            r "E mais bonito também."
            r "Mas isso é por conta do nosso jardineiro."
            r "Um senhor de idade muito calado..."
            r "As vezes, eu costumo sentar em um dos bancos..."
            r "E conversar com ele enquanto trabalha."
            r "Ele quase nunca me responde."
            r "Mas eu sei que ele me escuta com atenção."
            r "..."
            r "Um dia, quando eu era menor, ele me perguntou o motivo de minhas visitas constantes."
            r "Então eu respondi que todos os meus amigos estavam viajando com os pais."
            r "Enquanto os meus estavam sempre bem ocupados."
            m "Poxa..."
            r "Ele também reagiu da mesma forma."
            r "Bem..."
            r "Mais tarde, ele me trouxe uma cesta cheia de tomates que ele mesmo tinha cultivado."
            r "Sugeriu convidarmos a chef"
            r "Para que nos ajudasse a preparar alguns lanches com eles."
            r "Eu não gostei da ideia no início, pois não como nada com a cor vermelha."
            m "Nada com a cor vermelha? Por que?"
            r "Porque eu acho muito nojento!"
            r "Mas... Naquele momento eu pensei:"
            r "Por que não?"
            r "Aí nós três nos juntamos"
            r "E seguindo as ordens da nossa chef, fizemos sanduíches para o café da tarde."
            r "Cheguei até a me divertir no processo."
            r "Então, na hora de provar eu tive certeza..."
            r "De que definitivamente ODEIO comidas vermelhas!"
            $ vermelho = True
            "O QUEEE!!?"
            r "Fiquei tão frustrada! Joguei o sanduíche de volta no prato e subi chorando para meu quarto."
            r "Eca! só de lembrar daquele gosto horrível na minha boca..."
            "Ela cobre a boca como se estivesse prestes a vomitar."
            r "..."
            r "Pensando agora..."
            # Inventar nome pro veio (Helian)
            r "O sr. Helian deve ter ficado deveras decepcionado..."
            menu(nvl=True):
                "E com razão!":
                    m "Com certeza!"
                    m "Isso foi péssimo da sua parte!"
                    r "E você queria que eu fizesse o que?"
                    r "Fingir que gostei!?"
                    m "Não! Mas você poderia pelo menos agradecer."
                    m "Era literalmente o mínimo!"
                    "Ela bufa, irritada."
                    r "Urhg! Você é muito ignorante!"
                    r "Você e aquela Nádia!"
                    m "O que?!"
                    m "Quer saber? Eu tenho mais o que fazer!"
                    "Me afasto sem olhar pra trás."
                    "Tenho que voltar a treinar..."
                    jump cap1_5
                    $ ignorante = True








                "Talvez...":
                    m "Olha..."
                    m "Talvez o que importasse, no final, não era o sabor do sanduíche."
                    m "Mas sim a experiência do processo!"
                    m "Você mesma disse que não tinha gostado da ideia."
                    m "E mesmo assim aceitou participar."
                    m "Tenho certeza de que ele deve ter ficado contente por isso."
                    r "Acha isso mesmo...?"
                    r "Bem... Deve estar certa..."
                    r "Afinal, você se parece bastante com ele."
                    $ roko += 5
                    "Ah, nossa!"
                    "Me sinto até meio especial!"
                    "Pelo menos... pra Roko."
                    # reacao de moon(n sei o que colocar ainda)




                    # termino do assunto e convite pra treinar
                    m "Ah, não! Devo estar atrasada pro treino!"
                    r "Treino? Mas já não treinamos hoje cedo?"
                    m "Hmm... sim..."
                    m "Mas nós precisamos treinar... mais!"
                    r "Oh..."
                    "Roko está em choque."
                    "Ela não sabia que nós treinamos o dia todo?"
                    menu(nvl=True):
                        "Convidar Roko para treinar":
                            m "Se quiser pode vir comigo..."
                            r "Não, não... eu já atingi meu limite hoje e não quero cansar minha beleza."
                            r "Que tal... amanhã? De manhãzinha?"
                            m "Claro! Costumo fazer pilates de manhã."
                            m "Pode me encontrar na academia."
                            $ treino_roko = True
                            r ""








                        "Não convidar Roko para treinar":
                            m "Err... preciso muito ir agora..."
                            r "Ah, sim..."
                            r "Desejo boa sorte."




                    # encerramento do dialogo


        "Não":
            "Melhor não... Tenho que me preparar pro evento..."
           
    $ atividade = "Preparação do evento"
    "Dou uma última olhadinha no espelho e..."
    "É isso, estou pronta."
    "Espero que eu não estrague tudo ou..."
    l "Moonie? Cadê você? Vai acabar se atrasando!"
    m "Hã? J-Já tô indo!"




label cap1_5:
    # inicio do evento
    # Determinar local do acontecimento(fiquei em duvida)
    $ periodo = "Noite"
    $ atividade = "Evento ao vivo"




    "Ao chegarmos ao local"
    "Observamos que estão dispostas mesas, utensílios de cozinha e vários ingredientes."
    "Confusas, nós todas nos entreolhamos."
    Sr "Boas vindas, meninas!"
    Sr "Espero que tenham aproveitado o dia."
    l "Ah, nós aproveitamos sim!"
    l "Mas... Se me permite a pergunta..."
    l "O que está havendo aqui?"
    Sr "Ora! Não tenha pressa!"
    Sr "Vocês descobrirão em breve..."
    "Ele se diverte fazendo suspense."
    j "Uhg... Isso não parece bom..."
    Sr "Não se preocupem."
    Sr "Será divertido, eu garanto!"
    r "Divertido...?"
    Sr "Vamos ao ar em alguns instantes!"      
    l "Estejam preparadas, garotas."
    "Linne ajeita a postura e muda a sua expressão para algo mais confiante."








    Sr "Começamos em 3..."
    Sr "2..."
    Sr "1..."
    Sr "{i}Muito boa noite a todos!{/i}"
    Sr "Está começando agora o nosso primeiro grande evento ao vivo do reality Star's Selection!"
    Sr "E hoje, senhoras e senhores..."
    Sr "Organizamos um desafio diferenciado para nossas pequenas estrelas."
    Sr "As quais ainda não fazem ideia do que está por vir."
    Sr "He he he"
    "Algo não cheira bem aqui..."
    Sr "Muito bem! Estão prontas?"
    Sr "O desafio de hoje será..."
    Sr "Uma competição gastronômica!"
    n "Uma... O que?"
    Sr "É isso mesmo!"
    Sr "Serão sorteados dois grupos de duas pessoas"
    Sr "O resultado aparecerá no telão logo atrás de nós."
    Sr "Quem ficar de fora será a jurada."
    Sr "A equipe que preparar o melhor prato ao gosto da jurada"
    Sr "Sairá vitoriosa!"
    Sr "Alguma pergunta?"
    r "Teremos alguma recompensa por vencer?"
    Sr "Não, senhorita!"
    Sr "Este evento foi planejado para ser divertido e casual."
    Sr "Por isso não haverá recompensas."
    Sr "No entanto, pode haver punições a equipe que tentar trapacear ou sabotar a competição."
    Sr "Algo mais?"
    l "A jurada será uma de nós?"
    Sr "Sim, senhorita!"
    l "Então... Como podemos garantir que ela será imparcial?"
    Sr "Bom, acho que devo lembrar as senhoritas:"
    Sr "Tudo o que fazem neste reality está sujeito ao julgamento do público."
    Sr "Caso identifiquem algum comportamento suspeito..."
    Sr "Tenho certeza que eles não terão misericórdia."
    Sr "Mais alguma pergunta?"
    Sr "Não?"
    Sr "Nesse caso, que comece o sorteio das equipes!"
    Sr "A equipe 1 será composta por..."
    "No telão, aparece meu nome e o de Nádia."
    Sr "Ah, Moonie e Nádia! Uma dupla promissora!"
    Sr "Podem se dirigir a área de preparo."
    Sr "E não se esqueçam de vestir seus aventais!"
    "Fazemos o que nos é solicitado rapidamente."
    "Enquanto vestimos nossos aventais, Nádia quebra o silêncio."








    n "Que situação 'curiosa', não?"








    menu(nvl=True):
        "Curiosa?":
            m "Hmm? O que quer dizer?"
            n  "..."
            n "Você é bem lentinha, não?"
            "Ela suspira em desaprovação."
            m "Oh..."
            m "Me desculpa?"
        "Realmente...":
            m " É realmente bem 'curiosa' mesmo."
            n "Ah, você também percebeu?"
            m "É claro!"
            m "Eles nem disfarçaram."
            n "Aposto que isso saiu direto do Sr.Star..."
            n "É melhor a gente ficar ligada."








    "Outros dois nomes aparecem no telão."
    Sr "A equipe 2 será composta por Juni e Linne!"
    Sr "Uma equipe adorável, não é mesmo?"  
    Sr "Ha ha!"
    Sr "Pode se preparar, equipe 2!."
    Sr "Bom... Parece que temos uma jurada!"
    Sr "Senhorita Roko!"
    "Nádia sussurra sarcasticamente."
    n "Nossah, mas que surpresa."
    r "E-eu??"
    r "Não, não. Deve haver algum engano!"
    Sr "Não há enganos neste reality, querida!"
    Sr "Pode ficar tranquila."
    "Ele diz isso com um sorriso irônico no rosto, expressando exatamente o oposto."
    Sr "Roko escolherá um prato e as equipes terão 45 minutos para prepará-la."
    Sr "Ah, e não haverá acréscimo de tempo."
    Sr "jurada Roko! Qual será o prato desta noite?"
    r "Hãh..."
    "Consigo ver desespero e angústia nos olhos dela."
    Sr "Sim?"
    r "Que tal..."
    "Finalmente acende uma lâmpada na cabeça dela."
    r "Espaguete!"
    Sr "Espaguete?"
    r "Isso!"
    r "Mas sem-"
    Sr "É isso! Grupos 1 e 2 terão 45 minutos para preparar um prato de Espaguete!"
    r "Espera, não acabei de falar-"
    Sr "Começando exatamente agora!"
    "O tempo em minutos aparece no telão."
    Sr "Uma boa sorte para vocês!"
    n "Pelo menos ela não escolheu um daqueles pratos chiques e complicados..."
    n "Alguma sugestão do que fazer?"








    if(vermelho):
        m "Não exatamente..."
        m "Mas eu sei que ela não gosta de coisas vermelhas."
        n "Ela o que!?"
        m "Não gosta d-"
        n "Espera, eu ouvi da primeira vez."
        n "Tipo, como assim ela 'não gosta de coisas vermelhas'?"
        n "Palhaçada isso!"
        "Nádia está completamente indignada."
    else:
        m "Não tenho nem ideia."
        n "Ótimo..."
        n "Vamos fazer o tradicional espaguete com almôndegas e molho de tomate."
        n "Não tem como errar nisso."
        "Ao buscarmos pelos ingredientes"
        "Notamos que não há mais tomates nem almôndegas."
        n "Elas pegaram tudo!"
        m "Acho que chegamos tarde."
        n "Urhg!"
        m "Calma, vamos fazer outra coisa."
        "Ela respira fundo e se acalma."


    n "Nesse caso..."
    n "Podemos preparar um espaguete ao molho branco."
    n "Você prepara a massa enquanto eu faço o molho."
    m "Pode ser!"


    n "Temos disponíveis aqui:"
    n "Massas dos tipos tradicional e linguine..."
    m "Linguine é um macarrão?! Pensei que fosse aquele moço do Ratatouille..."
    n "..."
    n "Meio que é isso também... Mas na verdade esse é aquele macarrão mais achatado, sabe?"
    n "Temos aqui também os queijos parmesão, gorgonzola e mussarela..."
    n "E de proteínas temos frango, salmão e bacon."
    n "Qual massa você acha uma boa?"


    "Nádia espera por uma resposta."
    $ time = 5
    $ timer_range = 5
    $ timer_range = 'escolha_devagar'


    menu:
        "Tradicional":
            m "Eu gosto do tradicional."
            n "Ok..."
        "Linguine":
            m "O Linguine parece interessante."
            n "Ce escolheu esse por causa do desenho do rato, né?"
            menu(nvl=True):
                "Não...":
                    m "Não, não! Eu nunca faria uma coisa desas!"
                    n "Sei..."
                "Talvez...":
                    m "Hmm... Talvez..."
                    n "Meu irmãozinho de 10 anos teria respondido a mesma coisa."
                    m "Ei!"
   
    n "E o queijo?"
label escolha_devagar:
   
    "Coletamos os ingredientes e materiais e começamos a trabalhar."
    "Enquanto espero o macarrão cozinhar, observo Nádia fazer sua parte."
    "Ela é rápida e confiante em seus movimentos."
    "Chega até a cantarolar uma música."
    m "Você parece bem confortável."
    n "Ah! Eu?"
    n "É que na verdade já estou acostumada, sabe."
    n "Minha família tem um restaurante"
    n "E eu costumava ajudar na cozinha."
    m "É sério!? Caramba, que legal!"
    n "Na verdade, não era tão legal assim."
    n "Tinha muito problema e dor de cabeça..."
    n "Ainda tem, no caso…"
    n "Com o tempo as coisas pioraram por causa do dinheiro."
    m "Ah..."

    if ignorante:
        n "Bem que eu poderia ter nascido bem rica pra não ter que passar por esse tipo de coisa..."
        n "Tipo aquela metida da Roko. O maior dos problemas dela deve ser decidir em que continente vai passar as férias."
        n "Eu odeio ela... Sempre me olha com aquela cara de nojo."
        m "Ela te olha com nojo? Que horror!"
        n "Não me conformo que uma pessoa dessas já tenha ganhado na vida só por ser herdeira."
        # olha a fofoca
        m "Hoje mais cedo, eu estava conversando com ela."
        m "Você não vai acreditar no que ela disse..."
        n "O que ela disse? Vai, fala logo!"
        m "Ela chamou a gente de ignorante!"
        n "*surpresa* Não acredito!"
        n "Nossa, se eu ver ela na rua..."
        "Nádia está com MUITA raiva."
        n "Seria suspeito se, acidentalmente, colocassemos um 'pouco' de pimenta no prato dela?"
        m "Acho que sim..."
        m "Vamos deixar essa vingança pra depois."

    "O tempo passou enquanto preparavamos a comida."
    n "Hmm... Acho que vou adicionar alguns brócolis."
    n "Tô achando a receita meio sem graça."
    Sr "O tempo está se esgotando, meninas!"
    m "Vamos ter que nos apressar."


label cap1_6:
    # entrega dos pratos
    Sr "Tempo esgotado!"
    Sr "Equipe 1, apresentem seus pratos por gentileza."
    "Levamos nosso prato ao balcão de Roko."
    #Sr "Começando por Moonie e Nádia."
    Sr "O que prepararam?"
    m "Fizemos um delicioso espaguete ao molho branco."
    n "Com brócolis."
    "Roko se esforça para não fazer cara de nojo mais uma vez."
    Sr "Pode provar, jurada."
    "Ela empurra os brócolis para um canto do prato com o garfo."
    "E prova a massa com molho."
    r "Hmm..."
    r "Até que não está ruim..."
    r "Eu daria um 8..."
    Sr "8 é uma boa nota!"
    r "Mas como tem brócolis a minha nota final é 5!"
    Sr "!!!"
    "Ah não, não pode ser..."
    "Como ela tem a audácia!?"
    "Olho para o lado e vejo Nádia com uma expressão vazia."
    "Mas sinto o ódio crescente nela."
    Sr "Ehr..."
    "Até mesmo o Sr.Star parece indignado."
    Sr "Neste caso... 5 é a nota final!"
    Sr "He he..."
    "Ele ri meio sem graça."
    Sr "Podem ir, meninas. Vocês fizeram um ótimo trabalho!"
    Sr "Equipe 2, por favor, apresente-se!"
    "As meninas da equipe 2 dispõem seu prato sobre o balcão de Roko."
    "Roko arregala os olhos ao observar o macarrão coberto de molho de tomate."


    if (vermelho):
        "Nádia sussurra ao meu lado."
        n "Parece que a Carminha Frufru se deu mal..."
       
    Sr "Uhh! Parece muito bom!"
    Sr "Podem dizer do que se trata?"
    l "Temos aqui o clássico e muito amado espaguete com almôndegas."
    r "E... molho de tomate...?"
    j "Sim! Foi temperado com um ingrediente secreto especial meu!"
    "Juni parece orgulhosa sobre isso."


    if (vermelho):
        "Mal ela sabe..."


    r "... Tenho mesmo que comer isso?"
    Sr "Para dar uma nota, você precisa primeiro provar."
    r "Ok..."
    "Ela hesita em provar por algum tempo."
    Sr "Apresse-se! O prato vai esfriar!"
    "Depois de muito esforço mental, ela leva o garfo à boca."
    r "..."
    "Ela mastiga devagar..."
    Sr "Está tudo bem, srta. Roko...?"
    r "..."
    "Ela continua mastigando."
    "Seu rosto começa a suar e empalidecer."
    "Ela parece prestes a vomitar ou desmaiar."
    Sr "Meu Deus, há algo errado!"
    "As meninas da equipe 2 também parecem nervosas."
    l "Oh, não! O que houve?!"
    n "Meninas, quando eu falei de envenenar ela, eu estava BRIN-CAN-DO, tá bem?"
    "Nádia se diverte com a situação."
    Sr "Equipe médica, por favor!"
    "Sr.Star acena para chamar os primeiros socorros."
    "Nesse momento, Roko finalmente consegue engolir."
    r "Arhg!"
    r "Não precisa, eu estou bem..."
    Sr "Ufa!"
    "Todos parecem bem mais aliviados."
    Sr "A senhorita realmente nos preocupou..."
    Sr "Gostaria de uma pausa para respirar, srta. Roko?"
    r "Não, não."
    r "Isso já foi o suficiente para minha decisão final."
    "O clima se torna mais tenso após suas palavras."
    Sr "Bem... Então..."
    Sr "Diga-nos a sua escolha!"
    r "Dadas as circunstâncias..."
    r "Minha nota para a equipe 2 é..."
    "A produção coloca uma música de tensão."

    r "5.1!"
    "!!!"
    "O-o que...?"
    "Todos permanecem em choque por uns instantes."
    j "5-5.1??"
    "Juni se vira para Linne, ainda em choque."
    j "Então nós..."
    l "Vencemos?!"
    Sr "Ha Ha, sim!"
    Sr "As vencedoras são Linne e Juni!"
    Sr "Meus parabéns, meninas!"
    "Confetes são lançados ao ar em comemoração."
    # elaborar comemoracao
    n "Espera aí um instante..."
    n "Você quase desmaiou provando aquele prato..."
    n "E mesmo assim deu a MAIOR NOTA?!"
    #"Nádia finalmente libera sua raiva."
    r "Eu não estava quase desmaiando..."
    r "Estava apenas... Saboreando o ingrediente especial da Juni!"
    r "Sabe ele deu um sabor..."
    #"Roko procura por palavras."
    r "Muito..."
    r "Huh..."
    r "..."
    r "Único!"
    r "Por isso achei que elas mereceram essa nota."
    n "Escuta aqui, sua-"
    l "Calma, Nádia. Não há motivos para ficar irritada."
    l "É só uma brincadeira..."
    #Sr "Exatamente. Vocês não sairam prejudicadas."
    n "Grrr!"
    "Ela vira as costas e sai batendo os pés."
   
    "É melhor eu conversar com ela."
    m "Nádia, espera!"
    "Corro atrás dela enquanto o Sr.Star encerra o evento."
    "Já estamos na metado do caminho para os dormitórios quando finalmente a alcançou."
    n "Argh! O que foi agora?!"
    n "Será que não posso ter um minuto de paz!??"
    m "Podemos conversar um segundo?"
    n "..."

    menu(nvl=True):
        "Você não devia reagir assim":
            m "Sei que está zangada, mas..."
            m "Explodir daquela forma na frente de todos é loucura!"
            n "Isso... não é algo fácil de controlar e você sabe disso!"
            n "Afinal, aquilo foi muito pessoal."
            m "..."
            m "Mas se você continuar assim..."
            m "Quem sairá prejudicada será você!"
            n "... Não preciso da sua preocupação."


        "O julgamento está errado.":
            m "Olha eu te entendo..."
            m "Pela forma que Roko fez o julgamento..."
            m "Ela-"
            n "Tem algo pessoal contra nós? Sim. Eu percebi!"
            n "Ela deve achar que a gente é algum tipo se seres primitivos! Por isso fez aquilo!"
            n "Porque não se manifestou naquela hora? Você também fazia parte da equipe."
            m "..."
            "Mas que situação complicada..."
            $ roko -= 3

    "Solto um longo suspiro."
    m "É melhor esquecermos isso."

    "Ouço as outras garotas chegando a nós."
    r "Ora se não é a pavio curto e companhia!"
    r "Espero que tenha esfriado a cabeça após aquele pequeno show."
    "O comentário incomoda não apenas Nádia, mas também Juni."
    n "Você que dá um julgamento totalmente inconsistente e eu saio como louca?!"
    l "Ela não disse isso!"
    l "Não há motivos para brigar, meninas!"
    l "Aquilo não era importante-"
    j "Quem pensa que é..."
    j "Quem você pensa que é para dar apelidos para os outros, Roko!"
    #"Surpresas, encaramos Juni."
    r "!"
    j "Err... Quero dizer..."
    j "E-essa não é uma atitude... Muito legal..."
    n "Concordo plenamente."
    r "..."
    r "Te dou 0.1 ponto a mais e é assim que me agradece?"
    r "Deveria ter avaliado aquela porcaria como um completo zero!"
    # de qual lado ficar?
    l "Agora já chega!"
    l "Isso está indo longe demais!"
    l "Não podemos nos esquecer..."
    l "Que no final somos todas colegas e-"
    n "Cansei dessa conversa fiada!"
    n "Tô indo pro meu quarto. Uma boa noite pra vocês."
    "Nádia segue em direção aos dormitórios."
    l "Bem... Vamos deixar ela esfriar a cabeça."
    l "Vocês não sabem do que ela é capaz quando está com muita raiva..."
    r "Hã?! Como assim?"
    l "Acreditem em mim... Eu a conheço há muito tempo."
    m "Conhece?"
    l "..."
    l "Está tarde... Vamos dormir, meninas."
    # final da discussao

    $ atividade = "Antes de dormir"

    "Finalmente, tomei um banho e estou pronta para dormir."
    "Caramba, estou exausta!"
    "???"
    "Enquanto me dirigia ao meu quarto, escuto uma voz vinda do quarto fechado ao lado..."
    r "... Eu já não aguento mais!"
    "Essa é Roko..."
    "Me aproximo da porta para ouvir melhor."
    r "Estou sofrendo uma pressão enorme para treinar duro..."
    r "Todas aqui são grosseiras... não me tratam com o mínimo de atenção e respeito que mereço."
    r "E pra piorar eles me obrigam a usar esse shampoo barato!"
    r "Ai, isso não é justo! Não era pra ser tão difícil assim!"
    "Escuto ela chorar lá dentro."
    r "Eu tinha certeza de que daria conta..."
    "..."
    "E-Eu gostaria de ajudar... Mas acho que seria muita intromissão minha."
    "Talvez eu converse com ela sobre isso mais tarde."

    jump cap2_1

