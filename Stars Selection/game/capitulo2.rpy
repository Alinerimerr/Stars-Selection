label cap2_1:

    "Mais uma manhã..."
    "Ahh... Parece que tenho que voltar a treinar."
    "Não quero acabar como Roko..."
    "Ao sair do meu quarto, escuto Juni e Nádia conversando na sala de estar."
    n "... Isso me lembra da minha época de colegial."
    j_n "C-colegial?"
    j_m "Uhh, tenho más lembraças de lá."
    j_m "Sinto um frio na espinha só de pensar..."

    #"Oh, esse parece um tópico sensivel de Juni."
    "Melhor eu não me intrometer..."
    
    "Enquanto me preparava para começar meu treinamento, alguns funcionários da produção avisam que o apresentador que falar comigo o mais cedo possível."
    "Fui conduzida até sua sala."
    Sr "Srta.Monnie! Por favor, sente-se."
    m "Huh... Claro."
    "O que será que ele quer?"
    Sr_n "Bom, Srta... Tenho observado que você é, realmente, bem carismática..."
    Sr "Por isso, te ofereço um acordo especial."
    m "Um acordo...?"
    Sr "Sim. Mas antes, gostaria que ficasse sabendo de algumas coisas."
    Sr_n "Com saída de Roko, acabei perdendo um pouco do investimento para o reality..."
    Sr_n "Ela era um grande imã de dinheiro..."
    Sr "Felizmente, esse investimento pode retornar dependendo da audiencia do programa."
    Sr "E é aí que você entra."
    m "C-como assim?"
    Sr "Não sei se a srta sabe, mas a sua figura é importante!"
    Sr "Tanto para o público... Quanto para as outras participantes do programa."
    Sr "Suas interações tem efeito... E as pessoas gostam disso!"
    Sr_n "Então, o acordo é simples:"
    Sr "Você se torna minha agente..."
    Sr "Me passando informações e manipulando algumas coisas no jogo."
    # desenvolver melhor essa parte p melhor entendimento
    Sr "E em troca recebe benefícios como um empurrãozinho nas avaliações, grandes ofertas ou ferramentas exclusivas."
    Sr "O que acha?"
    menu(nvl=True):
        "Não sei...":
            m "Não tenho certeza..."
            Sr "Ah, está tudo bem ficar dúvida."
            Sr_n "Mas caso mude de ideia..."
        "Gostei da ideia!":
            m "Parece um bom negocio."
            m "Eu aceito a proposta!"
            Sr "Sabia que aceitaria!"

    Sr "Leve este telefone como você."
    "Sr.Star me entrega um celular comum."
    Sr "Ele tem acesso a Internet e a srta. pode me contatar quando quiser."
    m "Mas celulares não são permitidos..."
    Sr "Ora, não se preocupe com isso!"
    Sr "Eu controlo tudo aqui dentro. Posso facilmente apagar qualquer evidencia a respeito disso."
    Sr_n "Ah! Mas é melhor manter isso loge das outras competidoras."
    Sr_n "Podemos ter problemas caso elas saibam..."
    
    Sr "Bom, srta. Moonie, está dispensada."

    # encerramento do dialogo e reflexao 

    #Havera a oportunidade de falar com juni sobre seu passado sombrio de escola
    #e escolha entre vazar essa informacao p apresentador ou n.

    menu(nvl=True):
        "Passar informações":
            $ vazamento = True
            $ karma = 15

        "Não passar":
            m "sheeeesh"

label cap2_2:
    "hihihehehuhuhuhu"

    #evento no qual Juni sera escolhida 
