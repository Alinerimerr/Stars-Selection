label prologo1_i:
  
    #show palco at truecenter:
    #    zoom 2
    #with dissolve"""
    "Som, som, testando… E-hem…"
    Sr "Boa noite, senhoras e senhores telespectadores!"
    Sr "Agradeço sua sublime companhia que nos permite estar neste palco tão acolhedor"
    "{i}Eu estou tão nervosa.{/i}"
    "{i}Não acredito que isso realmente tá acontecendo…{/i}"
    Sr "Eu sou o Sr. Star e este é o primeiro episódio de {i}STAR'S SELECTION!{/i}"
    Sr "A partir de uma avaliação prévia"
    Sr "haverão cinco trainees com potencial para debutar."
    Sr "No entanto, apenas uma delas irá ser capaz de superar e mostrar ao mundo suas habilidades!"
    #mudar para sorriso arrogante
    Sr "Agora, eu sei que vocês devem estar curiosos para conhecer elas…"
    Sr "Hehe, eu também estou!"
    Sr "Então vamos conferir as nossas candidatas!"
    Sr "Começando por..."
    Sr "Srta. Linnie!"
    Sr "Com suas habilidades excepcionais de canto e visuais incríveis"
    Sr "Mesmo tão jovem, é definitivamente um charme para os fãs!"
    Sr "Gostaria de compartilhar algo sobre suas expectativas?"
    #colocar piscadinha
    l "Primeiramente, boa noite a todos!"
    #colocar sorriso falso
    l "Gostaria de agradecer a todos que me deram a oportunidade de estar aqui."
    l "Sem seu apoio eu não seria capaz de ir tão longe!"
    l "Eu prometo que não irei decepcionar vocês!"
    #colocar hiperreação do Sr Star
    Sr "Ahhhh! Como ela é encantadora, muito obrigado pelas suas palavras!"
    Sr "Sente-se aqui, por favor."
    Sr "Agora, nossa próxima candidata."
    # Luzes apontam para Nadia
    Sr "Eu lhes apresento: Srta. Nadia!"
    n "Olá, mundo! Preparem-se pois eu vou com tudo!"
    Sr "Caramba, e que baita personalidade…"
    #risadas programadas do público
    Sr "Mas o que é um reality sem um pouco de encrenca, não é mesmo? Hehehe"
    n "Como é?!"
    #ela parece incomodada
    Sr "Nada, minha querida! Era só brincadeira!"
    Sr "Fique à vontade para falar com o público."
    Sr "Mas cuidado com o que diz, senhorita, pois todos estão ouvindo!"
    n "Humpf! Muito bem..."
    #ela olha para a câmera
    n "Sei que poucas pessoas me conhecem e esta será sua primeira impressão de mim..."
    #olhar determinado
    n "Mas eu quero deixar claro quem eu sou e que não me deixarei perder pelo caminho."
    n "Esta é uma grande oportunidade e eu não vou desperdiçá-la. Irei lutar até o fim!"
    #falso sorriso do sr star
    Sr "Quanta determinação! É assim que se fala, Nadia! Agora, pode se dirigir ao seu assento."
    Sr "A nossa próxima convidada ganhou o olhar dos nossos jurados à primeira vista, uma pérola rara!"
    Sr "Apresento-lhes: Srta. Junnie!"
    #junnie tímida
    j "O-Olá, pessoal…!"
    Sr "Vamos lá, não seja tímida, certamente há muito que você queira dizer."
    j "Certo, bem… Meu nome é Junnie e e-eu realmente quero conseguir debutar…"
    j "Conto com o apoio de todos vocês!"
    Sr "Obrigada, querida, espero que possamos vê-la evoluir na sua timidez…"
    Sr "A próxima candidata tem um nome relativamente conhecido…"
    Sr "Não para a indústria da música muito embora, e sim para a de cosméticos!"
    Sr "Com vocês, Srta. Roko!"  
    r "Boa noite, Sr. Star! Boa noite, todo mundo!"
    Sr "Olá, querida! Há muito tempo que não vejo seu rosto por aqui."
    #o sr star faz cara de confuso
    Sr "Perdoe-me pela deselegância, se me cabe a pergunta, mas o que traz você aqui?"
    r "Oh, Sr. Star, sinto que devo correr atrás dos meus sonhos, devo viver o mundo eu mesma!"
    #faz cara de drama
    r "Sei que muitos acreditam que a influência da minha família me garante um futuro"
    r "porém, não é assim!"
    r "Eu tenho que conquistá-lo por conta própria!"
    r "Portanto, estou aqui para provar meu valor."
    #Sr. star faz cara de choro
    Sr "Oh, meu Deus, que comovente! Seja bem-vinda para mostrar seu talento…"
    Sr "Bem, o show deve continuar…"
    Sr "Por último mas não menos importante,"
    "{i}É minha vez, é agora ou nunca…{/i}"
    Sr "Um rosto novo nas câmeras, com um potencial de desenvolvimento em todas as habilidades!"
    Sr "Aqui vem Srta. Moonie!"
    "Sou eu!"

    m "Boa noite, pessoal! Estou muito feliz de estar aqu-"
    Sr "E quem não estaria? Ha ha ha!"
    Sr "Brincadeira, querida!"
    m "Hah..."
    "Caramba! que sem noção...!"
    Sr "Oh, minhas sinceras desculpas, senhorita!"
    Sr "Não era minha intenção interrompe-la dessa forma."
    Sr "Então... A senhorita é nova na área e já ouvi que tem talento."
    Sr "Porém, o público anseia por mais sobre você!"
    Sr "Não gostaria de dizer algo mais sobre... Por exemplo, as suas motivações?"
    
label prologo1_m:
    "Essa pode ser a minha chance de impressionar o apresentador."
    "O que devo dizer? Qual é a minha maior motivação?"

    menu(nvl=True):
        "Minha família.":
            # a protagonista sente q precisa vencer como forma de agradecimento a td o q a familia fez por ela
            m "Devo tudo o que tenho e tudo o que conquistei à minha família..."
            m "Eles investiram tanto no meu sonho de me tornar uma idol... Agora, o mínimo que posso fazer em retribuição é vencer!"
            m "Para que se orgulhem de mim e vejam o valor de todo esse esforço."
            Sr "Ah sim, sim! Retribuir o investimento é importante para alguns."
            Sr "Mas, se me permite dizer..."
            Sr "Acredito que fracassar a essa altura os deixaria bem decepcionados, não?"
            m "Hmm... S-sim... Ma-"
            Sr "Pois bem, mantenha isso em mente para tentar sua vitória! Ha, ha!"
            "É a segunda vez que ele me corta."
            "Talvez, a minha resposta não o tenha agradado..."
            $ familia = True
            
        "Fama e luxo.":
            # a protagonista deseja a vitoria pelo prazer de estar nos holofotes e receber muito bem
            m "Desde garotinha... Sempre aspirei para que o mundo soubesse meu nome."
            m "Nasci para brilhar nos palcos e nas capas das maiores revistas!"
            m "Ainda serei a Idol mais bem-sucedida da atualidade, e este é apenas o primeiro passo."
            Sr "Minha nossa! Quanta ambição, senhorita."
            Sr "Nunca, em tantos anos de minha carreira, presenciei ninguém que teve a coragem de dizer isso para o público."
            Sr "Ainda mais em um grande programa como este, senhoras e senhores!"
            Sr "Admiro a sua boa honestidade e sede de fama, querida Monnie."
            Sr "Vejo que chegará longe!"
            "Consegui impressionar o Sr.Star!"
            "Nem foi tão complicado quanto imaginei... Talvez ele tenha se identificado."
            $ fama = True

        "Fazer aquilo que eu gosto.":
            # a protagonista deseja fazer aquilo que sempre sonhou, música, dança e apresentar-se
            # (ex.: produzir musicas, letras, stages grandes, etc...)
            m "Simplesmente quero fazer aquilo que gosto."
            m "A música é uma parte muito importante da minha vida."
            m "Então, performar aquilo que treinei por tanto tempo, trata-se de um sonho realizado."
            m "Quero compartilhar com o mundo esta parte de mim."
            Sr "Oh! A juventude e a paixão destemida!"
            Sr "Espero que não esteja dizendo isso apenas para ganhar o público, querida!"
            m "O que-"
            $ reconh = True

        "Inspirar as pessoas.":
            # a protagonista quer ajudar as pessoas e inspirar
            # (ex.: produzir musicas, letras, stages grandes, etc...)
            m "Quero fazer algo que as pessoas possam se identificar."
            m "Seja pela música, os sentimentos contidos nas letras, na dança, e no palco."
            m "Servir de inspiração para meus fãs quando eles mais precisarem."
            m "Por meio da arte, podemos nos conectar uns com os outros."
            m "Assim, saberemos que não estamos sozinhos."
            Sr "Essas... são belas palavras, realmente."
            Sr "Espero que não esteja dizendo isso apenas para ganhar o público, querida!"
            m "Eu nunc-"
            $ reconh = True
   
    Sr "Muito bem, assim se encerra a nossa apresentação dessas promissoras estrelas!"
    if reconh:
        "Lá vai ele de novo... Já consigo ver os cortes na transmissão colocados em vídeos frustrados de fãs..."
    Sr "Amanhã estaremos de volta para esclarecer o funcionamento do programa"
    Sr "E para apresentar a primeira performance!"
    #Sr "Quem sairá vitoriosa? É o que vamos descobrir nos próximos episódios!"
    Sr "Muito obrigado por fazer parte da nossa audiência e até a próxima!"

label prologo2:
    # Cena apos apresentacao
    # As participantes conversam entre si

    # o jogador pode ou nao falar com as personagens

    "Após a apresentação, fomos todas reunidas nos bastidores."
    "Elas estão conversando... devo me juntar a elas?"

    
    menu (nvl=True):
        "Se juntar a conversa":
            # aqui temos a primeira interacao com as personagens
            "Respiro fundo, tomo coragem e me aproximo do grupo."
            l "Foi uma ótima apresentação, meninas!"
            l "Na minha opinião, todas se saíram muito bem."
            "As garotas parecem mais empolgadas depois da fala de Linne."
            "Com exceção de Nádia, que parece indiferente."
            j "Ah, muito obrigada, Linne."
            j "Você também foi maravilhosa."
            j "Fez parecer super fácil e..."
            j "Natural..."
            r "Não sou de ficar elogiando muito."
            r "Mas... Devo admitir que fiquei impressionada."
            "Nádia revira os olhos."
            "O que será que ela tem?"
            menu(nvl=True):
                "Perguntar qual o problema.":
                    m "... Algum problema?"
                    "Pergunto baixo para que apenas Nádia escute."
                    n "Não é nada, não."                                  
                    menu(nvl=True):
                        "Insistir.":
                            m "Tem certeza?"
                            m "Você não parece muito-"
                            n "Quer parar de me encher!"
                            n "..."
                            n "Com todo respeito."
                            $ nadia -= 1
                        "Não insistir.":
                            m "..."
                            n "É só que..."
                            n "Isso é tão irritante."
                            m "Irritante?"
                            n "Ah, desculpa."
                            n "Eu só... pensei alto."
                            m "Entendi..."
        
                "Não perguntar.":
                    "Ela não parece aberta para conversar..."
            

        "Não falar com ninguém":

            #"Tá maluco vo eh dormi kkkkk"
            #"Brincadeira, hehe"
            "Acho... que vou ficar na minha mesmo."
            "Escuto Linne, Juni e Roko trocarem elogios."
            "Enquanto Nádia permanece calada."
            "E levemente irritada também."
            "Após algum tempo, sua atenção se volta para mim."
            n "..."
            "Devo dizer algo para ela?"
            menu(nvl=True):
                "Tentar puxar assunto":
                    m "Er..."
                    m "Seu nome é Nádia, não?"
                    m "É um prazer te conhecer."
                    n "Oh, o prazer é todo meu."
                "Não dizer nada":
                    m "..."
                    n "Entendi..."
                    n "Você não é muito de conversar, né?"
            "Isso atrai a atenção das outras."
            n "Não se preocupe, eu não mordo a menos que necessário, he, he."
            l "Certo, junte-se a nós, estaremos convivendo por bastante tempo, não?"
            m "Obrigada, espero que nos demos bem."
            r "Olh-"
    
    "O que quer que Roko fosse dizer, acabou sendo ignorado."
    "A conversa foi interrompida pela equipe de produção se aproximando e anunciando o próximo cronograma."
    "O diretor explica que, basicamente, todas as nossas atividades serão gravadas para o programa."
    "Inclusive algumas partes do dormitório, como cozinha, quartos e sala de estar."
    "Não precisaremos dividir os quartos e nem nos preocupar em preparar nossas refeições."
    "Logo após isso, a equipe nos conduz ao nosso dormitório."
    "Ao chegarmos, analisamos o local em conjunto."
    # aq pode ter uma descrição do ambiente

    # achei melhor a protagonista ter uma opinião propria aq
    "Apesar de simples, achei o espaço até que bem agradável."
    r "Ah... Eh aqui que nós todas vamos ficar?"
    "Roko olha ao redor com uma expressão meio... enojada."
    l "Ora, Roko! Não faça essa cara!"
    l "A equipe deu tudo para que o ambiente fosse o melhor possível!"
    l "É muito rude da sua parte exigir isso."
    n "Ainda bem que não vamos precisar dividir os quartos..."
    "Nádia sussurrou, mas não foi baixo o suficiente..."
    r "O que?!"
    l "Nádia, por favor, você também não!"
    "Linne retorce levemente a boca."
    "Por um momento, ela pareceu bem irritada"
    j "A decoração também é muito bem elaborada..."
    j "Eu achei uma graça!"
    n "A cozinha parece ótima também..."
    n "Será que podemos fazer alguma coisa aqui?"
    m "Ninguém disse que não podíamos, né?"
    n "É verdade!"
    n "Hmm... Como se chama mesmo?"
    n "Luna ou algo do tipo, né?"
    "Como... Como ela errou completamente o nome!?"
    m "É moonie, na verdade."
    m "Mas podem me chamar de Moon, se quiserem."
    n "Moon... Gostei!"
    j "Aaah! achei um apelido muito fofinho!"
    n "E é bem mais simples lembrar."   
    n "Bem, ia dizendo..."
    n "Podemos preparar um banquete com o que temos aqui!"
    n "O que acham?"

    menu(nvl=True):
        "Parece uma boa ideia":
            m "Claro! Seria muito legal!"

        "Não parece grande coisa.":
            m "Não acho que estamos aqui pra isso..."
            l "Exatamente!"
            l "Não vamos ter tempo para essas coisas."
            "Nádia suspira beeem alto."
            n "Que chato."

    r "De qualquer forma..."
    #"Seu tom de voz se torna mais agressivo."
    r "Não irei ingerir nada que as senhoritas preparem."  
    "Todas param para encarar Roko."
    "E um silêncio julgador recai sobre nós."
    r "Ah, sinto muito se as ofendi!"
    r "Mas eu costumo comer apenas pratos profissionais."
    r "Não posso correr riscos, endentem?"
    n "Nossah!"
    n "Com certeza estamos planejando te envenenar!"
    "Ela diz isso em um tom sarcástico e brincalhão."
    l "Não brinque com isso Nádia!"
    l "Este é um assunto sério."
    l "E roko..."
    l "Sei que deve estar sendo difícil para você..."
    l "Mas, sabe..."
    l "Não precisa nos ver como inimigas."
    l "Afinal, estamos nessa jornada juntas!"
    "Mesmo com o pequeno discurso de Linne"
    "O clima continua meio pesado."
    j "humm... bem..."
    j "Melhor nós descansarmos agora."
    j "Hoje foi um dia cheio e amanhã temos muito o que fazer."
    m "Devo admitir que estou bem cansada, também."
    m "Vou terminar de me instalar por aqui e ir dormir."
    m "Boa noite, meninas!"

label fimprologo:

    # aq moonie esta em seu quarto p refletir e descansar
    "..."
    "Finalmente, tenho um momento a sós no meu quarto."
    "Tenho muito o que processar..."
    # ela formula opinioes sobre as personagens e contextos

    "Bom... É melhor eu ir dormir."
    jump cap1_1


