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
    p"{i}Mas nossa presença foi solicitada no pátio às 8:30{/i}"
    p"{i}É melhor eu começar a me preparar{/i}"
    p"{i}Não quero estragar tudo logo no primeiro dia.{/i}"

    "Saindo para o corredor dou de cara com as outras."
    "Todas estavam saindo de seus quartos parecendo ter acordado agora também."
    "Exceto Linne."
    "Percebemos isso quando passamos pela sala, onde a encontramos escrevendo algo em um caderninho."
    lh "Bom dia, garotas!"
    m "Bom dia."
    "Juni boceja alto."
    jn "Bom dia."
    nsm " 'Dia."
    "Roko apenas se dirige ao banheiro."
    "E as outras garotas continuam seus preparativos."
    ln "Algum problema, Moon? Você está com uma cara horrível."
    m "N-Não... Nenhum problema..."
    m "É só que... Eu tenho problemas em acordar cedo."
    lh "Entendi. O despertador deve ser o seu maior inimigo, né? hi hi."
    m "Heh... Sim, sim."
    p"{i}Gostaria que isso não fosse verdade...{/i}"

    menu(nvl=True):
        "Falar com Linne":
            m "Linne, que horas você levantou?"
            m "Parece estar acordada há horas."
            ln "Ah, não... Nem estou de pé há tanto tempo."
            ln "E também já estou acostumada a acordar cedo."
            m "Nossa..."
            menu(nvl=True):                
                "Quanta determinação":
                    m "Você parece tão disposta, Linne."
                    m "Admiro que consiga acordar tão cedo e ainda estar com um sorriso no rosto."
                    lh "Muito obrigada, Moon... Nossa, fiquei até sem graça."
                    p "{i}Ela está realmente contente.{/i}"
                    $ linne += 1
                    ln "Enfim... Não é melhor você se aprontar?"
                    m "Ah! Sim, é verdade!"
                    m "Nos encontramos mais tarde!"
                "Ainda é muito cedo":
                    m "Mas... Ainda há muito tempo até às 8:00."
                    m "Precisava mesmo estar pronta com tanta antecedência?"
                    ln "Hmm..."
                    ln "Não gosto de deixar as coisas pra última hora."
                    p"{i}Não sei se isso responde minha pergunta...{/i}"

        "Continuar minhas tarefas":
            m "Bom, é melhor me apressar..."
            ln "Ah, claro."
            ln "Boa sorte hoje."
    #jump end

label cap1_2:
    $ periodo = "Manhã"
    $ atividade = "Entrevista"
    #transicao foda
    Srn "Começamos em alguns instantes!"
    Srn "E não se preocupem! Dessa vez não será ao vivo."
    "..."
    p"{i}Essa demora está me deixando ansiosa.{/i}"
    p"{i}E observando bem... Juni também está tensa.{/i}"
    menu(nvl=True):
        "Tentar acalmá-la":
            m "Ei, Juni!"
            #"Ela olha para mim confusa e surpresa."
            jn "Ahn??"
            m "Não precisa ficar assim... Sei que vai se sair bem!"
            jn "Ah... T-tudo bem."
            jn "..."
            $ ajuda_j = True
            $ juni += 1

        "Não fazer nada":
            "..."

    Srn "Começamos em 3..."
    Srn "2..."
    Srn "E..."
    Srh "Sejam muito bem vindos de volta ao reality Star's Selection!"
    Srh "Chegou o momento de esclarecermos alguns pontos do programa."
    Srn "Todos devem saber que em em realitys de sobrevivência"
    Srn "Os participantes vão sendo declassificados ao decorrer dos testes."
    Srn "A pior das performances, infelizmente, será eliminada"
    Srn "E voltará para casa."
    Srn "As participantes também estão sujeitas ao julgamento do público."
    Srn "Pois, caso algum comportamento não os agrade..."
    Srh "Vocês poderão entrar em nosso site para exigir uma punição!"
    p"{i}Parando pra pensar... Isso é bem pesado.{/i}"
    p"E ele ainda anuncia isso com um sorriso no rosto..."
    Srn "Agora, sobre os testes:"
    Srn "Eles serão aplicados periodicamente."
    Srn "São fundamentais para decidir quem sai..."
    Srh "E para avaliar as performances em geral e exaltar a melhor!"
    Srn "E, obviamente..."
    Srn "Após o período de testes haverá um descanso para nossas pequenas estrelas."
    Srn "O espaço do reality possui o alojamento das garotas"
    Srn "Espaços de treinamento, como a sala de dança, estúdio e academia."
    Srn "E espaços de lazer, como a sala de estar, a área externa e a cozinha."
    Srn "Então, respondendo sua pergunta, senhorita Nádia..."
    Srh "Vocês são livres para fazerem o que quiserem nesses espaços."
    nn "Ah..."
    Srn "Bom... Creio que esclareci tudo o que precisava."
    Srn "Agora vocês acompanharão as participantes em suas atividades antes da performance."
    Srh "E ficarão sabendo mais sobre elas de pertinho!"
    Srn "Ah, e não se esqueçam que hoje à noite teremos um grande evento!"
    Srh "Eu sou o Sr. Star, e você está acompanhando o reality Star's Selection!"
    "A gravação encerra."
    Srn "Muito bem, equipe!"
    Srn "Agora, senhoritas..."
    Srsc "Vocês serão entrevistadas individualmente em suas atividades de treino."
    Srsc "Espero que estejam preparadas."


    # entrevista particular
    "Uma a uma, as garotas são entrevistadas. Logo chega a minha vez."
    "Vejo muitas cameras aponatadas para mim e o sr.Star."
    "Ele fala animadamente com uma delas."
    Srn "Finalmente, chegou a vez de Moonie falar um pouco sobre si."
    Srh "Adimito que estava bem animado para ouvir mais sobre você, querida."
    m "Hã? Quer dizer... Muito obrigada Sr.Star."
    p"{i}Será que é só um modo de falar... Ou ele realmente acha isso?{/i}"
    Srn "Gostaria de compartilhar sua rotina?"
    m "C-claro!"
    m "Logo de manhã eu faço minha skincare e tomo meu café da manhã-"
    Srh "Ahh, sim, sim! Não deve ser fácil manter esse rostinho bonito, não é mesmo?"
    p"{i}E mais uma vez, ele me interrompe.{/i}"
    p"{i}Parece que vou ter que me acostumar...{/i}"
    Srsu "Oh, me perdoe senhorita."
    Srh "Por favor continue, querida."
    m "Bem... ainda na parte da manhã eu faço pilates e treino canto."
    m "Já no início da tarde eu almoço e, logo após, tiro uns 30 minutos para mim."
    m "Treino dança e fortaleço minha resistência no restante da tarde."
    m "Ah, eu também gosto muito de tomar um chá da tarde quando sinto fome..."
    m "Enfim, durante a noite faço novamente minha skincare, cuido do meu cabelo e unhas."
    m "Janto e me preaparo para dormir."
    Srn "*bocejo*"
    # ele é mt bom em destrir a moral das participantes
    Srn "Bem, não vi nada de mais... Existem rotinas melhores por aí..."
    Srn "Por um momento, eu esperei algo mais interesante."
    p"{i}C-Como assim ele esperava mais? Isso já não é o suficiente?{/i}"
    Srn "Mas quem sou eu para julgar, não é?"
    Srn "Agora, me deixe perguntar o que todos querem saber..."
    Srn "Qual é..."
    Srh "O seu segredo?"
    m "S-Segredo... ?"
    Srn "Como faz para ter essa pele de porcelana?"
    Srh "E esse cabelo Impecável? Ou esse corpão violão?"
    m "Hmmm... N-não sei..."
    Srn "Ora, deixe de suspense, querida. Diga logo!"
    Srn "O público precisa saber!"
    m "A-Acho que não faço nada de mais..."
    Srsu "Nem um procedimento estético? Ou produtos milagrosos?"
    m "O que? Nada disso."
    Srsc "..."
    m "Hmm... P-Perdão se eu disse alguma cois-"
    Srh "Ha ha! Isso é ótimo!"
    Srn "Saiba que, mesmo tendo essa personalidade beeem sem sal ao meu ver..."
    Srn "Todo mundo adora um rostinho bonito!"
    p"{i}S-Sem sal?!{/i}"
    Srh "Eu APOSTO que vai se dar bem no programa!"
    Srn "Era só isso mesmo que tinha para conversar com você, querida."
    Srn "Muito obrigado e boa sorte com os seus treinos."
    Srn "E não se atrase para o evento de hoje à noite, viu?"
    Srn "Está dispensada."
    p"{i}Ainda não posso acreditar que ele me chamou de sem sal...{/i}"
    p"{i}Será que todo mundo pensa assim?{/i}"


label cap1_3:


    $ periodo = "Tarde"
    "Hora do almoço."
    p "{i}Finalmente. Estou morreeendo de fome.{/i}"


    if reconhecimento:
        m "???"
        "{i}Escuto alguém se aproximar de mim.{/i}"
        jn "Ei, Moon!"
        "{i}É a Juni.{/i}"


        if ajuda_j:
            jn "Não tive oportunidade d-de te agradecer naquela hora."
            m "Agradecer por...?"
            jn "Por me apoiar hoje mais cedo."
            jn "E sabe..."
            jn "Você também parecia nervosa."
            jnv "E-então... Quero que saiba que está se saindo bem!"  
            jn "Ah! Mais uma coisinha..."      
        jn "Hm..."
        jn "Naquele hora, no dia da primeira apresentação"
        jn "O que você disse algo sobre ser alguém importante..."
        jn "Achei interessante..."


        menu(nvl=True):
            "...":
                m "..."
                "Nos encaramos por um tempo."          
                jnv "..."
                jnv "Enfim... Era só isso que queria dizer."
                $ juni -= 1


            "É mesmo?":
                m "Oh!"
                m "você achou mesmo?"
                jn "... Ahan."
                m "Isso é ótimo!"
                m "Obrigada, você é muito gentil."
                jh "Ah, imagina."
                jn "Bem..."


            "O que quer dizer?":
                m "Interessante? Como?"
                jn "..."
                p "{i}Ela tá me deixando nervosa...{/i}"
                m "Por que está me olhando assim?..."
                "Ela percebe que estava me encarando."
                jsu "Ah, meu Deus!"
                jnv "Eu n-não percebi que estava te deixando nervosa."
                js "Nossa, me desculpa..."
                jn "É só que... Foi muito legal o que disse."
                jn "Então queria saber se realmente..."
                m "Sim?"
                jnv "Hmm... Bem..."
                "Ela reflete por um momento."
                jn "Ah... Deixa pra lá."


        jn "Acho que precisamos ir, agora..."
        jn "Afinal, temos um evento p-para protagonizar mais tarde."
        jh "He he..."
        jnv "Err... T-Tchau."
        "Ela se vira rapidamente e vai embora."
        m "Foi um prazer!"
        p "{i}Acho que ela nem escutou...{/i}"
        p "{i}Caramba... Não achei que fosse encontrar uma pessoa tão ansiosa quanto eu...{/i}"
        p "{i}Talvez eu converse melhor com ela depois.{/i}"
        p "{i}Agora, eu tenho que comer algo antes que eu desmaie (drama).{/i}"


    # hr do almoço
    "Chegando no refeitório, encontro Linne almoçando."
    ln "Olá, Moon."
    ln "Você viu o restante das meninas?"
    m "Não. Só vi a Juni..."
    m "Cadê ela, afinal?"
    jn "E-Estou aqui."
    p"{i}Não tinha reparado nela bem atrás de mim.{/i}"
    ln "Venham. Juntem-se à mesa."
    "Nos juntamos a ela na mesa para almoçar."
    ln "O que acharam da entrevista, meninas?"
    jnv "Acho q-que não foi nada de mais..."
    ln "Não precisa ser tímida. Pode falar."
    jnv "..."
    ln "Bem, já que é assim..."
    ln "O que achou Moon?"
    menu(nvl=True):
        "Foi bom.":
            m "Apesar de algumas coisinhas... Acredito que ocorreu tudo muito bem."
            ln "Ah... Eh, isso é bom."
            ln "Não é todo mundo que consegue se manter otimista nessas horas."
            jump cap1_al


        "Foi péssimo.":
            m "Não sei..."
            m "Talvez o Sr.Star tenha uma péssima impressão sobre mim."
            ln "Poxa, que chato..."
            ln "Mas... Tenho a impressão de que você está sendo pessimista, Moon."
            jump cap1_al




        "Tanto faz.":
            m "Na verdade, não tenho nada a comentar."
            ln "Nada? Nenhuma impressão ou opinião?"
            m "Err... Não."
            li "... Então, tá."
            li "Já que vocês não querem conversar comigo... Eu vou me retirar."
            "Ela se levanta de maneira dramática."
            li "Até logo."
            p "{i}Será que ela ficou magoada? Mas essa não era minha intenção...{/i}"
            p "{i}Eu só queria comer meu almoço em paz.{/i}"
            js "..."
            p "{i}Juni também não parece querer conversar agora.{/i}"
            "Termino meu almoço sem trocar uma palavra com Juni."
            jump cap1_4




label cap1_al:
    ln "Tente tomar cuidado... Esse pensamento pode te arruinar um dia, sabia?"
    m "É mesmo? por que?"
    # tentativa de linne de diminuir moon e exaexaltar a si mesma
    ln "Você ainda é muito iniciante e não tem experiência suficiente para julgar algumas coisas, ora!"
    ln "Por isso você corre o risco de passar por muitos micos! Acredite em mim!"
    jnv "M-Micos?!"
    m "Nunca tinha pensado nisso..."
    ln "Melhor vocês começarem a se preocupar sobre. Já que isso envolve suas imagens."
    jnv "Uhg... Não gosto nem de pensar..."
    # potencializa uma insegurança das duas
    ln "Eu tenho alguma experiência na área e acreditem, eu já notei vários comportamentos problemáticos em vocês."
    lh "Hihi! Chega até a ser meio engraçado."
    "Ela se levanta da mesa graciosamente."
    lh "Preciso ir agora, meninas."
    # mesmo se esse dialogo n acontecer, juni vai procurar porn "ajuda" da linne
    ln "Mas se quiserem conversar mais sobre o assunto alguma hora, estarei disposta a ajudar."
    lh "Até logo!"
    "Linne sai."
    jnv "... M-Moon?"
    jnv "Acha mesmo q-que eu t-tenho... Co-comportamentos problemáticos?"
    "Juni tenta disfarçar sua tremedeira sem sucesso."
    p "{i}Confesso que isso me pegou desprevenida... Não achei que estava indo tão mal...{/i}"
    m "..."
    js "Não estou mais com fome..."
    "Ela sai correndo, deixando metade de um prato de salada para trás."




label cap1_4:
    # dps dos treinos da tarde
    $ atividade = "Depois dos treinos"


    "Resolvi dar uma olhada no jardim depois dos meus treinos da tarde. Precisava espairecer."
    "É um gramado bem verde, com um banco no meio de alguns arbustos. O céu estava bem limpo, poucas nuvens a vista."
    "Enquanto passava pelo jardim, encontrei Roko observando as flores."
    p "{i}Seria uma boa ideia conversar com ela?{/i}"
    menu(nvl=True):
        "Sim":
            "Me aproximo para conversar com ela."
            m "Olá, Roko!"
            rsu "AAAH!"
            ra "Pelos céus! Você me assustou!"
            rn "Onde estão seus modos??!"
            m "Ah, me desculpa."
            m "Não foi minha intenção..."
            ri "Hump!"
            rn "O que quer comigo, afinal?"
            m "Eh..."
            m "Só queria perguntar como foi a sua performance..."
            rc "Ah, sobre isso..."
            rc "Foi ótima, se quer saber a minha opinião."
            rc "Parece até que nasci pra isso."
            m "Caramba!"
            m "Fiquei sem palavras diante de tanta confiança."
            rc "Isso acontece com os menos afortunados, de fato."
            p "{i}Bem humilde...{/i}"
            rc "É como eu sempre digo:"
            rc "Para se tornar uma verdadeira estrela"
            rc "Primeiro você deve acreditar que já é!"
            rc "Afinal, é a minha opinião que importa."
            "Ela estufa o peito e empina o nariz."
            menu(nvl=True):
                "Não é bem assim que funciona.":
                    m "Entendo que autoconfiança é importante..."
                    m "Mas, não acho que seja bom ter em excesso."
                    rsu "Como?"
                    m "Sabe... Você pode acabar perdendo a noção da realidade..."
                    m "E prejudicando tanto a si mesma quanto os outros a sua volta."
                    ri "Prejudicando?"
                    ri "Não, não... Você entendeu errado."
                    ra "Ahf... Não vou discutir."
                    ra "Você não entenderia de qualquer forma..."
                    p "{i}Acho que VOCÊ não entenderia de qualquer forma.{/i}"




                "Tem razão.":
                    m "Faz sentido..."
                    m "Acho que tem razão!"
                    rc "Tenho, sim!"
                    rc "Viu? Foi assim que te convenci."
                    rc "Se você acredita em algo fielmente"
                    rc "As outras pessoas vão acreditar também!"
                    p "{i}UAU!{/i}"
                    $ roko += 3
   
            # termino do assunto
            rn "..."
            m "..."
            "Observamos o jardim em silêncio por um tempo."
            rn "É um belo jardim."
            m "Sim..."
            rn "Ele me lembra de casa..."
            rn "Claro que o de lá é bem maior."
            rn "E mais bonito também."
            rn "Mas isso é por conta do nosso jardineiro."
            rn "Um senhor de idade muito calado..."
            rn "As vezes, eu costumo sentar em um dos bancos..."
            rh "E conversar com ele enquanto trabalha."
            ri "Ele quase nunca me responde."
            rh "Mas eu sei que ele me escuta com atenção."
            rn "..."
            rn "Um dia, quando eu era menor, ele me perguntou o motivo de minhas visitas constantes."
            rn "Então eu respondi que todos os meus amigos estavam viajando com os pais."
            rn "Enquanto os meus estavam sempre bem ocupados."
            m "Poxa..."
            rh "Ele também reagiu da mesma forma."
            rn "Bem..."
            rn "Mais tarde, ele me trouxe uma cesta cheia de tomates que ele mesmo tinha cultivado."
            rn "Sugeriu convidarmos a chef"
            rn "Para que nos ajudasse a preparar alguns lanches com eles."
            ra "Eu não gostei da ideia no início, pois não como nada com a cor vermelha."
            m "Nada com a cor vermelha? Por que?"
            ri "Porque eu acho muito nojento!"
            rn "Mas... Naquele momento eu pensei:"
            rn "Por que não?"
            rh "Aí nós três nos juntamos"
            rh "E seguindo as ordens da nossa chef, fizemos sanduíches para o café da tarde."
            rh "Cheguei até a me divertir no processo."
            rn "Então, na hora de provar eu tive certeza..."
            ri "De que definitivamente ODEIO comidas vermelhas!"
            $ vermelho = True
            p "{i}O QUEEE!!?{/i}"
            ri "Fiquei tão frustrada! Joguei o sanduíche de volta no prato e subi chorando para meu quarto."
            ri "Eca! só de lembrar daquele gosto horrível na minha boca..."
            "Ela cobre a boca como se estivesse prestes a vomitar."
            ri "..."
            rn "Pensando agora..."
            # Inventar nome pro veio (Helian)
            rn "O sr. Helian deve ter ficado deveras decepcionado..."
            menu(nvl=True):
                "E com razão!":
                    m "Com certeza!"
                    m "Isso foi péssimo da sua parte!"
                    ra "E você queria que eu fizesse o que?"
                    ra "Fingir que gostei!?"
                    m "Não! Mas você poderia pelo menos agradecer."
                    m "Era literalmente o mínimo!"
                    "Ela bufa, irritada."
                    ra "Urhg! Você é muito ignorante!"
                    ra "Você e aquela Nádia!"
                    m "O que?!"
                    m "Quer saber? Eu tenho mais o que fazer!"
                    "Me afasto sem olhar pra trás."
                    "{i}Tenho que voltar a treinar...{/i}"
                    jump cap1_5
                    $ ignorante = True








                "Talvez...":
                    m "Olha..."
                    m "Talvez o que importasse, no final, não era o sabor do sanduíche."
                    m "Mas sim a experiência do processo!"
                    m "Você mesma disse que não tinha gostado da ideia."
                    m "E mesmo assim aceitou participar."
                    m "Tenho certeza de que ele deve ter ficado contente por isso."
                    rn "Acha isso mesmo...?"
                    rn "Bem... Deve estar certa..."
                    rh "Afinal, você se parece bastante com ele."
                    $ roko += 5
                    p "{i}Ah, nossa!{/i}"
                    p "{i}Me sinto até meio especial!{/i}"
                    p "{i}Pelo menos... pra Roko.{/i}"
                    # reacao de moon(n sei o que colocar ainda)




                    # termino do assunto e convite pra treinar
                    m "Ah, não! Devo estar atrasada pro treino!"
                    rn "Treino? Mas já não treinamos hoje cedo?"
                    m "Hmm... sim..."
                    m "Mas nós precisamos treinar... mais!"
                    rn "Oh..."
                    "Roko está em choque."
                    "{i}Ela não sabia que nós treinamos o dia todo?{/i}"
                    menu(nvl=True):
                        "Convidar Roko para treinar":
                            m "Se quiser pode vir comigo..."
                            rn "Não, não... eu já atingi meu limite hoje e não quero cansar minha beleza."
                            rh "Que tal... amanhã? De manhãzinha?"
                            m "Claro! Costumo fazer pilates de manhã."
                            m "Pode me encontrar na academia."
                            $ treino_roko = True
                            rn "Certo. Me aguarde."








                        "Não convidar Roko para treinar":
                            m "Err... preciso muito ir agora..."
                            rn "Ah, sim..."
                            rh "Desejo boa sorte."




                    # encerramento do dialogo


        "Não":
            p "{i}Melhor não... Tenho que me preparar pro evento...{/i}"
           
    $ atividade = "Preparação do evento"
    "Dou uma última olhadinha no espelho e..."
    p "{i}É isso, estou pronta.{/i}"
    p "{i}Espero que eu não estrague tudo ou...{/i}"
    ln "Moonie? Cadê você? Vai acabar se atrasando!"
    m "Hã? J-Já tô indo!"




label cap1_5:
    # inicio do evento
    # Determinar local do acontecimento(fiquei em duvida)
    $ periodo = "Noite"
    $ atividade = "Evento ao vivo"




    "Ao chegarmos ao local, tudo estava preparado para uma gravação."
    "Observamos que estão dispostas mesas, utensílios de cozinha e vários ingredientes."
    "Confusas, nós todas nos entreolhamos."
    Srn "Boas vindas, meninas!"
    Srn "Espero que tenham aproveitado o dia."
    lh "Ah, nós aproveitamos sim!"
    ln "Mas... Se me permite a pergunta..."
    ln "O que está havendo aqui?"
    Srn "Ora! Não tenha pressa!"
    Srh "Vocês descobrirão em breve..."
    "Ele se diverte fazendo suspense."
    jnv "Uhg... Isso não parece bom..."
    Srn "Não se preocupem."
    Srn "Será divertido, eu garanto!"
    rn "Divertido...?"
    Srn "Vamos ao ar em alguns instantes!"      
    ln "Estejam preparadas, garotas."
    "Linne ajeita a postura e muda a sua expressão para algo mais confiante."








    Srn "Começamos em 3..."
    Srn "2..."
    Srn "1..."
    Srh "{i}Muito boa noite a todos!{/i}"
    Srh "Está começando agora o nosso primeiro grande evento ao vivo do reality Star's Selection!"
    Srn "E hoje, senhoras e senhores..."
    Srn "Organizamos um desafio diferenciado para nossas pequenas estrelas."
    Srn "As quais ainda não fazem ideia do que está por vir."
    Srh "He he he"
    "{i}Algo não cheira bem aqui...{/i}"
    Srn "Muito bem! Estão prontas?"
    Srn "O desafio de hoje será..."
    Srh "Uma competição gastronômica!"
    nsu "Uma... O que?"
    Srh "É isso mesmo!"
    Srn "Serão sorteados dois grupos de duas pessoas"
    Srn "O resultado aparecerá no telão logo atrás de nós."
    Srn "Quem ficar de fora será a jurada."
    Srn "A equipe que preparar o melhor prato ao gosto da jurada..."
    Srh "Sairá vitoriosa!"
    Srn "Alguma pergunta?"
    rn "Teremos alguma recompensa por vencer?"
    Srn "Não, senhorita!"
    Sra "Este evento foi planejado para ser divertido e casual."
    Srh "Por isso não haverá recompensas."
    Srn "No entanto, pode haver punições a equipe que tentar trapacear ou sabotar a competição."
    Srn "Algo mais?"
    ln "A jurada será uma de nós?"
    Srh "Sim, senhorita!"
    ln "Então... Como podemos garantir que ela será imparcial?"
    Srn "Bom, acho que devo lembrar as senhoritas:"
    Srn "Tudo o que fazem neste reality está sujeito ao julgamento do público."
    Srn "Caso identifiquem algum comportamento suspeito..."
    Srsc "Tenho certeza que eles não terão misericórdia."
    Srn "Mais alguma pergunta?"
    Srn "Não?"
    Srn "Nesse caso, que comece o sorteio das equipes!"
    Srn "A equipe 1 será composta por..."
    "No telão, aparece meu nome e o de Nádia."
    Srsu "Ah, Moonie e Nádia! Uma dupla promissora!"
    Srn "Podem se dirigir a área de preparo."
    Srn "E não se esqueçam de vestir seus aventais!"
    "Fazemos o que nos é solicitado rapidamente."
    "Enquanto vestimos nossos aventais, Nádia quebra o silêncio."








    nsr "Que situação 'curiosa', não?"


    menu(nvl=True):
        "Curiosa?":
            m "Hmm? O que quer dizer?"
            nn "..."
            nn "Você é bem lentinha, não?"
            "Ela suspira em desaprovação."
            m "Oh..."
            m "Me desculpa?"
        "Realmente...":
            m " É realmente bem 'curiosa' mesmo."
            nn "Ah, você também percebeu?"
            m "É claro!"
            m "Eles nem disfarçaram."
            nsr "Aposto que isso saiu direto do Sr.Star..."
            nsr "É melhor a gente ficar ligada."








    "Outros dois nomes aparecem no telão."
    Srsu "A equipe 2 será composta por Juni e Linne!"
    Srh "Uma equipe adorável, não é mesmo?"  
    Srh "Ha ha!"
    Srn "Pode se preparar, equipe 2!."
    Srn "Bom... Parece que temos uma jurada!"
    Srn "Senhorita Roko!"
    "Nádia sussurra sarcasticamente."
    nsr "Nossah, mas que surpresa."
    rsu "E-eu??"
    ra "Não, não. Deve haver algum engano!"
    Srn "Não há enganos neste reality, querida!"
    Srh "Pode ficar tranquila."
    "Ele diz isso com um sorriso irônico no rosto, expressando exatamente o oposto."
    Srn "Roko escolherá um prato e as equipes terão 45 minutos para prepará-la."
    Srn "Ah, e não haverá acréscimo de tempo."
    Srn "jurada Roko! Qual será o prato desta noite?"
    rnv "Hãh..."
    p "{i}Consigo ver desespero e angústia nos olhos dela.{/i}"
    Srn "Sim?"
    rnv "Que tal..."
    "Finalmente acende uma lâmpada na cabeça dela."
    rc "Espaguete!"
    Srn "Espaguete?"
    rc "Isso!"
    rn "Mas sem-"
    Srn "É isso! Grupos 1 e 2 terão 45 minutos para preparar um prato de Espaguete!"
    ra "Espera, não acabei de falar-"
    Srn "Começando exatamente agora!"
    "O tempo em minutos aparece no telão."
    Srh "Uma boa sorte para vocês!"
    nn "Pelo menos ela não escolheu um daqueles pratos chiques e complicados..."
    nn "Alguma sugestão do que fazer?"








    if(vermelho):
        m "Não exatamente..."
        m "Mas eu sei que ela não gosta de coisas vermelhas."
        nsu "Ela o que!?"
        m "Não gosta d-"
        nsr "Espera, eu ouvi da primeira vez."
        nsr "Tipo, como assim ela 'não gosta de coisas vermelhas'?"
        na "Palhaçada isso!"
        "Nádia está completamente indignada."
    else:
        m "Não tenho nem ideia."
        nn "Ótimo..."
        nsm "Vamos fazer o tradicional espaguete com almôndegas e molho de tomate."
        nsm "Não tem como errar nisso."
        "Ao buscarmos pelos ingredientes notamos que não há mais tomates nem almôndegas."
        nsr "Elas pegaram tudo!"
        m "Acho que chegamos tarde."
        na "Urhg!"
        m "Calma, vamos fazer outra coisa."
        "Ela respira fundo e se acalma."


    nn "Nesse caso..."
    nsm "Podemos preparar um espaguete ao molho branco."
    nsm "Você prepara a massa enquanto eu faço o molho."
    m "Pode ser!"


    nsr "Temos disponíveis aqui:"
    nsr "Massas dos tipos tradicional e linguine..."
    m "Linguine é um macarrão?! Pensei que fosse aquele moço do Ratatouille..."
    nn "..."
    nsm "Meio que é isso também... Mas na verdade esse é aquele macarrão mais achatado, sabe?"
    nsr "Temos aqui também os queijos parmesão, gorgonzola e mussarela..."
    nsr "E de proteínas temos frango, salmão e bacon."
    nn "Qual massa você acha uma boa?"


    "Nádia espera por uma resposta."
    $ time = 5
    $ timer_range = 5
    $ timer_range = 'escolha_devagar'


    menu:
        "Tradicional":
            m "Eu gosto do tradicional."
            nsm "Todo mundo gosta do tradicional."
            $ tradicional = True
        "Linguine":
            m "O Linguine parece interessante."
            nsm "Ce escolheu esse por causa do desenho do rato, né?"
            menu(nvl=True):
                "Não...":
                    m "Não, não! Eu nunca faria uma coisa desas!"
                    nsm "Sei..."
                "Talvez...":
                    m "Hmm... Talvez..."
                    nh "Meu irmãozinho de 10 anos teria respondido a mesma coisa."
                    m "Ei!"

    nn "E o queijo?"

    $ time = 5
    $ timer_range = 5
    $ timer_range = 'escolha_devagar'
    show screen countdown
    menu(nvl=True):
            "Parmesão. ":
                hide screen countdown
                nsm "Hmm..."
                $ parmesao = True
            "Gorgonzola. ":
                hide screen countdown
                nsr "Eca! que nojo!"
                m "Que foi? Não gosta?"
                nsr "E você gosta?"
                nsr "Não devia ter deixado você ajudar..."

    nn "Agora... a carne"

    $ time = 5
    $ timer_range = 5
    $ timer_range = 'escolha_devagar'
    show screen countdown

    menu(nvl=True):
        "Frango":
            hide screen countdown
            nsm "Hmm, parece uma boa."
            $ frango = True
            jump escolha_rapida
        "Bacon":
            hide screen countdown
            nn "Você é estranha..."
            jump escolha_rapida

label escolha_devagar:
    nsr "Credo, cê demora demais!"
    nsr "Deixa que eu faço."
    "Ela me afasta e escolhe os ingredientes sozinha."

label escolha_rapida:   
   
    "Coletamos os ingredientes e materiais e começamos a trabalhar."
    "Enquanto espero o macarrão cozinhar, observo Nádia fazer sua parte."
    "Ela é rápida e confiante em seus movimentos."
    "Chega até a cantarolar uma música."
    m "Você parece bem confortável."
    nsu "Ah! Eu?"
    nsm "É que na verdade já estou acostumada, sabe."
    nsm "Minha família tem um restaurante"
    nsm "E eu costumava ajudar na cozinha."
    m "É sério!? Caramba, que legal!"
    nn "Na verdade, não era tão legal assim."
    nsr "Tinha muito problema e dor de cabeça..."
    nn "Ainda tem, no caso…"
    nn "Com o tempo as coisas pioraram por causa do dinheiro."
    m "Ah..."

    if ignorante:
        nn "Bem que eu poderia ter nascido bem rica pra não ter que passar por esse tipo de coisa..."
        nsr "Tipo aquela metida da Roko. O maior dos problemas dela deve ser decidir em que continente vai passar as férias."
        nsr "Eu odeio ela... Sempre me olha com aquela cara de nojo."
        m "Ela te olha com nojo? Que horror!"
        nsr "Não me conformo que uma pessoa dessas já tenha ganhado na vida só por ser herdeira."
        # olha a fofoca
        m "Hoje mais cedo, eu estava conversando com ela."
        m "Você não vai acreditar no que ela disse..."
        nsr "O que ela disse? Vai, fala logo!"
        m "Ela chamou a gente de ignorante!"
        na "Não acredito!"
        na "Nossa, se eu ver ela na rua..."
        "{i}A Nádia está com MUITA raiva.{/i}"
        na "Seria suspeito se, acidentalmente, a gente colocasse um 'pouco' de pimenta no prato dela?"
        m "Acho que sim..."
        m "Vamos deixar essa vingança pra depois."

    "O tempo passou enquanto preparavamos a comida."
    nn "Hmm... Acho que vou adicionar alguns brócolis."
    nn "Tô achando a receita meio sem graça."
    Srn "O tempo está se esgotando, meninas!"
    m "Vamos ter que nos apressar."


label cap1_6:
    # entrega dos pratos
    Srn "Tempo esgotado!"
    Srn "Equipe 1, apresentem seus pratos por gentileza."
    "Levamos nosso prato ao balcão de Roko."
    #Srn "Começando por Moonie e Nádia."
    Srn "O que prepararam?"
    m "Fizemos um delicioso espaguete ao molho branco, com queijo e carne."
    nsm "E brócolis."
    "Roko se esforça para não fazer cara de nojo mais uma vez."
    Srn "Pode provar, jurada."
    "Ela empurra os brócolis para um canto do prato com o garfo."
    "E prova a massa com molho."
    rnsu "Hmm..."
    rn "Até que não está ruim..."
    rn "Eu daria um 8..."
    Srsu "8 é uma boa nota!"

    if (tradicional && parmesao && frango):
        Srn "Algo mais a comentar, senhorita Roko?"
        rn "Bem que o macarrão poderia ser fresco."
        Sra "Aí já é pedir demais."
        Srn "Será que a equipe 2 fará um trabalho melhor?"
        Srh "É o que vamos descobrir em instantes! Então fique ligado!"
        $ aceitavel = True
        jump prato2

    ri "Mas como tem brócolis a minha nota final é 5!"
    Srsu "!!!"
    p "{i}Ah não, não pode ser...{/i}"
    p "{i}Como ela tem a audácia!?{/i}"
    "Olho para o lado e vejo Nádia com uma expressão vazia."
    "Mas sinto o ódio crescente nela."
    Sra "Ehr..."
    p "{i}Até mesmo o Sr.Star parece indignado.{/i}"
    Srn "Neste caso... 5 é a nota final!"
    Srn "He he..."
    "Ele ri meio sem graça."

label prato2:
    Srn "Podem ir, meninas. Vocês fizeram um ótimo trabalho!"
    Srn "Equipe 2, por favor, apresente-se!"
    "As meninas da equipe 2 dispõem seu prato sobre o balcão de Roko."
    "Roko arregala os olhos ao observar o macarrão coberto de molho de tomate."

    if (vermelho):
        "Nádia sussurra ao meu lado."
        nsm "Parece que a Carminha Frufru se deu mal..."
       
    Srsu "Uhh! Parece muito bom!"
    Srn "Podem dizer do que se trata?"
    ln "Temos aqui o clássico e muito amado espaguete com almôndegas."
    ra "E... molho de tomate...?"
    jh "Sim! Foi temperado com um ingrediente secreto especial meu!"
    "Juni parece orgulhosa sobre isso."

    if (vermelho):
        "{i}Mal ela sabe...{/i}"

    ra "... Tenho mesmo que comer isso?"
    Srn "Para dar uma nota, você precisa primeiro provar."
    ra "Ok..."
    "Ela hesita em provar por algum tempo."
    Sra "Apresse-se! O prato vai esfriar!"
    "Depois de muito esforço mental, ela leva o garfo à boca."
    rnv "..."
    "Ela mastiga devagar..."
    Srn "Está tudo bem, srta. Roko...?"
    ra "..."
    "Ela continua mastigando."
    "Seu rosto começa a suar e empalidecer."
    "Ela parece prestes a vomitar ou desmaiar."
    Srsu "Meu Deus, há algo errado!"
    "As meninas da equipe 2 também parecem nervosas."
    lsu "Oh, não! O que houve?!"
    nh "Meninas, quando eu falei de envenenar ela, eu estava BRIN-CAN-DO, tá bem?"
    "Nádia se diverte com a situação."
    Srsu "Equipe médica, por favor!"
    "Sr.Star acena para chamar os primeiros socorros."
    "Nesse momento, Roko finalmente consegue engolir."
    ra "Arhg!"
    ra "Não precisa, eu estou bem..."
    Srsu "Ufa!"
    "Todos parecem bem mais aliviados."
    Srsu "A senhorita realmente nos preocupou..."
    Srn "Gostaria de uma pausa para respirar, srta. Roko?"
    ra "Não, não."
    ra "Isso já foi o suficiente para minha decisão final."
    "O clima se torna mais tenso após suas palavras."
    Srn "Bem... Então..."
    Srn "Diga-nos a sua escolha!"
    rn "Dadas as circunstâncias..."
    rn "Minha nota para a equipe 2 é..."
    "A produção coloca uma música de tensão."
    rn "5.1!"

    if aceitavel:
        nn "UUUHUUUUU! Nós vencemos!"
        Srn "Com licença, srta.Nádia? Sou eu quem anuncia as coisas aqui."
        nn "Opss, foi mal."
        Srn "Senhoras e senhores, eu declaro Moonie e Nádia as vencedoras de hoje!"
        "Confetes são lançados ao ar em comemoração."
        Srn "Meus parabéns, garotas!"
        nn "Ha ha! Agora, sim! Nós vencemos!"
        m "Caramba, nem posso acreditar!"
        m "Eu queria dedicar essa vitória aos meus pais e aos meus amigos..."
        m "E a Nádia, também. Ela fez a maior parte."
        nn "Obrigada, obrigada."
        "Vejo Linne discutindo com Junie ao fundo..."
        nn "Mas até que, tipo... Cê foi bem."
        ln "Sr.Star, eu tenho uma objeção."
        Srn "Hm? Qual o problema, querida?"
        ln "Acredito que essa competição foi injusta."
        ln "Nádia claramente tem certa vantagem em culinária."
        Srn "E... Qual o problema?"
        # ela nao aceita perder
        ln "É que..."
        ln "A competição avaliou uma habilidade muito específica."
        ln "É como avaliar a habilidade de um peixe subir em árvores..."
        ln "Totalmente injunto."
        rn "É verdade. Eu concordo."
        ln "Nem estamos treinando para isso, não é Juni?"
        jn "Hm..."
        Srn "Ora, srta.Linne... Não vejo o motivo de sua preocupação."
        Srn "Afinal, isso é apenas uma brincadeira."
        ln "..."
        Srn "Mas se isso incomoda tanto, te recomendo começar um curso de culinária!"
        nn "Ha! Chuuupaaa!"
        rn "..."
        Srn "Bem, isso é tuuuuudo por hoje!"
        Srn "Mas não percam, logo voltaremos com muito mais!"
        Srn "Uma ótima noite à todos e até mais!"
        jump cap1_7
    else:
        "!!!"
        "O-O que...?"
        "Todos permanecem em choque por uns instantes."
        jn "5.1??"
        "Juni se vira para Linne, ainda em choque."
        jn "Então nós..."
        ln "Vencemos!"
        Srn "Ha ha, sim!"
        Srn "As vencedoras são Linne e Juni!"
        Srn "Meus parabéns, meninas!"
        "Confetes são lançados ao ar em comemoração."
        # elaborar comemoracao
        nn "Espera aí um instante..."
        nn "Você quase desmaiou provando aquele prato..."
        nn "E mesmo assim deu a MAIOR NOTA?!"
        #"Nádia finalmente libera sua raiva."
        rn "Eu não estava quase desmaiando..."
        rn "Estava apenas... Saboreando o ingrediente especial da Juni!"
        rn "Sabe ele deu um sabor..."
        #"Roko procura por palavras."
        rn "Muito..."
        rn "Huh..."
        rn "..."
        rn "Único!"
        rn "Por isso achei que elas mereceram essa nota."
        nn "Escuta aqui, sua-"
        ln "Calma, Nádia. Não há motivos para ficar irritada."
        ln "É só uma brincadeira..."
        #Srn "Exatamente. Vocês não sairam prejudicadas."
        nn "Grrr!"
        "Ela vira as costas e sai batendo os pés."
    
        "É melhor eu conversar com ela."
        m "Nádia, espera!"
        "Corro atrás dela enquanto o Sr.Star encerra o evento."
        "Já estamos na metado do caminho para os dormitórios quando finalmente a alcançou."
        nn "Argh! O que foi agora?!"
        nn "Será que não posso ter um minuto de paz!??"
        m "Podemos conversar um segundo?"
        nn "..."

        menu(nvl=True):
            "Você não devia reagir assim":
                m "Sei que está zangada, mas..."
                m "Explodir daquela forma na frente de todos é loucura!"
                nn "Isso... não é algo fácil de controlar e você sabe disso!"
                nn "Afinal, aquilo foi muito pessoal."
                m "..."
                m "Mas se você continuar assim..."
                m "Quem sairá prejudicada será você!"
                nn "... Não preciso da sua preocupação."


            "O julgamento está errado.":
                m "Olha eu te entendo..."
                m "Pela forma que Roko fez o julgamento..."
                m "Ela-"
                nn "Tem algo pessoal contra nós? Sim. Eu percebi!"
                nn "Ela deve achar que a gente é algum tipo se seres primitivos! Por isso fez aquilo!"
                nn "Porque não se manifestou naquela hora? Você também fazia parte da equipe."
                m "..."
                "Mas que situação complicada..."
                $ roko -= 3

        "Solto um longo suspiro."
        m "É melhor esquecermos isso."

        "Ouço as outras garotas chegando a nós."
        rn "Ora se não é a pavio curto e companhia!"
        rn "Espero que tenha esfriado a cabeça após aquele pequeno show."
        "O comentário incomoda não apenas Nádia, mas também Juni."
        nn "Você que dá um julgamento totalmente inconsistente e eu saio como louca?!"
        ln "Ela não disse isso!"
        ln "Não há motivos para brigar, meninas!"
        ln "Aquilo não era importante-"
        jn "Quem pensa que é..."
        jn "Quem você pensa que é para dar apelidos para os outros, Roko!"
        #"Surpresas, encaramos Juni."
        rn "!"
        jn "Err... Quero dizer..."
        jn "E-essa não é uma atitude... Muito legal..."
        nn "Concordo plenamente."
        rn "..."
        rn "Te dou 0.1 ponto a mais e é assim que me agradece?"
        rn "Deveria ter avaliado aquela porcaria como um completo zero!"
        # de qual lado ficar?
        ln "Agora já chega!"
        ln "Isso está indo longe demais!"
        ln "Não podemos nos esquecer..."
        ln "Que no final somos todas colegas e-"
        nn "Cansei dessa conversa fiada!"
        nn "Tô indo pro meu quarto. Uma boa noite pra vocês."
        "Nádia segue em direção aos dormitórios."
        ln "Bem... Vamos deixar ela esfriar a cabeça."
        ln "Vocês não sabem do que ela é capaz quando está com muita raiva..."
        rn "Hã?! Como assim?"
        ln "Acreditem em mim... Eu a conheço há muito tempo."
        m "Conhece?"
        ln "..."
        ln "Está tarde... Vamos dormir, meninas."
        # final da discussao

label cap1_7:
    $ atividade = "Antes de dormir"

    "Finalmente, tomei um banho e estou pronta para dormir."
    "Caramba, estou exausta!"
    "???"
    "Enquanto me dirigia ao meu quarto, escuto uma voz vinda do quarto fechado ao lado..."
    rn "... Eu já não aguento mais!"
    "Essa é Roko..."
    "Me aproximo da porta para ouvir melhor."
    rn "Estou sofrendo uma pressão enorme para treinar duro..."
    rn "Todas aqui são grosseiras... não me tratam com o mínimo de atenção e respeito que mereço."
    rn "E pra piorar eles me obrigam a usar esse shampoo barato!"
    rn "Ai, isso não é justo! Não era pra ser tão difícil assim!"
    "Escuto ela chorar lá dentro."
    rn "Eu tinha certeza de que daria conta..."
    "..."
    "E-Eu gostaria de ajudar... Mas acho que seria muita intromissão minha."
    "Talvez eu converse com ela sobre isso mais tarde."

    jump cap2_1

