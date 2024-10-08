label cap1_1:
    "TRRIN TRRIN TRRIN TRRIN TRRIN TRRIN"
    m "Ah!"
    "Acordo assustada como som do despertador"
    m "Hmmm..."
    "O relógio marca 6:30"
    m "Queria dormir só mais um pouquinho..."
    "Mas nossa presença foi solicitada no pátio às 8:30"
    "E faremos uma pequena performance durante a tarde."
    "É melhor eu começar a me preparar"
    "Não quero estragar tudo logo no primeiro dia."

    "Saindo para o corredor dou de cara com as outras."
    "Todas estavam saindo de seus quartos parecendo ter acordado agora também."
    "Exceto Linne."
    "Percebemos isso quando passamos pela sala, onde a encontramos escrevendo algo em um caderninho."
    l "Bom dia, garotas!"
    m "Bom dia."
    "Juni boceja alto."
    j "Bom dia!"
    n " 'Dia."
    "Roko apenas acena para nós e se dirige ao banheiro."
    "E as outras garotas continuam seus preparativos."
    "..."
    "Linne já parece estar pronta, mas ainda há tempo até nosso compromisso..."
    "Que estranho."

    menu(nvl=True):
        "Falar com Linne":
            m "Linne, que horas você levantou?"
            m "Parece estar acordada há horas."
            l "Ah, não, nem estou de pé há tanto tempo."
            l "E também já estou acostumada a acordar cedo."
            m "Nossa..."
            menu(nvl=True):                
                "Quanta determinação":
                    m "Você parece tão disposta, Linne."
                    m "Admiro que consiga acordar tão cedo e ainda estar com um sorriso no rosto!"
                    l "Ha, ha... Agora fiquei até sem graça."
                    l "Mas muito obrigada, Moon!"
                    "Ela está realmente contente."
                    $ linne += 1
                    l "Enfim... Não é melhor você se aprontar?"
                    m "Ah! Sim, é verdade!"
                    m "Nos encontramos mais tarde!"
                "Ainda é muito cedo":
                    m "Mas... Ainda há muito tempo até às 8:00."
                    m "Precisava mesmo estar pronta com tanta antecedência?"
                    l "Hmm." 
                    l "Não gosto de deixar as coisas pra última hora."
                    "Não sei se isso responde minha pergunta..."
                    m "Bom... Vou voltar a me preparar."
                    l "Até logo."

        "Continuar minhas tarefas":
            "Bom, é melhor me apressar."
            l "Moonie?"
            "Linne chama meu nome assim que viro as costas."
            "Percebo que todas as outras já se foram."
            l "Boa sorte hoje."

    #jump end

label cap1_2:
    "Dado 8:30, estávamos todas presentes no pátio."
    "O apresentador e a equipe de produção se preparava para a gravação."
    Sr "Começamos em alguns instantes!"
    Sr "E não se preocupem! Dessa vez não será ao vivo."
    "Mas... Essa demora está me deixando ansiosa."
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
    n "Ah..."
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
    # apos o treino, as personagens podem descansar
    "Ufa! Finalmente acabou!"
    "Estou livre para descansar."
    "Pelo menos até o evento."

    if reconh:
        "???"
        "Escuto alguém se aproximar de mim."
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
        "Ela se vira rapidemente e vai embora."
        m "Foi um prazer!"
        "Acho que ela nem escutou..."

    else:
        #aq acontece a escolha entre passar o tempo sozinha
            #passar o tempo sozinha faz moon refletir e chegar a novos julgamentos
            #(talvez n seja uma boa hr pra isso)
        #ou conversar com roko
            #ao conversar, ficamos sabendo mais sobre roko(estilo de vida, opinioes etc.)
            #temos a oportunidade de aumentar a amizade com ela
        "Enquanto passava pelo jardim, encontro Roko observando as flores."
        "Seria uma boa ideia conversar com ela?"
        menu(nvl=True):
            "Sim":
                "Me aproximo para conversar com ela."
                m "Roko!"
                r "AAAH!"
                r "Pelos céus! Você me assustou!"
                r "Onde estão seus modos??!"
                m "Ah, me desculpa."
                m "Não foi minha inteção..."
                r "Hump!"
                r "O que quer comigo, afinal?"
                m "Eh..."
                m "Só queria perguntar como foi a sua performance..."
                r "Ah, sobre isso..."
                r "Foi ótima, se quer saber a minha opinião."
                r "Parece até que nasci pra isso."
                m "Caramba!"
                m "Fiquei palavras diante de tanta confiança."
                r "Isso acontece com os menos afortunados, de fato."
                "Oh..."
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
                        m "E prejudincando tanto a si mesma quanto os outros a sua volta."
                        r "Prejudicando?"
                        r "Não, não... Você entendeu errado."
                        r "Ahf... Não vou discutir."
                        r "Você não entenderia de qualquer forma..."
                        "Acho que VOCÊ não entenderia de qualquer forma."


                    "Tem razão.":
                        m "Faz sentido..."
                        m "Acho tem razão!"
                        r "Tenho, sim!"
                        r "Viu? Foi assim que te convenci."
                        r "Se você acredita em algo fielmente"
                        r "As outras pessoas vão acreditar também!"
                        "UAU!"
                        $ roko += 1

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
                r "Ele quanse nunca me responde."
                r "Mas eu sei que ele me escuta com atenção."
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
                r "Fiquei tão frustrada! Joguei o sanduiche de volta no prato e subi chorando para meu quarto."
                r "Eca! só de lembrar daquele gosto horrivel na minha boca..."
                "Ela cobre a boca como se esivesse prestes a vomitar."
                r "..."
                r "Pensando agora..."
                # Inventar nome pro veio
                r "O senhor jardineiro deve ter ficado deveras decepcionado..."
                menu(nvl=True):
                    "E com razão!":
                        m "Com certeza!"
                        m "Isso foi péssimo da sua parte!"
                        r "E você queria que eu fizesse o que?"
                        r "Fingir que gostei!?"
                        m "Não! Mas você poderia pelo menos agradecer"
                        m "Era literalmente o mínimo!"
                        "Ela bufa, irritada."
                        r "Urhg! Você é muito ignorante!"
                        r "Você e aquela Nádia!"
                        $ ignorante = True

                    "Talvez ...":
                        m "Olha..."
                        m "Talvez o que importasse, no final, não era o sabor do sanduíche."
                        m "Mas sim a experiência do processo!"
                        m "Você mesma disse que não tinha gostado da ideia."
                        m "E mesmo assim aceitou participar"
                        m "Tenho certeza de que ele deve ter ficado contente por isso."
                        r "Acha isso mesmo... ?"
                        r "Bem... Deve estar certa..."
                        r "Afinal, você se parece bastante com ele."
                        $ roko += 5

label cap1_4:
    # inicio do evento
    # Determinar local do acontecimento(fiquei em duvida)

    "Ao chegarmos ao local"
    "Observamos que estão dispostas mesas, utensílios de coxinha e vários ingredientes."
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
    Sr "O resultado aparecerá no telão logo atras de nós."
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
    "No telão, aparecem meu nome e o de Nádia."
    Sr "Ah, Moonie e Nádia! Uma dupla promisora!"
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
    "Nádia susurra sarcasticamente."
    n "Nossah, mas que surpresah."
    r "E-eu??"
    r "Não, não. Deve haver algun engano!"
    Sr "Não há enganos neste reality, querida!"
    Sr "Pode ficar tranquila."
    "Ele diz isso com um sorriso ironico no rosto, expressando exatamente o oposto."
    Sr "Roko escolherá um prato e as equipes terão 45 minutos para prepará-la."
    Sr "Ah, e não haverá acrécimo de tempo."
    Sr "jurada Roko! Qual será o prato desta noite?"
    r "Hãh..."
    "Consigo ver desespero e angustia nos olhos dela."
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
        "Ela espira fundo e se acalma."

    n "Nesse caso..."
    n "Podemos preparar um espaguete ao molho branco."
    n "Você prepara a massa enquanto eu faço o molho."
    m "Pode ser!"
    "Coletamos os ingredientes e materiais e começamos a trabalhar."
    "Enquanto espero o macarrão cozinhar, observo Nádia fazer sua parte."
    "Ela é rápida e confiante em seus movimentos."
    "Chega até a cantarolar uma música."
    m "Você parece bem confortável."
    n "Ah! Eu?"
    n "É que na verdade já estou acostumada, sabe."
    n "Minha família tem um restaurante"
    n "e eu costumava ajudar na cozinha."
    m "É sério!? Caramba, que legal!"
    n "Na verdade, não era tão legal assim."
    n "Tinha muita dor de cabeça..."
    n "E ainda tem."
    n "Com o tempo as coisas pioraram."
    m "Ah..."
    # dialogo caso ignorante=True

    n "Hmm... Acho que vou adicionar alguns brócolis."
    n "Tô achando a receita meio sem graça."
    Sr "O tempo está se esgotando, meninas!"
    m "Vamos ter que nos apressar."

    # entrega dos pratos
    Sr "Tempo esgotado!"
    Sr "Equipe 1, apresentem seus pratos por gentileza."
    "Levamos nosso prato ao balcão de Roko."
    #Sr "Começando por Moonie e Nádia."
    Sr "O que prepararam?"
    m "Fizemos um delicioso espaguete ao molho branco."
    n "Com Brócolis."
    "Roko se esforça para não fazer cara de nojo mais uma vez."
    Sr "Pode provar, jurada."
    "Ela empurra os brócolis pra um canto do prato com o garfo."
    "E prova a massa com molho."
    r "Hmm..."
    r "Até que não está ruim..."
    r "Eu daria um 8..."
    Sr "8 é uma boa nota!"
    r "Mas como tem brócolis a minha nota final é 5!"
    Sr "!!!"
    "Ah não, não pode ser..."
    "Como ela tem a audacia!?"
    "Olho para o lado e vejo Nádia com uma expressão vazia."
    "Mas sinto o ódio crescente nela."
    Sr "Ehr..."
    "Até mesmo o Sr.Star parece indignado."
    Sr "Neste caso... 5 é a nota final!"
    Sr "He he..."
    "Ele ri meio sem graça."
    Sr "Podem ir, meninas. Vocês fizeram um ótimo trabalho!"
    Sr "Equipe 2, por favor, apresente-se!"
    "As meninas da equipe 2 dispoe seu prato sobre o balcão de Roko."
    "Roko arregala os olhos ao observar o macarrão coberto de molho de tomate."

    if (vermelho):
        "Nádia susurra ao meu lado."
        n "Parece que a Carminha Frufru se deu mal..."
        m "Tudo o que vai... volta."
        
    Sr "Uhh! Parece muito bom!"
    Sr "Podem dizer do que se trata?"
    l "Temos aqui o clássico e muito amado espaguete com almondegas."
    r "E... molho de tomate...?"
    j "Sim! foi temperado com um ingrediente secreto especial meu!"
    "Juni parece orgulhosa sobre isso."
    
    if (vermelho):
        "Mal ela sabe..."

    r "... Tenho mesmo que comer isso?"
    Sr "Para dar uma nota, você precisa primeiro provar."
    r "Ok..."
    "Ela hesita em provar por algum tempo."
    Sr "Apresse-se! O prato vai esfriar!"
    "Depois de muito esforço mental, ela leva o garfo a boca."
    r "..."
    "Ela mastiga devadar..."
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
    "Nesse momento, Roko finalmete consegue engolir."
    r "Arhg!"
    r "Não precisa, eu estou bem..."
    Sr "Ufa!"
    "Todos parecem bem mais aliviados."
    Sr "A senhorita realmente nos preocupou..."
    Sr "Gostaria de uma palsa para respirar, srta. Roko?"
    r "Não, não."
    r "Isso já foi o suficiente pra minha decisão final."
    "O clima se torna mais tenso após suas palavras."
    Sr "Bem... Então..."
    # muda para feicao confiante
    Sr "Diga-nos a sua escolha!"
    r "Dadas as circunstâncias..."
    r "Minha nota para a equipe 2 é..."
    "A produção coloca uma música de tensão."

    r "5.1!"
    "!!!"
    "O-o que...?"
    "Todos permanecem em choque por uns istantes."
    j "5-5.1??"
    "Juni se vira para Linne, ainda em choque."
    j "Então nós..."
    l "Vencemos?!"
    Sr "Ha Ha, sim!"
    Sr "As vencedoras são Linne e Juni!"
    Sr "Meus parabéns, meninas!"
    "Confetes são lançados ao ar em comemoração."
    # elaborar comemoracao

    n "Espera aí um istante..."
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
    n "Escuta aqui o sua-"
    l "Calma, Nádia. Não há motivos para ficar irritada."
    l "É só uma brincadeira..."
    #Sr "Exatamente. Vocês não sairam prejudicadas."
    n "Grrr!"
    "Ela vira as costas e sai batendo os pés."

    # opcao de escolha?
    "É melhor eu conversar com ela."
    m "Nádia, espera!"
    "Corro atrás dela enquanto Sr.Star encerra o evento."
    "Já estamos na metado do caminho para os dormitórios quando finalmente a alcanço."
    n "Argh! O que foi agora?!"
    n "Será que não posso ter um minuto de paz!??"

    menu(nvl=True):
        "Você não devia reagir assim":
            m "Sei que está zangada, mas..."
            m "Explodir daquela forma na frente de todos é loucura!"
            n "Isso... não é algo fácil de controlar e você sabe disso!"
            n "Afinal, aquilo foi muito pessoal..."
            m "..."
            m "Mas se você continuar assim..."
            m "Quem sairá prejudicada será você!"
            n "... Não preciso da sua preocupação."

        "Há algo de errado no julgamento.":
            m "Acredito que você também tenha percebido..."
            m "Pela forma que Roko fez o julgamento..."
            m "Ela-"
            n "Tem algo pessoal contra nós? Sim. Eu percebi!"
            n "Porque não se manifestou naquela hora? Você também fazia parte da equipe."
            m "..."
            m "Bom... Tenho certeza de que ela colherá o que plantou."
            $roko -= 5

    "Solto um longo suspiro."
    m "É melhor esquecermos isso."

    "Ouço as outras garotas chegando a nós."
    r "Ora se não é a pavio curto e compania!"
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
    n "Cansei dessa conversa furada!"
    n "Tô indo pro meu quarto. Uma boa noite pra vocês."

    # final da discussao

label cap1_5:

    # a sequencia de dias a seguir servem apenas p/ treinamento e pequenas conversas com as personagens
    # lembrando que roko nunca se interessa por treinar muito

    # dia 2

    # dia 3

    # Final do dia 3
    "Acho que vou encerrar os treinos de hoje."
    "Amanhã já é a nossa primeira apresentaçaõ oficial..."
    "Ah, que emoção!"
    "Devo treinar mais um pouco para garantir?"
    "Não, não posso pensar assim!"
    "Fiz tudo o que podia..."
    "Eu acho."

    # dia da apresentacao

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
            $linne += 3
            $karma += 5

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
    Sr "As nossas queridas participantes serão avaliádas de acordo com seus devidos desempenhos."
    Sr "Aquela que ficar em último no ranking..."
    Sr "Será, infeizmente, desqualificada do reality."
    # bla bla bla
    Sr "Começaremos com a promissora Moonie!"
    "Eu!!"
    # Minigame

    "Aplausos soam ao final da apresentação."
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
    j "B-boa sorte."
    "Após o que parece ser uma eternidade, o ranking aparece no telão."
    Sr ""







            






    
