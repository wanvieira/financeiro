def definir_categoria(descricao):

    descricao = descricao.lower()

    categorias = {

        'alimentacao':[
            'burger',
            'mc',
            'ifood',
            'pizza'
        ],

        'tecnologia':[
            'kabum',
            'amazon',
            'pichau'
        ],

        'lazer':[
            'netflix',
            'cinema',
            'spotify'
        ]
    }

    for categoria, palavras in categorias.items():

        for palavra in palavras:

            if palavra in descricao:

                return categoria

    return 'Outros'