label prologo1_i:
  
    #show palco at truecenter:
    #    zoom 2
    #with dissolve"""
    Srn "Som, som, testando… E-hem…"
    Srh "Boa noite, senhoras e senhores telespectadores!"
    Srn "Agradeço sua sublime companhia que nos permite estar neste palco tão acolhedor"
    p"{i}Eu estou tão nervosa.{/i}"
    p"{i}Não acredito que isso realmente tá acontecendo…{/i}"
    Srh "Eu sou o Sr. Star e este é o primeiro episódio de {i}STAR'S SELECTION!{/i}"
    Srn "A partir de uma avaliação prévia"
    Srn "haverão cinco trainees com potencial para debutar."
    Srsu "No entanto, apenas uma delas irá ser capaz de superar e mostrar ao mundo suas habilidades!"
    #mudar para sorriso arrogante
    
    Srn "Agora, eu sei que vocês devem estar curiosos para conhecer elas…"
    Srh "Hehe, eu também estou!"
    Srh "Então vamos conferir as nossas candidatas!"
    Srn "Começando por..."
    Srh "Srta. Linnie!"
    Srn "Com suas habilidades excepcionais de canto e visuais incríveis"
    Srn "Mesmo tão jovem, é definitivamente um charme para os fãs!"
    Srn "Gostaria de compartilhar algo sobre suas expectativas?"
    #colocar piscadinha
    lh "Primeiramente, boa noite a todos!"
    #colocar sorriso falso
    lh "Gostaria de agradecer a todos que me deram a oportunidade de estar aqui."
    ln "Sem seu apoio eu não seria capaz de ir tão longe!"
    lh "Eu prometo que não irei decepcionar vocês!"
    #colocar hiperreação do Sr Star
    Srsu "Ahhhh! Como ela é encantadora, muito obrigado pelas suas palavras!"
    Srn "Sente-se aqui, por favor."
    Srn "Agora, nossa próxima candidata."
    # Luzes apontam para Nadia
    Srn "Eu lhes apresento: Srta. Nadia!"
    nsm "Olá, mundo! Preparem-se pois eu vou com tudo!"
    Srsu "Caramba, e que baita personalidade…"
    #risadas programadas do público
    Srh "Mas o que é um reality sem um pouco de encrenca, não é mesmo? Hehehe"
    na "Como é?!"
    #ela parece incomodada
    Srh "Nada, minha querida! Era só brincadeira!"
    Srh "Fique à vontade para falar com o público."
    Srn "Mas cuidado com o que diz, senhorita, pois todos estão ouvindo!"
    nsr "Humpf! Muito bem..."
    #ela olha para a câmera
    nsm "Sei que poucas pessoas me conhecem e esta será sua primeira impressão de mim..."
    #olhar determinado
    nsr "Mas eu quero deixar claro quem eu sou e que não me deixarei perder pelo caminho."
    nsr "Esta é uma grande oportunidade e eu não vou desperdiçá-la. Irei lutar até o fim!"
    #falso sorriso do sr star
    Srsu "Quanta determinação! É assim que se fala, Nadia! Agora, pode se dirigir ao seu assento."
    Srn "A nossa próxima convidada ganhou o olhar dos nossos jurados à primeira vista, uma pérola rara!"
    Srh "Apresento-lhes: Srta. Junnie!"
    #junnie tímida
    jn "O-Olá, pessoal…!"
    Srn "Vamos lá, não seja tímida, certamente há muito que você queira dizer."
    jn "Certo, bem… Meu nome é Junnie e e-eu realmente quero conseguir debutar…"
    jn "Conto com o apoio de todos vocês!"
    Srn "Obrigada, querida, espero que possamos vê-la evoluir na sua timidez…"
    Srn "A próxima candidata tem um nome relativamente conhecido…"
    Srn "Não para a indústria da música muito embora, e sim para a de cosméticos!"
    Srn "Com vocês, Srta. Roko!"  
    rc "Boa noite, Sr. Star! Boa noite, todo mundo!"
    Src "Olá, querida! Há muito tempo que não vejo seu rosto por aqui."
    #o sr star faz cara de confuso
    Srsu "Perdoe-me pela deselegância, se me cabe a pergunta, mas o que traz você aqui?"
    rc "Oh, Sr. Star, sinto que devo correr atrás dos meus sonhos, devo viver o mundo eu mesma!"
    #faz cara de drama
    rn "Sei que muitos acreditam que a influência da minha família me garante um futuro"
    ra "porém, não é assim!"
    rc "Eu tenho que conquistá-lo por conta própria!"
    rc "Portanto, estou aqui para provar meu valor."
    #Sr. star faz cara de choro
    Srn "Oh, meu Deus, que comovente! Seja bem-vinda para mostrar seu talento…"
    Srh "Bem, o show deve continuar…"
    Srn "Por último mas não menos importante,"
    p"{i}É minha vez, é agora ou nunca…{/i}"
    Srn "Um rosto novo nas câmeras, com um potencial de desenvolvimento em todas as habilidades!"
    Srh "Aqui vem Srta. Moonie!"
    m "Sou eu!"

    m "Boa noite, pessoal! Estou muito feliz de estar aqu-"
    Srh "E quem não estaria? Ha ha ha!"
    Srn "Brincadeira, querida!"
    m "Hah..."
    p "{i}Caramba! que sem noção...!{/i}"
    Srsu "Oh, minhas sinceras desculpas, senhorita!"
    Srn "Não era minha intenção interrompe-la dessa forma."
    Srn "Então... A senhorita é nova na área e já ouvi que tem talento."
    Srn "Porém, o público anseia por mais sobre você!"
    Srn "Não gostaria de dizer algo mais sobre... Por exemplo, as suas motivações?"
    
label prologo1_m:
    p "{i}Essa pode ser a minha chance de impressionar o apresentador.{/i}"
    p "{i}O que devo dizer? Qual é a minha maior motivação?{/i}"

    menu(nvl=True):
        "Minha família.":
            # a protagonista sente q precisa vencer como forma de agradecimento a td o q a familia fez por ela
            m "Devo tudo o que tenho e tudo o que conquistei à minha família..."
            m "Eles investiram tanto no meu sonho de me tornar uma idol... Agora, o mínimo que posso fazer em retribuição é vencer!"
            m "Para que se orgulhem de mim e vejam o valor de todo esse esforço."
            Srh "Ah sim, sim! Retribuir o investimento é importante para alguns."
            Srn "Mas, se me permite dizer..."
            Sra "Acredito que fracassar a essa altura os deixaria bem decepcionados, não?"
            m "Hmm... S-sim... Ma-"
            Srh "Pois bem, mantenha isso em mente para tentar sua vitória! Ha, ha!"
            p "{i}É a segunda vez que ele me corta.{/i}"
            p "{i}Talvez, a minha resposta não o tenha agradado...{/i}"
            $ familia = True
            
        "Fama e luxo.":
            # a protagonista deseja a vitoria pelo prazer de estar nos holofotes e receber muito bem
            m "Desde garotinha... Sempre aspirei para que o mundo soubesse meu nome."
            m "Nasci para brilhar nos palcos e nas capas das maiores revistas!"
            m "Ainda serei a Idol mais bem-sucedida da atualidade, e este é apenas o primeiro passo."
            Srsu "Minha nossa! Quanta ambição, senhorita."
            Srsu "Nunca, em tantos anos de minha carreira, presenciei ninguém que teve a coragem de dizer isso para o público."
            Srh "Ainda mais em um grande programa como este, senhoras e senhores!"
            Srn "Admiro a sua boa honestidade e sede de fama, querida Monnie."
            Srh "Vejo que chegará longe!"
            p "{i}Consegui impressionar o Sr.Star!{/i}"
            p "{i}Nem foi tão complicado quanto imaginei... Talvez ele tenha se identificado.{/i}"
            $ fama = True

        "Fazer aquilo que eu gosto.":
            # a protagonista deseja fazer aquilo que sempre sonhou, música, dança e apresentar-se
            # (ex.: produzir musicas, letras, stages grandes, etc...)
            m "Simplesmente quero fazer aquilo que gosto."
            m "A música é uma parte muito importante da minha vida."
            m "Então, performar aquilo que treinei por tanto tempo, trata-se de um sonho realizado."
            m "Quero compartilhar com o mundo esta parte de mim."
            Srh "Oh! A juventude e a paixão destemida!"
            Srh "Espero que não esteja dizendo isso apenas para ganhar o público, querida!"
            m "O que-"
            $ reconhecimento = True

        "Inspirar as pessoas.":
            # a protagonista quer ajudar as pessoas e inspirar
            # (ex.: produzir musicas, letras, stages grandes, etc...)
            m "Quero fazer algo que as pessoas possam se identificar."
            m "Seja pela música, os sentimentos contidos nas letras, na dança, e no palco."
            m "Servir de inspiração para meus fãs quando eles mais precisarem."
            m "Por meio da arte, podemos nos conectar uns com os outros."
            m "Assim, saberemos que não estamos sozinhos."
            Srn "Essas... são belas palavras, realmente."
            Srh "Espero que não esteja dizendo isso apenas para ganhar o público, querida!"
            m "Eu nunc-"
            $ reconhecimento = True
   
    Srh "Muito bem, assim se encerra a nossa apresentação dessas promissoras estrelas!"
    if reconhecimento:
        p "{i}Lá vai ele de novo... Já consigo ver os cortes na transmissão colocados em vídeos frustrados de haters...{/i}"
    Srn "Amanhã estaremos de volta para esclarecer o funcionamento do programa"
    Srn "E para apresentar a primeira performance!"
    #Sr "Quem sairá vitoriosa? É o que vamos descobrir nos próximos episódios!"
    Srh "Muito obrigado por fazer parte da nossa audiência e até a próxima!"

label prologo2:
    # Cena apos apresentacao
    # As participantes conversam entre si

    # o jogador pode ou nao falar com as personagens

    p "{i}Após a apresentação, fomos todas reunidas nos bastidores.{/i}"
    p "{i}Elas estão conversando... devo me juntar a elas?{/i}"

    
    menu (nvl=True):
        "Se juntar a conversa":
            # aqui temos a primeira interacao com as personagens
            p "{i}Respiro fundo, tomo coragem e me aproximo do grupo.{/i}"
            lh "Foi uma ótima apresentação, meninas!"
            lh "Na minha opinião, todas se saíram muito bem."
            p "{i}As garotas parecem mais empolgadas depois da fala de Linne.{/i}"
            p "{i}Com exceção de Nádia, que parece indiferente.{/i}"
            jn "Ah, muito obrigada, Linne."
            jn "Você também foi maravilhosa."
            jn "Fez parecer super fácil e..."
            jn "Natural..."
            rh "Não sou de ficar elogiando muito."
            rc "Mas... Devo admitir que fiquei impressionada."
            p "{i}Nádia revira os olhos.{/i}"
            p "{i}O que será que ela tem?{/i}"
            menu(nvl=True):
                "Perguntar qual o problema.":
                    m "... Algum problema?"
                    "Pergunto baixo para que apenas Nádia escute."
                    nn "Não é nada, não."                                  
                    menu(nvl=True):
                        "Insistir.":
                            m "Tem certeza?"
                            m "Você não parece muito-"
                            ns "Quer parar de me encher!"
                            ns "..."
                            nn "Com todo respeito."
                            $ nadia -= 1
                        "Não insistir.":
                            m "..."
                            nn "É só que..."
                            nn "Isso é tão irritante."
                            m "Irritante?"
                            nn "Ah, desculpa."
                            nn "Eu só... pensei alto."
                            m "Entendi..."
        
                "Não perguntar.":
                    p "{i}Ela não parece aberta para conversar...{/i}"
            

        "Não falar com ninguém":

            #"Tá maluco vo eh dormi kkkkk"
            #"Brincadeira, hehe"
            p "{i}Acho... que vou ficar na minha mesmo.{/i}"
            "Escuto Linne, Juni e Roko trocarem elogios."
            "Enquanto Nádia permanece calada."
            p "{i}E levemente irritada também.{/i}"
            "Após algum tempo, sua atenção se volta para mim."
            ns "..."
            p "{i}Devo dizer algo para ela?{/i}"
            menu(nvl=True):
                "Tentar puxar assunto":
                    m "Er..."
                    m "Seu nome é Nádia, não?"
                    m "É um prazer te conhecer."
                    nsu "Oh, o prazer é todo meu."
                "Não dizer nada":
                    m "..."
                    nn "Entendi..."
                    nsm "Você não é muito de conversar, né?"
            "Isso atrai a atenção das outras."
            nh "Não se preocupe, eu não mordo a menos que necessário, he, he."
            ln "Certo, junte-se a nós, estaremos convivendo por bastante tempo, não?"
            m "Obrigada, espero que nos demos bem."
            rn "Olh-"
    
    "O que quer que Roko fosse dizer, acabou sendo ignorado."
    "A conversa foi interrompida pela equipe de produção se aproximando e anunciando o próximo cronograma."
    "O diretor explica que, basicamente, todas as nossas atividades serão gravadas para o programa."
    "Inclusive algumas partes do dormitório, como cozinha, quartos e sala de estar."
    "Não precisaremos dividir os quartos e nem nos preocupar em preparar nossas refeições."
    "Logo após isso, a equipe nos conduz ao nosso dormitório."
    "Ao chegarmos, analisamos o local em conjunto."
    # aq pode ter uma descrição do ambiente
    "Há uma copa ligada a uma cozinha, com uma mesa de exatos cinco lugares."
    "Não muito longe, há um sofá com alguns puffs ao lado."
    "Daqui, é visível um corredor que dá para os quartos."
    "."
    # achei melhor a protagonista ter uma opinião propria aq
    "{i}Apesar de simples, achei o espaço até que bem agradável.{/i}"
    r "Ah... Eh aqui que nós todas vamos ficar?"
    "Roko olha ao redor com uma expressão meio... enojada."
    l "Ora, Roko! Não faça essa cara!"
    l "A equipe deu tudo para que o ambiente fosse o melhor possível!"
    l "É muito rude da sua parte exigir isso."
    n "Ainda bem que não vamos precisar dividir os quartos..."
    r "O que?!"
    n "Nada, não."
    j "A decoração também é muito bem elaborada..."
    j "Eu achei uma graça!"
    n "A cozinha parece ótima também..."
    n "Será que podemos fazer alguma coisa aqui?"
    m "Ninguém disse que não podíamos, né?"
    n "É verdade!"
    n "Hmm... Como se chama mesmo?"
    n "Luna ou algo do tipo, né?"
    "Como... Como ela errou completamente o nome!?"
    m "É Moonie, na verdade."
    m "Mas podem me chamar de Moon, se quiserem."
    j "Aaah! achei um apelido muito fofinho!"
    n "E é bem mais simples lembrar."   
    n "Do que tava falando mesmo?... Ah, é!"
    n "Dá fazer muita coisa legal aqui."
    n "O que acham?"

    menu(nvl=True):
        "Parece divertido!":
            m "Acho uma ótima ideia!"

        "Não parece grande coisa.":
            m "Não acho que estamos aqui pra isso..."
            l "Exatamente!"
            l "Não vamos ter tempo para essas coisas."
            "Nádia suspira beeem alto."

    r "De qualquer forma..."
    #"Seu tom de voz se torna mais agressivo."
    r "Não irei ingerir nada que vocês prepararem!"  
    n "!!!"
    #r "Não é nada pessoal..."
    r "É q-que eu costumo comer apenas pratos profissionais..."
    r "N-não é nada pessoal, endentem?"
    n "Na verdade pareceu bem pessoal, sim!"  
    j "humm... Bem..."
    j "Melhor nós descansarmos agora."
    j "Hoje foi um dia cheio e amanhã temos muito o que fazer."
    m "Devo admitir que estou bem cansada, também."
    m "Vou terminar de me instalar por aqui e ir dormir."
    m "Boa noite, meninas."

label fimprologo:

    # aq moonie esta em seu quarto p refletir e descansar
    "..."
    "{i}Finalmente, tenho um momento a sós no meu quarto.{/i}"
    "{i}Tenho muito o que processar...{/i}"
    "{i}Vou ter que desfazer as malas, também.{/i}"
    "{i}Não foi permito trazer muias coisas, infelizmente...{/i}"
    "{i}Pelo menos deixaram eu entrar com o meu conjunto de treino favorito!{/i}"
    "{i}Vou guardar ele bem... Aqui parece bom.{/i}"
    #"Arrumo meu quarto enquanto penso sobre o dia."
    "{i}...!{/i}"
    "{i}Ai, não! Naquela hora da apresentação...{/i}"
    "{i}Fui interrompida e fiquei sem graça!{/i}"
    "{i}O público deve ter me achado uma idiota! Um fracasso total!{/i}"
    "{i}Mas tá tudo bem...{/i}"
    "{i}Tipo, se for comparar a minha apresentação com a de Roko...{/i}"
    # pode ter um menu de escolhas aq, mas n pensei em nd ainda
    "{i}A dela foi tão vazia quanto eu poderia imaginar!{/i}"
    "{i}Quanto a Juni... Acho que fiquei até com pena dela.{/i}"
    "{i}Ela pode ser muitas mais do que capaz...{/i}"
    "{i}Mas com aquela timidez não dá pra chegar muito longe.{/i}"
    "{i}Engraçado que Nádia é meio que o oposto de Juni.{/i}"
    "{i}Toda afrontosa e confiante...{/i}"
    "{i}Fico assustada toda vez que vejo algum boato sobre ela.{/i}"
    "{i}Eh... Pelo menos, com elas acho que dá pra competir...{/i}"
    "{i}Agora competir com a Linne?{/i}"
    "{i}Com aquela voz perfeita, aparência perfeita, atuação perfeita...{/i}"
    "{i}Sorriso perfeito, timbre perfeito...{/i}"
    "{i}TUDO perfeito!{/i}"
    "{i}Que raiva! E eles juram que esse programa é justo!{/i}"
    "{i}Ahhf...{/i}"
    "{i}Tenho que me acalmar, ficar irritada faz mal pra minha pele...{/i}"
    "{i}E a falta de uma boa noite de sono também.{/i}"

    
    # finalizacao 
    jump cap1_1


