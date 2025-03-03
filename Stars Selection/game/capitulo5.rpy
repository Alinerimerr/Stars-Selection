label cap5_1:
    
    $ dia += 1
    $ periodo = "Manhã"
    $ atividade = "Café da manhã"

    "..."
    "Estou tomando meu chá com biscoitos na cozinha."
    "Completamente só."
    "Muita coisa aconteceu ontem..."
    "..."
    p "{i}Eu me sinto um lixo.{/i}"
    p "{i}Quando eu aceitei o trato... Não achei que fosse tudo dar tão errado.{/i}"
    p "{i}Por que eu fui aceitar uma coisa dessas?{/i}"
    p "{i}Por que, dentre todas, eu tive que ser a escolhida para o trato?{/i}"

    ln "..."
    "Neste momento, Linne chega na cozinha e se senta à mesa para tomar café."
    m "..."
    "Permanecemos em silêncio por um tempo."
    "Olho fixamente pra minha xícara de chá para evitar olhar Linne nos olhos."
    ln "Moon..."
    m "O que foi?"
    "Continuo com os olhos fixos na xícara."
    ln "O que foi? Está brava comigo?"
    ln "É por causa do que aconteceu ontem?"
    ln "Você parece cansada... E arrependida."

    menu(nvl=True):
        "Você também.":
            m "Quanto a você?"
            m "Aposto que nem dormiu durante a noite."
        "Isso não é da sua conta":
            m "E daí? O que você tem a ver com isso?"

    ln "Por que... Não desiste logo?"
    "Finalmente levanto meus olhos para encará-la."
    m "Como?"
    ln "Sabe, isso vai te poupar do sofrimento..."
    ln "Encare isso como uma redenção."
    m "Tentando me convencer a desistir?"
    m "Hah... Não vou cair nessa, sua..."
    li "Está achando que pode me julgar? Quem esteve trapasseando com um aparelho esse tempo todo não fui eu."
    li "Você e eu... Não somos tão diferentes."
    ln "Estamos dispostas a qualquer coisa para vencer..."
    m "Está errada!"
    ln "Me conta... Você recebeu ajuda, não é?"
    m "..."
    ln "Admita. Nunca chagaria até aqui sem ajuda."
    ln "Teria sido eliminada no lugar de Juni. Eu tenho certeza."
    li "Você não passa de um rostinho bonito com talento mediano. Nunca precisou sacrificar nada pra chegar até aqui."
    ln "Já eu..."
    li "Eu treinei por minha vida toda."
    li "Cortei os laços com meus amigos..."
    li "Me forcei a ser perfeita. Só pra chegar até aqui."
    li "Tudo isso é mérito meu!"
    li "E você? Acha que merece vencer?"
    li "É tão egoíta assim?"
    m "Eu... Preciso ir."

    p "{i}Eu não aguento mais!{/i}"
    p "{i}Tenho que fazer alguma coisa!{/i}"

    "Pego meu celular e mando uma mensagem marcando uma reunião com o Sr.Star."

    $ periodo = "Tarde"
    $ atividade = "Reunião"

    "..."
    Srn "Gostaria de falar comigo, senhorita?"
    m "Sim... Eu-"
    Srn "Esses dias tão uma loucura, menina!"
    Srh "A senhorita viu? A eliminação de ontem deu o que falar nos fóruns do programa!"
    Sra "Aquela Nádia causou demais! Por sorte ninguém culpou o programa pelos danos causados por ela."
    Sra "*suspiro* Nunca mais permito gente daquela laia no meu programa!"
    m "Sei..."
    Srn "Estava até pensando em organizar algum evento ao vivo para hypar as finais..."
    Sra "Mas estou sofrendo uma pressão absurda pra terminar logo o programa por conta das polêmicas..."
    Srn "Infelizmente, vocês duas só se apresentarão nas finais mesmo."
    Srn "Então, o que quer afinal, querida?"
    m "Err... Eu..."
    p "{i}Preciso saber o motivo de eu ser a escolhida.{/i}"
    m "Por que dentre todas as participantes, eu fui escolhida pra o trato?"
    Srsc "Me fez perder meu tempo precioso só por uma pergunta?"
    m "Desculpe... É importante pra mi-"
    Srh "Que ousado! Gostei!"
    Srn "Respondo a sua pergunta com prazer!"
    Srn "Por onde eu começo...?"
    Srn "Roko era uma garotinha mimada e irritante."
    Srn "Juni era tããão apagadinha... Quase não tinha carisma e ninguém se lembrava dela."
    Sra "E ela engorda muuuito fácil. Não quero uma pessoa assim na minha empresa!"
    Srn "E Nádia... Bem, você viu o que aconteceu ontem."
    Srn "Com ela seria problema toda semana!"
    m "Tudo bem, mas... Porque não Linne? Ela era perfeita..."
    Srn "He heh... Não é obvio?"
    Srn "Ela manipulou e sabotou durante o programa inteiro!"
    Srn "Tinha que ver o tanto de atrocidades que ela falou sobre você para as outras participantes."
    Srsc "Se ela é capaz de tudo isso, pra ela sabotar minha empresa em benefício próprio era dois palitos!"
    Srn "E não sei se a senhorita percebeu... Mas o seu despertador não tinha problema nenhum."
    Srn "Era só ela desconfigurando o alarme pra te fazer dormir até mais tarde."
    Srh "Inclusive foi numa dessas sabotagens que ela descobriu o celular..."
    Srn "Foi até meio engraçado... As pessoas estão dispostas a todo tipo de coisa pra vencer! "
    m "É sério?! E o senhor não fez nada a respeito? Poderia ter expulsado ela logo no início!"
    Srn "Tudo ficaria muito sem graça se ela saisse."
    Srn "E a senhorita sabe que o público adoooora um conflito, não é mesmo?"
    m "O Sr. ainda não respondeu a minha pergunta..."
    Sr "Oh, perdão, senhorita!"
    Srn "Bem... Você é bonita, educada, as pessoas gostam de você..."
    Srn "E as suas habilidades são até aceitáveis. É exatamente do que estou precisando no momento!"
    m "..."
    Srsu "Qual o problema? Isso não te deixa feliz?"
    Srn "Afinal, a senhorita está cada vez mais perto do seus sonhos..."
    m "É que... Eu..."
    m "Estou... Quebrando nosso trato!"
    m "Não quero mais fazer perte desse esquema."
    Srsu "..."
    Srsc "Como assim, senhorita?"
    Srsc "Desistir a essa altura do campeonato não faz o menor sentido."
    Srsc "Pense bem, jovem... Essa é a sua única chance de vencer."
    Srsc "A final já é depois de amanhã."
    Srsc "E você não aguentaria concorrer com Linne de verdade."
    p "{i}Linne está exausta... Acho que posso vence-lá!{/i}"
    m "Não importa... Eu desisto do trato."
    Srsc "Ora... Tudo bem."
    Srn "Tá se achando demais, hein?"
    Srn "A senhorita quem sabe."
    "Devolvo o celular ao Sr.Star e saio da sala."
    "Do corredor consigo escutar o Sr.Star dizer:"
    Srsc "Que tonta! Que diferença faz desistir agora? Ela não percebeu os sacrifícios?"
    
    p "{i}Eles vão ver! Vou provar que sou muito mais do que eles pensam!{/i}"
    "..."

label cap5_2:

    $ dia += 1
    $ periodo = "Tarde"

    "..."
    "Depois de passar esses dois dias treinando, volto aos dormitórios para um descanço merecido."
    p "{i}Está tudo tão silencioso...{/i}"
    "..."
    p "{i}Queria poder conversar...{/i}"
    p "{i}Será que devo procurar por Linne?{/i}"
    
    menu(nvl=True):
        "Sim.":
            p "{i}Não sei se é uma boa ideia... Mas acho que vou falar com ela.{/i}"
            # descricao do local
            "Após andar um pouco, percebo a porta do banheiro entreaberta."
            "A pia chia com o som da água e respirações pesadas saem de lá."
            "Resolvo entrar."
            "Encontro Linne pressionando o pulso, que parece lesionado."
            m "Aconteceu algo, Linne?"
            m "Você está bem?"
            lnv "E-Estou! É só um machucadinho..."
			
                menu(nvl=True):
                    "Bem feito!":
                        m "É nisso que dá ser uma pessoa péssima."
                        m "Você sempre acaba se dando mal."
                        la "Cala a boca! Quem você acha que é para dar lição de moral?"
                        la "Melhor tomar cuidado, ou quem vai de dar mal no final é você!"
                        la "Sai logo daqui! Não preciso de você me atrapalhando!"
                        m "Hump!"
                        m "Então boa sorte na apresentação de amanhã!"
                        "Dito isso, saio em direção ao meu quarto. Não tenho mais compaixão por ela."
                        "Durmo neste dia com um sono inquieto e uma ansiedade constante."
                        $ karma += 10
                        jump cap5_3
    
                    "Certeza?":
                        m "Certeza? Você parece machucada-"
                        li "N-Não fale comigo!"
                        li "Me deixe em paz!"
                        p "{i}Ela parece mal...{/i}"
                            if linne > 2:
                                m "Por que não procura pela equipe médica? Eles podem ajudar."
                                li "Eles vão me impedir de competir!"
                                la "Não vou perder assim!"
                                lnv "Minha mãe vai me matar se eu perder desse jeito..."
                                    menu(nvl=True):
                                        "Te matar?":
                                            m "Como assim sua mãe..."
                                            lnv "N-Nada! Eu só pensei alto!"
                                            # moon n entende q nem todo mundo tem bons pais (a mana vive numa bolha)
                                            m "Aposto que sua mãe estaria preocupada com o seu estado atual."
                                            m "Ela entederia caso você precisasse de ajuda."
                                            li "Preocupada? Ela só está preocupada com o meu sucesso."
                                            li "E apenas isso."
                                            p "Caramba... Que horrível!"
                    
                                        "Mas você precisa de ajuda!":
                                            m "Mas... Você parece exausta há dias."
                                            m "E agora está machucada!"
                                            m "Não pode continuar desse jeito sem receber ajuda..."
                                            li "Besteira! Já passei por coisa pior."
                                            m "Coisa pior?"
                                            li "Eu era forçada a treinar todos os dias, mesmo nas piores situções."
                                            li "Não vai ser uma lesão que vai me impedir agora."
                                            p "Forçada? será que a mãe dela..."
                                    $ pressao = True
                
                                li "Vá embora. Já falei que não quero conversar."
                                m "Tudo bem... Mas pode vir falar comigo se precisar de algo."
                                "Sigo em direção aos dormitórios, deixando Linne para trás."
                            else:
                                "Queria poder ajudar, mas..."
                                "Acho que ela vai ficar ainda mais brava."
                                m "Tudo bem... Mas pode vir falar comigo se precisar de algo."
                                "Sigo em direção aos dormitórios, deixando Linne para trás."
        
        "Não.":
            "Melhor não..."

    p "{i}Estou no meu quarto pronta para dormir.{/i}"
    p "{i}Que nervoso! Amanhã já é a apresentação final!{/i}"
    p "{i}Serei capaz de vencer Linne?{/i}"
    p "{i}Por mais que a situação esteja favorável para mim... Ainda sinto medo.{/i}"
    p "{i}Espero que eu consiga dormir...{/i}"

    $ dia += 1
    $ periodo = "Noite"
    $ atividade = "Apresentação final"

label cap5_3:

    Srh "Muuuuuuito boa noite, senhoras e senhores!"
    Srn "Eu sou o Sr.Star e... Vocês sabem que dia é hoje?"
    Srh "É O GRANDE DIA DA APRESENTAÇÃO FINAL DO REALITY STAR'S SELECTION!"
    # aplausos
    Srsu "Nossas estrelas tiveram uma loooonga jornada durante todo o programa."
    Srn "E finalmente, chegamos ao momento do grande e tão esperado desfecho!"
    Srsu "Quem saira vitoriosa? É o que vamos descobrir essa noite!"
    Srn "Estão preparadas, meninas? Pois vamos começar!"
    Srh "Apresente-se, srta.Moonie!"
    p "{i}Meu Deus! Meu Deus!{/i}"
    p "{i}Preciso me manter calma! Não posso me deseperar agora.{/i}"
    "Subo no palco e assumo minha posição."
    # descricao da apresentação dela

    Srh "E essa foi a performance da nossa queridíssima Moonie!"
    Srn "Muito bem, senhorita!"
    Srn "Agora, vamos segur em frente."
    Srh "Suba ao palco, srta.Linne!"

    "Linne sobe ao palco."
    "Mesmo com muita maquiagem, dá pra ver traços de exaustão nela."
    "Seu movimentos estão meio lentos e as vezes dessincronizados."
    "E sua voz parece cansada também."
    "Ela faz a performance da melhor forma que pode, apesar de tudo."
    p "{i}Mesmo assim... Acredito que tenho chances!{/i}"

    Srh "E essa foi a performance da srta.Linne!"
    Srsu "Eu esperava mais de você..."
    Srsu "Ainda mais na apresentção final."
    Srn "Enfim..."
    Srh "Essas foram as apresentações da noite, senhoras e senhores!"
    Srn "Já já voltamos com os resultados finais do reality."
    Srh "Fiquem ligados!"

    "Durante o intervalo, eu e Linne ficamos em um silêncio constrangedor."
    li "..."
    li "Está confiante?"
    m "Estou sim..."

    li "É mesmo? Por que?"

    menu(nvl=True):
        "Minha apresentação foi boa.":
            m "Acredito que eu fiz um bom trabalho na minha apresentação."
            li "Ah, aquela performance mediocre? Você está mentindo pra si mesma!"
            li "Não tem chance contra mim."
            m "..."
        "Sua apresentação foi horrível.":
            m "A sua performance foi ridícula."
            m "Com certeza eu irei ganhar."
            la "O que? Como ousa..."
            la "Você vai ver só quando EU vencer!"
            $ karma += 10

    Srh "Bem-vindos de volta ao programa, senhoras e senhores!"
    Srsu "Chegou o tão aguardado momento..."
    Srh "Dos RE SUL TA DOS!"
    Srn "Em instantes, aparecerá no telão a pontuação atingida por cada participante."
    Srn "Como sabem, a que conquistar a meior pontuaçõa..."
    Srh "Será a grande estrela vencedora dessa edição do programa!"
    Srh "Espero que estejam tão animados quanto eu!"
    p "{i}É agora. A hora da verdade!{/i}"
    Srn "E a vencedora é...."
    "Depois do que pareceu uma eternidade, finalmente aparece no telão os resultados."

    if karma >= 30: # situacao em q moon perde
        # n sei expressar alegria
        Srh "A VENCEDORA É LINNE!"
        p "{i}O QUE?!{/i}"
        Srh "Meus parabéns, querida!"
        lh "Muito obrigada, Sr.Star!"
        lh "Muito obrigada a todos que me apoiaram!"
        lh "Amo muito todos vocês!"
        p "{i}Depois de tudo o que ela fez... Ela venceu.{/i}"
        p "{i}Se bem que... Eu também não fui muito justa.{/i}"
        p "{i}Talvez eu não merecesse ganhar no fim das contas...{/i}"
        m "Parabéns, Linne."
        #desenvolver melhor essa parte
    else:
        Srh "A VENCEDORA É MOONIE!"
        p "{i}SOU EU!{/i}"
        Srh "Meus parabéns, querida!"
        Srh "Você merece!"
        m "Ah, caramba!"
        m "Nem acredito que isso está acontecendo!"
        m "Eu nem sei o que dizer!"
        m "M-Muito obrigada a todos! Eu..."
        m "Essa é uma grande vitória para mim."
        m "E-E eu tô muito feliz!"
        $ vitoria = True
    #desenvolver melhor essa parte tmb

    # despedida e encerramento do programa
    Srh "E esse foi o reality STAR'S SELECTION!"
    Srh "Eu sou o Sr.Star e agradeço pela sua audiencia!"
    Srh "Uma ótima noite a todos e nos vemos numa próxima edição!"
    "Após o encerramento do programa,"
    "Somos convivadas a fazer uma entrevista da nossa experiência do programa nos bastidores."

    if vitoria:
    "Antes que pudessemos começar, Linne vem falar comigo."
    ls "Parabéns... Você conseguiu."
    m "Hã... Obrigada."
    ls "Como se sente destruindo meus sonhos?"
    ls "Treinei minha vida toda pra isso."
    ls "Pro no fim perder pra uma trapaceira."
    ls "*suspiro*"
    ls "Vou ser um fracasso pra sempre... Não importa o que faça."
    m "Eu... Sinto muito por você."

    if pressao:
    m "Mas vai ficar tudo bem. Sei que eles vão se orgulhar de você!"
    m "Além do mais, você pode continuar tentando debutar."
    ls "Eu..."
    ls "Eu não quero continuar tentando..."
    ls "Estou tão cansada!"
    ls "Mas se eu não continuar, minha família vai me odiar para sempre."
    m "A aprovação da sua família é tão importante assim?"
    ls "Eles me treinaram pra isso. Investiram muito em mim..."
    ls "Eu só queria que se orgulhassem de mim."
    ls "Isso é... Tudo para mim."
    m "Então debutar não é o seu sonho... É o da sua família!"
    m "Você não é obrigada a seguir as vontades dos outros por aprovação."
    ls "Mas..."
    m "Isso está acabando com você!" 
    m "Se eles se importassem de verdade com você, eles estariam orgulhosos."
    m "Independente do que aconteceu ou acontecerá."
    ls "..."
    ls "Eles nunca demonstraram isso..."
    ls "Hah... Como eu gostaria de ter uma família como a da Nádia..."
    ls "Ela é talentosa e tem uma boa relação com a família..."
    ls "Quela desgraçada tem tudo... E eu a invejo por isso."
    ls "... Obrigada, Moon."
    ls "Ninguém nunca me disse essas coisas..."
    ls "Porém... Não sei como continar."
    m "Vai encontrar um caminho. Tenho certeza disso."
    p "{i}Nos despedimos e seguimos para fazer a entrevista.{/i}"
    p "{i}Caramba... Eu ainda não acredito que venci!{/i}"
    p "{i}Mas... O que será que me aguarda?{/i}"
    p "{i}Mais importante...{/i}"
    p "{i}A que custo?{/i}"


    "FIM"
    "Obrigada por jogar!"
    "Créditos: Maritacas Gamedev."
    "Criadoras: Aline Riemer, Marcela Lima"
    "Agradecimento especial aos supervisores, veteranos e Jéssica."

    return

