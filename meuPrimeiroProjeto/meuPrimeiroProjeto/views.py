from django.http import HttpResponse
from django.shortcuts import render

def hello (request):
    return render(request, 'index.html')

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


def fidade (request, nome):
    idade = lerDoBanco(nome)['idade']
    return render(request, 'pessoa.html', {'v_idade': idade})
