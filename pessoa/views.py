from django.shortcuts import redirect, render , get_object_or_404 
from pessoa.models import Sobrevivente
from django.db.models import Avg, Sum
# Create your views here.

def home(request):
    return render(request, 'home.html', {'nome' : 'kastier'})

def adicionar_sobrevivente(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        idade = request.POST['idade']
        sexo = request.POST['sexo']
        localizacao = request.POST['localizacao']
        agua = request.POST['agua']
        medicamento = request.POST['medicamento']
        comida = request.POST['comida']
        municao = request.POST['municao']
        pontos = (int(agua) * 4) + (int(medicamento) * 3) + (int(comida) * 2) + int(municao)
        sobrevivente = Sobrevivente(nome=nome, idade=idade, sexo=sexo, localizacao=localizacao, agua=agua, medicamento=medicamento, comida=comida, municao=municao, pontos=pontos)
        sobrevivente.save()
        return redirect('lista_nao_infectados')
    else:
        return render(request, 'adicionar_sobrevivente.html')
    
def lista_nao_infectados(request):
    sobreviventes = Sobrevivente.objects.filter(infectado=False)
    context = {'sobreviventes': sobreviventes}
    return render(request, 'lista_nao_infectados.html', context)

def lista_infectados(request):
    sobreviventes = Sobrevivente.objects.filter(infectado=True)
    context = {'sobreviventes': sobreviventes}
    return render(request, 'lista_infectados.html', context)

def atualizar_sobrevivente(request, sobrevivente_id):
    sobrevivente = get_object_or_404(Sobrevivente, id=sobrevivente_id)
    if request.method == 'POST':
        sobrevivente.localizacao = request.POST['localizacao']
        sobrevivente.denuncias = int(request.POST['denuncias'])
        sobrevivente.save()
        if sobrevivente.denuncias >= 3:
            sobrevivente.infectado = True
            sobrevivente.save()
            return redirect('lista_infectados')
        else:
            return redirect('lista_nao_infectados')
    else:
        context = {'sobrevivente': sobrevivente}
        return render(request, 'atualizar_sobrevivente.html', context)

def dados(request):
    # Quantidade de sobreviventes não infectados
    nao_infectados = Sobrevivente.objects.filter(infectado=False).count()
    
    # Quantidade de sobreviventes infectados
    infectados = Sobrevivente.objects.filter(infectado=True).count()
    
    # Média de itens dos sobreviventes
    media_agua = Sobrevivente.objects.aggregate(Avg('agua'))['agua__avg']
    media_medicamento = Sobrevivente.objects.aggregate(Avg('medicamento'))['medicamento__avg']
    media_comida = Sobrevivente.objects.aggregate(Avg('comida'))['comida__avg']
    media_municao = Sobrevivente.objects.aggregate(Avg('municao'))['municao__avg']
    
    # Somar a quantidade de pontos dos infectados (que são os pontos perdidos)
    pontos_infectados = Sobrevivente.objects.filter(infectado=True).aggregate(Sum('pontos'))['pontos__sum']
    
    # Média de idade dos sobreviventes
    media_idade = Sobrevivente.objects.aggregate(Avg('idade'))['idade__avg']
    
    # Quantidade de sobreviventes por gênero
    homens = Sobrevivente.objects.filter(sexo='M').count()
    mulheres = Sobrevivente.objects.filter(sexo='F').count()
    
    context = {
        'nao_infectados': nao_infectados,
        'infectados': infectados,
        'media_agua': media_agua,
        'media_medicamento': media_medicamento,
        'media_comida': media_comida,
        'media_municao': media_municao,
        'pontos_infectados': pontos_infectados,
        'media_idade': media_idade,
        'homens': homens,
        'mulheres': mulheres,
    }
    return render(request, 'dados.html', context)



def troca(request):
    return render(request, 'troca.html')
