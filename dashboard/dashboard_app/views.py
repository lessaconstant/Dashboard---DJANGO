from django.shortcuts import render


def get_graphic():
    return[
            {'id':1,
            'url_img':'image/graph_pet.png',
            'descricao':'Este gráfico de barras compara a quantidade de imóveis que aceitam e não aceitam animais em diferentes cidades. Essa visualização oferece insights sobre a distribuição da política de aceitação de animais em diferentes localidades.'},
            {'id':2,
            'url_img':'image/cidades_mais.png',
            'descricao':'Este gráfico de barras ilustra a quantidade de imóveis disponíveis em cada cidade. Cada barra representa a quantidade de imóveis, permitindo uma rápida comparação entre as diferentes localidades.'},
            {'id':3,
            'url_img':'image/graph_pet.png',
            'descricao':'Este gráfico de barras compara a quantidade de imóveis que aceitam e não aceitam animais em diferentes cidades. Essa visualização oferece insights sobre a distribuição da política de aceitação de animais em diferentes localidades.'},
            {'id':4,
            'url_img':'image/graph_pet.png',
            'descricao':'Este gráfico de barras compara a quantidade de imóveis que aceitam e não aceitam animais em diferentes cidades. Essa visualização oferece insights sobre a distribuição da política de aceitação de animais em diferentes localidades.'},
            ]



def mainpage(request):
    return render(request, 'mainpage.html')

def dashboards(request):
    graphics = get_graphic()
    return render(request, 'dashboards.html', {'graphics' : graphics})
# Create your views here.
