label cap4_1:

    $ dia += 1
    $ periodo = "Manhã"
    $ atividade = "Café da manhã"
    
    "..."
    "O passar dos dias não facilitou para nós."
    "Não houve tempo ou disposição para pensar sobre Juni ou qualquer outra coisa."
    "Hoje é mais um dia intenso. Tenho que continuar."
    "Encontro Nádia na cozinha."
    nsm "Finalmente acordou no horário, Moon?"
    m "*bocejo* Bom dia, pra você também..."
    nn "Garota... cê tá acabada, hein."
    m "Ah, isso é normal..."
    m "Queria ter a habilidade de acordar disposta todos os dias."
    m "Como a Linne... "
    m "Aliás, cadê ela?"
    nn "Uh, sei lá."
    nn "Talvez treinando?"
    m "M-mas já?"
    m "Ainda é muito cedo..."
    m "Você não acha isso preocupante?"
    nn "Um pouquinho... mas, tipo, eu vou fazer o quê?"
    nsr "A doida não gosta que a gente questione ela."
    m "..."
    p "{i}Treinando? Mal amanheceu...{/i}"
    nh "Ahh, eu tô tããão feliz que acabaram os treinos em duplas..."
    nsm "Posso voltar a seguir minha rotina sem a interferencia de nenhuma chata."
    nsr "Estava me sentindo presa, já!"
    m "É mesmo? Bom..."
    m "Eu vou sentir falta da Juni. Era... Bem interessante treinar com ela."
    nn "Cê tinha uma boa dupla. Quanto a mim..."
    m "Você tá reclamando da sua dupla, mas ficaram em primeiro!"
    nn "Hã... Sim. Mas teve um custo."
    nsr "No começo eu sentia vontadade de esganar aquela galinha!"
    nn "Mas depois, tipo, as coisas foram melhorando bastante."
    nn "Não foi tão ruim quanto achei que fosse ser."
    p "{i}Nádia mudou de ideia a respeito da Linne?{/i}"
    nsm "Eu vou nessa, Moon."
    nsm "Até mais tarde."
    m "A-Até."
    p "{i}Estranho... Pensei que elas tinham brigado feio...{/i}"
    p "{i}Tava todo mundo falando sobre da última vez que eu olhei o celular.{/i}"
    p "{i}O que sará que eles descobriram? Eu não cheguei a ver...{/i}"
    p "{i}Naquele dia eu estava mais preocupada com a minha imagem do que qualquer outra coisa...{/i}"
    p "{i}Por causa do trato... Eu...{/i}"
    p "{i}Eu sinto que mudei...{/i}"

    if confianca_juni:
        p "{i}Poxa, Juni confia em mim!{/i}"
        p "{i}Imagine se ela descobrisse a verdade! Ela ficaria arrasada...{/i}"
        p "{i}Eu deveria parar de usá-lo{/i}"
        p "{i}Mas... Talves ela nunca descubra.{/i}"
        p "{i}O que os olhos não veem... O coração não sente...?{/i}"
    
    ln "Moon?"
    m "Ah, bom dia, Linne."
    "Seu rosto está inchado e ela parece sonolenta."
    p "{i}Será que... ela acordou agora? Isso é... possível?{/i}"
    m "Acordou agora, Linne?"
    li "..."
    "Ela fica irritada pela pergunta."
    m "Oh, d-desculpa! Eu não queria..."
    m "S-sabe, é que isso não é tão comum."
    m "Acho que a gente trocou de lugar hoje. He he..."
    m "Já que você perdeu o horário..."
    li "..."
    m "..."
    li "Não estou com muita vontade de conversar hoje."
    "Ela simplesmente dá meia volta e sai."
    p "{i}Ok...{/i}"
    p "{i}Talvez eu converse com ela mais tarde.{/i}"

    $ atividade = "Treinamento de canto"

    "Durante o treino de canto, minha voz chega a falhar algumas vezes."
    "O instrutor disse que não deve ser nada de mais..."
    "Mesmo assim ele me recomendou um tempo pra descançar a voz."
    "E ele chegou a comentar que Linne estava com o mesmo problema."
    "Deve ser uma boa oportunidade para falar com ela sobre."
    
    #$ periodo = "Tarde"
    $ atividade = "Descanso" 

    "Os lugares parecem mais vazios e mais movimentados a cada etapa do programa."
    "Encontro Linne no studio de dança."
    m "Olá, Linne. Tem um minuto para conversar."
    li "O que foi?"
    m "Err..."
    p "{i}Ela continua irritada...{/i}"
    m "Bem, eu... Estou com um probleminha com minha voz..."
    m "Fiquei sabendo que você também está com isso-"
    li "Quem disse isso?"
    m "Hã? O instrutor disse..."
    m "Aí ele recomendou um descanso."
    ln "Ah, isso é mentira."
    ln "Eu não preciso de descanço nenhum."
    m "M-Mas..."
    li "Posso continuar meu treino em paz agora?"
    m "... Pode sim."

label cap4_2:

    $ periodo = "Tarde"
    $ ativdade = "Almoço"

    "Me encontrei com Nádia para almoçarmos."
    nsm "Finalmente! Tô morta de fome."
    
    "Nos sentamos à mesa para comer."
    p "{i}Mas... Onde está Linne?{/i}"
    m "Hmm... Não cheguei a ver Linne depois do café... Você a viu?"
    nn "Ela deve estar treinando ou algo do tipo."
    nn "Por que?"
    m "É que... ela anda estranha."
    nn "Ah, deve ser o cansaço batendo na porta dela."
    nn "Depois de tanto treino pesado... Não dá pra esperar outra coisa."
    m "Isso é triste..."
    nn "Pois é... Mas é necessário. Pra debutar."
    nsr "..."
    nsr "Já pensou? O que será que vem após o debut?"
    m "O que quer dizer?"
    nn "Eu tava pensando sobre isso esses dias..."
    nn "Quem eu vou ter que me tornar depois do debut?"
    nn "O que eles farão comigo?"
    nn "A empresa vai criar uma nova identidade pra você... E tudo o que pode fazer é estar a altura das expectativas."
    nsr "Não sobra muito tempo pra eu ser... Eu."
    nn "Me assusta um pouco a ideia de que, depois de tudo o que passei, eu acabe como apenas uma ferramenta."
    p "{i}Fe-ferramenta?{/i}"
    nsm "Ah... Foi mal pelo desabafo. Eu só queria compartilhar com alguém."
    m "Não precisa se desculpar. E na verdade você tem um ótimo ponto."
    nsm "É claro que eu tenho!"
    nn "Esse é o preço que temos que pagar pela fama..."
    nn "Meio difícil me acostumar com a ideia. Mas, tipo..."
    p "{i}Esse assunto está me chateando... Melhor eu mudar.{/i}"
    m "E... Como se sente tão perto das finais?"
    m "Aliás, a próxima eliminação já é depois de amanhã."
    nsm "Eu? Eu tô confiante!"
    m "Nossa... Você parece animada."
    nsm "Saber que já tá chegando ao fim me anima."
    nsm "Heh. Vocês duas que se cuidem, porque eu não vou pegar leve!"
    nsm "Bem, eu já acabei minha refeição!"
    nsm "Tô indo nessa, Moon."
    m "Tudo bem..."

    p "{i}Ferramenta... Ferramenta...{/i}"
    p "{i}Será que eu vou me tornar uma... Não.{/i}"
    p "{i}Será que eu já me tornei... Uma ferramenta do sr.Star?{/i}"

label cap4_3:
    # mais tarde no dia
    $ periodo = "Noite"
    $ atividade = "Antes de dormir"

    "Após uma tarde de treinamento excessivos, finalmente estou no meu quarto."
    p "{i}Faz tempo que não olho as redes. É a minha oportunidade.{/i}"
    p "{i}Hmm... onde foi que eu deixei o celular?{/i}"
    "Ouço batidas na porta."
    desc "Moon, está aí?"
    m "AAAH!"
    "Linne abre a porta e entra no quarto."
    ln "O que aconteceu? Porque se assustou assim?"
    m "Ah, n-não é nada..."
    ln "Sei... eu só ia perguntar se você viu o meu secador."
    m "N-não vi, não..."
    li "Está escondendo algo, Moon?"
    m "Err... N-não."
    li "..."
    ln "Então, boa noite."
    "Ela fecha a porta do quarto enquanto saia."
    p "{i}Caramba... Essa foi por pouco...{/i}"
    "{i}Será que ela desconfia de algo?{/i}"
    "{i}Vou dar só uma olhadinha rápida nas postagens... Vai que ela resolve voltar.{/i}"
    "{i}Vejo notícias e muitas pessoas discutindo sobre a suposta agressão cometida por Nádia...{/i}"
    "{i}Deve ser o que Linne estava falando naquele dia. Será que ela foi agredida por Nádia mesmo?{/i}"
    "{i}Parece que as pessoas realmente estão invertigando o caso.{/i}"
    "{i}Tem muitos comentários de hate direcionados a Nádia, mesmo não tendo nada confirmado.{/i}"
    "{i}Subiram até uma hashtag nas redes...{/i}"
    "{i}Ela com certeza está em maus lençois.{/i}"
    "..."

    $ dia += 2
    $ periodo = "Manhã"
    $ atividade = "Acordando"

    "..."
    "Acordo com Nádia gritando do corredor."
    nsr "Vamo, gente! Bora acordar, já são nove e meia!"
    nsr "E hoje tem apresentação, hein!"
    p "{i}9:30? Mas era pro meu despertador despertar as 7!{/i}"
    p "{i}Qual o problema dele?! Parece até que ele fica se desconfigurando sozinho!{/i}"
    p "{i}Saindo do quarto, percebo que Linne também está acordando agora.{/i}"
    nn "Ué? Porque que ninguém ta acordando no horário?"
    m "O meu despertador tá com problema."
    nn "Sei... E você, Linne? Porque não acordou?"
    ln "O que... ? Ah, o meu deve estar também..."
    nsm "Sério? HA HA! Bem feito!"
    m "A gente deveria notificar o Sr.Star sobre-"
    lnv "N-Não! Não tem necessidade disso..."
    li "Anda. Temos que nos preparar."
    m "Hmm..."

    $ periodo = "Tarde"
    $ atividade = "Antes da apresentação"

    nn "Tá quase na hora..."
    m "Cadê a Linne? Ela não é de se atrasar..."
    nn "Ah, quem se importa? Uma hora ela aparece."
    nsm "Vou arrasar nessa apresentação! Eu tô sentindo!"
    
    if nadia > 5:
        m "Você mudou bastante, Nádia."
        nsr "Mudei? Que nada!"
        m "É verdade."
        m "Nem parece a mesma pessoa do início do programa."
        m "Sabe... Não perde a paciência tão rápido..."
        m "Tá mais controlada..."
        m "Até sorri mais!"
        nn "Cê tá exagerando... Mas..."
        nn "Tipo, eu aprendi a ser mais tolerante com algumas coisas..."
        nn "Meio que o programa me forçou a isso, no final das contas."
        m "Entendo..."

        menu(nvl=True):
            "Essa é uma mudança bem-vinda":
                m "Eu gostei da mudança."
                nsr "Hm? Tá querendo dizer o quê com isso, hein?!"
                m "N-Não me entenda mal!"
                m "É que... É bom ver você melhorando assim."
                nh "Ow. Que fofo!"

            "Como se sente com a mudança?":
                m "E o que está achando desse processo?"
                nn "Hã?"
                nn "Tipo..."
                nn "Eu não sei..."
                nsm "Com a mudança, eu sinto que finalmente estou próxima dos meus objetivos..."
                nn "E ao mesmo tempo..."
                nn "Tipo, parece que tô distante... de mim mesma."
                nsr "Eu tô ligada que isso é necessário até certo ponto..."
                nn "Ainda mais quando você é uma estrangeira barraqueira mal vista."
                nsr "Minha família já passou por xenofobia o suficiente por minha causa."
                nsr "Nossos vizinhos sempre diziam:"
                nsr "'Essa menina barulhenta é um terror! Se for pra causar essa bangunça, voltem logo pro seu país!'"
                nsr "Esses vizinhos eram uns malas!"
                nn "Mas eu também não facilitava, não."
                nn "*suspiro* Tudo me deixava cada vez mais nervosa..."
                nn "..."
                nsm "É bom saber que tô melhorando o meu controle emocional."
                nsm "Pra mim, tá valendo a pena passar por essa mudança."
    
    ln "Cheguei, meninas."
    ln "Perdi muita coisa?"
    "Não sobrou muito tempo para conversas, logo já estávamos sendo colocadas na frente de câmeras."
    "..."

    #troca de cenario
    $ atividade = "Apresentação"

    "..."
    Srh "Muito boa noite a toda nossa querida audiencia!"
    Srh "Eu sou o Sr.Star e você está assistindo o reality STAR'S SELECTION!"
    Srn "E essa noite, teremos mais uma eliminação!"
    Srn "Estamos cada vez mais próximos do gran finale!"
    Srh "Estão animados? Pois eu estou!"
    Srn "Agora, podemos dar início as apresentações."
    Srh "Srta. Moonie, pode subir ao palco!"

    "Realizamos as apresentações na sequência:"
    "Eu primeiro. Acredito que fui bem na medida do possível. A pressão é muito grande, mas não posso desistir."
    "Linne foi em segundo. Pela primeira vez, eu a vejo cometendo pequenos erros na performance..."
    "Nádia em terceiro. Ela estava certa quando disse que ia arrasar."

    Srh "Essas foram as apresentações, senhoras e senhores!"
    Srh "Todas as participantes foram MA-RA-VI-LHO-SAS!"
    Srn "Infelizmente, uma de vocês será desclassificada..."
    Srn "Quem será a pobre eliminada? É o que vamos descobrir logo logo!"
    Srh "Fiquem ligados! Já já estaremos de volta!"

    $ periodo = "Noite"

    "Nádia está radiante."
    li "..."
    li "Então... Uma de nós vai ser eliminada..."
    ln "Independente do resultado, quero que saibam que foram todas muito bem."
    nn "Pare de fingir que se importa, Linne. Isso tá ficando chato."
    li "Grr! Cale a boca! Eu só estou tentando ser legal."
    li "Diferente de você!"
    nsr "Eu? Ah, nem vem!"
    m "Vocês duas brigam com bastante frequência..."
    nn "Não... Isso ficou no passado."
    p "{i}Passado?{/i}"
    m "Falando nisso... Vocês já brigaram feio?" #ô enxerida lkkkkk
    m "Com agressões e-"
    nsu "O que? Nunca!"
    m "Jura?"
    m "A Linne já contou que aconteceu uma vez..."
    li "HÃ?!"
    nsr "Ela disse O QUE?"
    li "É-É mentira dela! Nunca falei nada do tipo!"
    m "Disse sim. Naquele dia quando estávamos almoçando... Cheguei a ficar preocupada-"
    lnv "N-Não acredite nela! Eu garanto que é tudo invenção!"
    na "Invenção? Quem inventaria alguma coisa dessas além de você?!"
    li "Ela... Ela é uma mentirosa trapasseadora!"
    li "Não se lembra do que eu falei? Ela extrai o máximo possivel de todos pra ganhar vantagem!"
    li "Por isso ela se aproxima tanto das pessoas! Pra se aproveitar delas!"
    m "Ei! Eu nunca faria isso!"
    li "E-E eu te contei que ela tem um celular, sendo ele totalmente proíbido!"
    m "!"
    li "Eu te avisei e você não quis acreditar!"
    p "{i}ELA DESCOBRIU!{/i}"
    n "Isso é verdade, Moonie?"
    "..."
    m "Obvio que não! Não tem como eu ter uma coisa dessas..."
    li "Viu? Ela hesitou!"
    nsr "..."
    nsr "o que tá acontecendo aqui... ?"

    "No exato momento que nos encaramos, membros da equipe vieram nos buscar para continuar o show."
    p "{i}Isso não tem como acabar bem...{/i}"

    $ atividade = "Saída dos resultados"

    "..."
    Srh "Estamos de volta ao programa!"
    Srn "Bem... Meninas, tenho más notícias..."
    Srn "Os resultados foram cancelados devido a um problema."
    Srsc "Nádia está desclassificada devido ao rumor de agressão que ganhou força nas redes do programa."
    nnv "C-COMO?"
    na "ENTÃO ERA VERDADE!"
    Sra "Por favor, se acalme-"
    # no fim ela n mudou tanto assim (algumas coisas não mudam né)
    na "INVENTOU UMA MENTIRA QUE ARRUINOU MINHA CARREIRA!"
    li "Eu não inventei nad-"
    "*SLAP*"
    "Nádia dá um tapa no rosto de Linne."
    "..."
    "..."
    na "NÃO QUERO TE VER NUNCA MAIS!"
    na "E VÃO SE FODER TODOS VOCÊS! ESTOU CANSADA DE TODAS ESSAS MENTIRAS!"
    "Ela sai batendo os pés e com lágrimas nos olhos."
    m "N-Nádia? Espera!"
    "Corro atrás dela."
    Srn "Err... Isso é tudo por hoje..."
    Sra "Corta a gravação."

    "Finalmente consigo alcança-la nos corredores para os palcos."
    ns "... O que foi, agora?!"
    m "Nádia eu..."
    ns "O que Linne disse sobre o celular... é verdade?"
    m "..."
    ns "Eu sabia... Então tudo aqui é falso!"
    m "Mas eu... Não tive escolha..."
    ns "Ah, é? Pois saiba que isso não te faz melhor do que ninguém... Muito pelo contrário!"
    m "Eu..."
    ns "Passou esse tempo todo enganando todas nós..."
    ns "Me responde... Você é um lixo humano como aquela cobra?"
    m "N-Não..."
    ns "Então prove! Ou nunca passará de um ser desprezível!"
    "Nádia vai em direção a saída sem dizer uma palavra."
    p "{i}Provar...?{/i}"

    jump cap5_1
    

