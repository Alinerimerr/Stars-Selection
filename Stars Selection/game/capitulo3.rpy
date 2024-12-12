label cap3_1:

    "Mais uma manhã..."
    "Ahh... Parece que tenho que voltar a treinar."
    "Não quero acabar como Roko..."
    
    "Enquanto me preparava para começar meu treinamento..."
    "Um funcionário do programa me informa que o Sr.Star quer que eu me apresente na área do palco o mais cedo possível."
    "{i}Me apresentar? Mas o evento será apenas á noite!{/i}"
    "{i}Sinto que há algo errado...{/i}"
    "Tento me manter calma enquanto caminho até o palco."
    "Chegando na área, vejo uma grande movimentação da equipe de produção para organizar o evento."

    Sr "Ah, Srta.Monnie, que bom que veio!"
    Sr "Temos muito o que discutir..."
    "{i}Oh, não! Será que fiz algo errado?{/i}"

    Sr "Mas não se preocupe, tentarei ser breve."
    Sr "Bom... Tenho observado que você é, realmente, bem habilidosa."
    Sr "E seus feitos no programa chamaram a atenção do público..."
    Sr "Você, basicamente, viralizou nas redes sociais e conquistou uma comunidade de fãs!"
    Sr "Isso trouxe vários novos telespectadores e muuuito engajamento para o programa!"
    Sr "O fato é que o seu debut nessas condições é extremamente benéfico para a empresa."
    Sr "E é por isso que tenho uma oferta especial para você."
    m "C-como assim?"
    Sr "A senhorita tem a oportunidade de garantir a vitória no programa."
    Sr "E tudo o que precisa fazer é manter o hype até a apresentação final."
    Sr "Pode deixar que eu e a produção faremos nossa parte."
    "{i}Caramba! Tô recebendo a maior proposta da minha vida!{/i}"
    "{i}Mas... Ao mesmo tempo isso parece tão injusto com as meninas.{/i}"
    Sr "Então... O que acha?"
    Sr "Ah, você também pode receber dicas e spoilers sobre os eventos..."
    Sr "E talvez alguns outros benefícios..."
    Sr "É, definitivamente, uma oferta IRRECUSÁVEL, não é mesmo?"

    menu(nvl=True):
        "Não sei, não...":
            m "..."
            Sr "A senhorita parece canfusa..."
            m "N-não é nada disso!É que isso me parece meio..."
            m "Corrupto."
            Sr "Ora! Pensei que soubesse com o que estava se metendo quando decidiu se tornar treinee."
            Sr "Essa indústria esconde vários pobres, garota."
            Sr "Se você quiser ter sucesso, deve saber abraçar a ideia quando lhe é conveniente!"
            "{i}Acho que terei problemas com ele se eu recusar a oferta...{/i}"
            m "Tudo bem. Vou pensar sobre."
        "Eu aceito!":
            #m "Parece um bom negocio."
            m "Eu aceito a proposta."
            Sr "Sabia que aceitaria!"
            $ karma += 15
            $ aceitar = True

    m "Só que... O que exatamente significa 'manter o hype'?"
    Sr "O seu trabalho é descobrir isso."
    m "Oh..."
    Sr "Mas tenho algo que com certeza será útil..."
    Sr "Aqui! Leve isto."
    "Ele me entrega um celular comum."
    Sr "Ele tem acesso à Internet, então você pode saber o que as pessoas de fora estão achando."
    m "Mas celulares não são permitidos..."
    Sr "Ora, não se preocupe com isso!"
    Sr "Eu controlo tudo aqui dentro. Posso facilmente apagar qualquer evidência sobre isso."
    Sr "Ah! E é melhor manter isso longe das outras competidoras."
    Sr "Podemos ter problemas caso elas saibam..."
    m "S-sim."
    Sr "Minha nossa, acabei perdendo o horário!"
    Sr "Está dispensada, senhorita."
    Sr "E... Tome cuidado com esse celular, por favor."
    m "Serei o mais cuidadosa possível!"
    m "Agradeço pela oportunidade, Sr.Sta-"
    "Mal termino de falar e ele já me deu as costas."
    "{i}Er... Melhor eu voltar ao meu treinamento.{/i}"

    # encerramento do dialogo e reflexao

    

label cap3_2:

    #evento no qual Juni passara por problemas.

    Sr "Bem vindos, senhoras e senhores, à mais um evento ao vivo..."
    Sr "Do reality Stars Selection!"
    Sr "E hoje teremos... Algo mais tranquilo."
    Sr "Mas não menos impotante, obviamente!"
    # Apresentacao evento

    Sr "E nesta noite, teremos um bate-papo com as estrelas aspirantes do reality."
    Sr "Os temas pautados serão escolhidos por votação em tempo real pela nossa querida audiência."
    Sr "Vocês podem votar pelo acesso ao nosso site ou QR code que está aparecendo na sua tela."
    Sr "Tá esperando o que? Corre lá votar!"
    #Sr "Esse bate-papo foi organizado com o intuito de..."
    Sr "Começando pelo primeiro tópico:"
    Sr "'Por que seguir a carreira de Idol?'"
    m "Oh, eu lembro que respondi essa pergunta na primeira apresentação!"
    Sr "Não era exatamente essa pergunta, mas... Sim, a senhorita respondeu."
    l "Então, eu gostaria de começar."
    # 
    l "Como vocês devem saber, minha família está repleta de artistas..."
    "{i}Eu não sabia disso...{/i}"
    l "Por isso, desde muito jovem estou em constante contato com a arte, que se tornou a minha paixão."
    l "Então seguir essa carreira maravilhosa que inspira muitas pessoas todos os dias..."
    l "Me faz sentir que estou fazendo a coisa certa, o meu papel no mundo."
    j "Poxa, Linne, isso é lindo!"
    j "N-não foi uma decisão muito difícil pra você, n-né?"
    l "Nem um pouco!"
    j "Ahh, he he... Que bom..."
    j "Bem... Admito q-que não foi tão fácil assim para mim..."    
    n "Também não foi no meu caso."
    n "É que, tipo... Eu queria seguir carreira no rap..."
    n "E meio que ser trainee e debutar era a opcão mais 'fácil'."
    j "Sim, sim!"
    j "Mesmo sendo a forma mais 'fácil' de ser artista, também é uma das formas mais puxadas..."