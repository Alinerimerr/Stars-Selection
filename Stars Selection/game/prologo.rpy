label prologo1_i:
  
    #show palco at truecenter:
    #    zoom 2
    #with dissolve"""
    "Som, som, testando… E-hem…"
    Sr "Boa noite, senhoras e senhores telespectadores!"
    Sr "Agradeço sua sublime companhia que nos permite estar neste palco tão acolhedor."
    "{i}Eu estou tão nervosa. Não acredito que isso realmente tá acontecendo…{/i}"
    Sr "Eu sou o Sr. Star e este é o primeiro episódio de {i}STAR'S SELECTION!{/i}"
    Sr "A partir de uma avaliação prévia, foram escolhidas cinco trainees com potencial para debutar."
    Sr "No entanto, apenas uma delas irá ser capaz de superar e mostrar ao mundo suas habilidades!"
    #mudar para sorriso arrogante
    Sr "Agora, eu sei que vocês devem estar curiosos para conhecer elas… Hehe, eu também estou!"
    Sr "Então vamos conferir as nossas candidatas!"
    Sr "Começando por..."
    Sr "Srta. Linnie!"
    Sr "Com suas habilidades excepcionais de canto e visuais incríveis, mesmo tão jovem, é definitivamente um charme para os fãs!"
    Sr "Srta. Linne, gostaria de compartilhar algo sobre suas expectativas com o programa?"
    #colocar piscadinha
    l "Primeiramente, boa noite a todos!"
    #colocar sorriso falso
    l "Gostaria de agradecer a todos os fãs que me deram a oportunidade de estar aqui, sem seu apoio eu não seria capaz de ir tão longe!"
    l "Eu prometo que não irei decepcionar vocês!"
    #colocar hiperreação do Sr Star
    Sr "Ahhhh! Como ela é encantadora, muito obrigado pelas suas palavras!"
    Sr "Sente-se aqui, por favor."
    l "Obrigada."
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
    Sr "Olá, querida!"
    #o sr star faz cara de confuso
    Sr "Perdoe-me pela deselegância, se me cabe a pergunta, mas o que traz você aqui?"
    r "Oh, Sr. Star, sinto que devo correr atrás dos meus sonhos, devo viver o mundo eu mesma!"
    #faz cara de drama
    r "Sei que muitos acreditam que a influência da minha família me garante um futuro, mas não é assim! Eu tenho que conquistá-lo por conta própria!"
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
    "Caramba, que sem noção...!"
    Sr "Oh, minhas sinceras desculpas, senhorita..."
    Sr "Não era minha intenção deixá-la interrompe-la dessa forma."
    Sr "Então... A senhorita é nova na área e já ouvi que tem talento."
    Sr "Porém, o público anseia por mais sobre você!"
    Sr "Não gostaria de dizer algo mais sobre... Por exemplo, as suas motivações?"
    
label prologo1_m:
    "Essa pode ser a minha chance de impressionar o apresentador e o público."
    "O que devo dizer? Qual é a minha maior motivação?"

    menu(nvl=True):
        "Minha família.":
            # a protagonista sente q precisa vencer como forma de agradecimento a td o q a familia fez por ela
            m "Devo tudo o que tenho e tudo o que conquistei à minha família..."
            m "Eles investiram tanto no meu sonho de me tornar uma idol... Agora, o mínimo que posso fazer em retribuição é vencer!"
            m "Para que se orgulhem de mim e vejam o valor de todo esse esforço."
            Sr "Ah sim, sim! Retribuir o investimento é importante para alguns."
            Sr "Entretanto, espero que não pense demais na possibilidade contrária ao sucesso, sua determinação será sua maior aliada, não é mesmo?"
            m "Hmm... S-sim... Ma-"
            Sr "Pois bem, mantenha isso em mente para tentar sua vitória! Ha, Ha!"
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
            "Acho que consegui impressionar o Sr.Star! Talvez ele tenha se identificado..."
            "Mas não tenho tanta certeza quanto aos espectadores. Nem todos lidam muito bem com sinceridade..."
            $ fama = True

        "Ser uma pessoa querida e reconhecida.":
            # a protagonista deseja a fama para ajudar pessoas por meio de sua arte
            # (ex.: produzir musicas p/ pessoas se identificarem e se sentir melhor)
            m "Quero poder fazer a diferença na vida das pessoas."
            m "Servir de inspiração para meus fãs quando eles mais precisarem."
            m "Por meio da arte, podemos nos conectar uns com os outros."
            m "Assim, saberemos que não estamos sozinhos."
            Sr "Essas... são belas palavras, realmente."
            sr "Espero que não esteja dizendo isso apenas para ganhar o público, querida!"
            m "Eu nunc-"
            $ reconh = True

        "Fazer aquilo que eu gosto.":
            # a protagonista deseja fazer aquilo que sempre sonhou, música, dança e apresentar-se
            # (ex.: produzir musicas, letras, stages grandes, etc...)
            m "Quero fazer."
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
    #Sr "Quem sairá vitoriosa?? É o que vamos descobrir nos próximos episódios!"
    Sr "Muito obrigada pela audiência e até a próxima!"

label prologo2:
    # Cena apos apresentacao
    # As participantes conversam entre si

    # o jogador pode ou nao falar com as personagens

    "Após a apresentação, todas as participantes se reuniram nos bastidores"
    "Elas estão conversando... devo me juntar a elas?"

    
    menu (nvl=True):
        "Se juntar a conversa":
            # aqui temos a primeira interacao com as personagens
            "Tomo coragem na cara e me aproximo do grupo."
            l "Foi uma ótima apresentação, meninas!"
            l "Na minha opinião, todas se saíram muito bem."
            "As garotas parecem mais empolgadas depois da fala de Linne."
            "Com exceção ção de Nádia, que parece indiferente."
            j "Ah, muito obrigada, Linne <3"
            j "Você também foi maravilhosa, ti-tipo... "
            j "Fez parecer super fácil e... e natural."
            r "Não sou de ficar elogiando muito."
            r "Mas, a senhorita é uma verdadeira Diva!"
            "Nádia, agora de cara fechada, revira os olhos e se afasta."
            "O que será que ela tem?"
            menu(nvl=True):
                "Perguntar qual o problema.":
                    "Chego perto o suficiente e pergunto baixinho para que apenas Nádia escute."
                    m "O que foi, Nádia? Algum problema?"
                    n "Argh! Essas garotas são mesmo umas puxa-saco, não?"
                    "Ela cochicha num tom mais baixo que eu, mas há intensidade em suas palavras."
                    n "Tem gente que não entende que ela estava apenas mantendo as aparências..."
                    #n "Como muito s"
                    menu(nvl=True):
                        "Concordar com Nádia":
                            m "Nossa, com certeza! Ela não me pareceu nada natural."
                            "Ela sorri em um tom de aprovação."
                            n "Que Bom que alguém concorda."
                            $ nadia += 1
                            "pt: [nadia]"
                        "Discordar":
                            m "Na verdade..."
                            m "Acho que você está sendo um pouco dura demais."
                            m "Não há nada de errado em trocar elogios."
                            n "Eh... Realmente."
                            "Sinto um forte deboche aqui."
        
                "Não dizer nada.":
                    "É melhor não mexer com quem tá quieto, né?"
            

        "Näo falar com ninguém":

            "Ta maluco vo eh dormi kkkkk"
            "Brincadeira, hehe"
            "Acho... que vou ficar na minha mesmo."

    
    "A equipe de produção se aproxima e intervém."
    "O diretor explica que, basicamente, todas as nossas atividades serão gravadas para o programa."
    "Inclusive algumas partes do dormitório, como cozinha, quartos e sala de estar."
    "Não precisaremos dividir os quartos e nem nos preocupar em preparar nossas refeições."
    "Logo após isso, a equipe nos conduz ao nosso dormitório."
    "Ao chegarmos, analisamos o local em conjunto."
    # aq pode ter uma descrição do ambiente, mas no momento to sem ideias

    # achei melhor a protagonista ter uma opinião propria aq
    "Apesar de simples, achei o espaço até que bem agradável."
    r "Ah... Eh aqui que nós todas vamos ficar?"
    "Roko olha ao redor com uma expressão... meio enojada."
    l "Hora, Roko! Não faça essa cara!"
    l "A equipe deu tudo para que o ambiente fosse o melhor possível!"
    l "É muito rude da sua parte fic-"
    n "Oia só!"
    n "Não vamos precisar dividir os quartos!"
    l "Uh... Sim??"
    l "Já fomos notificadas sobre isso anteriormente, Nádia!"
    n "Ohh..."
    n "Acho que não estava prestando atenção nessa hora."
    "Linne retorce levemente a boca e seu olhar se torna mais afiado."
    #"Por um momento, ela pareceu bem irritada"
    j "A decoração também é muito bem elaborada..."
    j "Eu achei uma graça!"
    n "A cozinha parece ótima também..."
    n "Será que podemos fazer alguma coisa aqui?"
    m "Ninguém disse que não podíamos, né?"
    n "É verdade!"
    n "Han... Como se chama mesmo?"
    n "Luna ou algo do tipo, né?"
    "Como... Como ela errou completamente o nome?"
    m "É moonie, na verdade."
    m "Mas podem me chamar de Moon se quiserem."
    n "Tudo bem, Moon."
    n "Podemos preparar um banquete com o que temos aqui!"
    n "O que acha?"

    menu(nvl=True):
        "Parece uma boa ideia":
            m "Claro! Seria muito legal!"

        "Parece uma péssima ideia":
            m "Não acho que estamos aqui pra isso..."

    r "De qualquer forma..."
    "Seu tom de voz se torna mais agressivo."
    r "Não irei ingerir nada que as senhoritas preparem."  
    "Todas param para encarar Roko."
    "E um silêncio julgador recai sobre nós."
    r "Ah sinto muito se as ofendi"
    r "Mas eu costumo comer apenas pratos profissionais"
    r "Então não posso correr riscos, endentem?"
    n "Humph! Essa daí tá achando que a gente vai intoxicar ela."
    "Ela diz isso mais para si mesma do que para todas em geral."
    j "Uhg... bem..."
    j "Melhor nós descansarmos agora."
    j "Hoje foi um dia cheio e amanhã temos muito o que fazer."
    m "Devo admitir  que estou bem cansada, também."
    m "Vou terminar de me instalar por aqui e ir dormir."
    m "Boa noite, meninas <3"

label fimprologo:

    # aq moonie esta em seu quarto p refletir e descansar
    "..."
    "Finalmente, tenho um momento a sós no meu quarto."
    "Aahf"
    "Tenho muito o que processar."
    # ela formula opinioes sobre as personagens e contextos

    jump cap1_1


