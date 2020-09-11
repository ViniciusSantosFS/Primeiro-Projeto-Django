from django.http import HttpResponse
def hello (request):
    return HttpResponse ("Ola Mundo");

def numero (request, year):
    return HttpResponse('O ano enviado foi: ' + str(year))


def lerDoBanco(nome): #função para simular a leitura do banco de dados
    Lista_nomes = [
        {"nome": "Ana", "idade": 20},
        {"nome": "Pedro","idade": 19},
        {"nome": "Lucas", "idade": 18}
    ]
    for pessoa in Lista_nomes:
        if pessoa ["nome"] == nome:
            return pessoa
    else :
        return {"nome": "Não encontrado", "idade": 0}

def fname (request, nome ):
    result = lerDoBanco(nome)
    if result["idade"] > 0:
        return HttpResponse( "o nome é " + result["nome"] + " e a idade " +  str(result['idade'])+ " anos" )
    else:
        return HttpResponse("Pessoa não encontrada")