from django.shortcuts import render


def get_graphic():
    return[
            {'id':1,
             'titulo':'Relação da quantidade de imóveis que aceitam pets.',
            'url_img':'image/graph_pet.png',
            'descricao':'Este gráfico de barras compara a quantidade de imóveis que aceitam e não aceitam animais em diferentes cidades. Essa visualização oferece insights sobre a distribuição da política de aceitação de animais em diferentes localidades.',
            'detalhamento': "Este gráfico de barras proporciona uma análise detalhada da aceitação de animais em imóveis, apresentando uma comparação entre aqueles que acolhem nossos amigos de estimação e os que não o fazem em diversas cidades. Ao examinar a distribuição dessa política em diferentes localidades, é possível extrair valiosos insights sobre as preferências e restrições relacionadas a animais de estimação. A visualização destaca nuances nas práticas imobiliárias, permitindo uma compreensão mais profunda das tendências e variações nas políticas de aceitação de animais ao longo das diferentes regiões."},
            {'id':2,
             'titulo':'Relação da quantidade de imóveis em cada estado.',
            'url_img':'image/cidades_mais.png',
            'descricao':'Este gráfico de barras ilustra a quantidade de imóveis disponíveis em cada cidade. Cada barra representa a quantidade de imóveis, permitindo uma rápida comparação entre as diferentes localidades.',
            'detalhamento': "Este envolvente gráfico de barras oferece uma representação visual da disponibilidade de imóveis em diversas cidades. Cada barra meticulosamente delineada reflete a quantidade de residências disponíveis em uma determinada localidade, proporcionando uma visão panorâmica e comparativa da oferta imobiliária. Essa representação gráfica simplifica a análise, permitindo uma rápida e eficaz comparação entre as diferentes cidades. Ao explorar as alturas das barras, é possível discernir padrões e discrepâncias na disponibilidade de imóveis, proporcionando uma valiosa compreensão das dinâmicas do mercado imobiliário em cada região."},
            {'id':3,
             'titulo': 'Média do valor do aluguel por número de quartos',
            'url_img':'image/aluguel.png',
            'descricao':'Este gráfico de barras apresenta a média do valor do aluguel em relação ao número de quartos em imóveis. Cada barra representa uma quantidade específica de quartos, permitindo uma visualização rápida das tendências no valor do aluguel conforme o número de quartos aumenta.',
            'detalhamento':'Este gráfico de barras evidencia uma correlação entre o número de quartos em imóveis e a média do valor do aluguel. A tendência ascendente sugere que propriedades com mais quartos têm, em média, valores de aluguel superiores. Esse insight indica que o tamanho do imóvel desempenha um papel significativo na determinação dos preços de aluguel, oferecendo uma visão valiosa para locatários e proprietários no mercado imobiliário.'}
            ]



def mainpage(request):
    return render(request, 'mainpage.html')

def dashboards(request):
    graphics = get_graphic()
    return render(request, 'dashboards.html', {'graphics' : graphics})

def detail_dashboard(request, id):
    graphics = get_graphic()
    graphic = next(filter(lambda g: g['id'] == id, graphics), None)

    if graphic is not None:
        return render(request, 'detail_dashboard.html', {'graphic': graphic})
    else:
        return render(request, '404.html')  



# Create your views here.


