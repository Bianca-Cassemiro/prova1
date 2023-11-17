import re


def pagamento_resposta(_):
    return "Vamos analisar o seu crédito, um momento"

def pedido_resposta(_):
    return "Vou verificar o status do pedido!"

intent_dict = {
    "pagamento":
    [
    r"Como posso atualizar meu cartão de crédito",
    r" Preciso mudar a forma de pagamento, o que fazer",
    r" Quero atualizar minhas informações de pagamento" ,
    r"Método de pagamento desatualizado",
    r"Como proceder para atualizar"
    ],
    "status_pedido":
    [
    r"Onde vejo o status do meu pedido",
    r"Como faço para rastrear meu pedido",
    r"Quero saber onde está meu pedido, como faço", 
    r"Status de entrega, como consultar"
    ]
}

action_dict = {
        "pagamento": pagamento_resposta,
        "status_pedido": pedido_resposta
}

command = input("Digite o seu comando: ")


for intention, patterns in intent_dict.items():
    for key in patterns:
        match = re.match(key, command, re.IGNORECASE)
        if match:
            resposta = action_dict[intention](match)
            print(resposta)
