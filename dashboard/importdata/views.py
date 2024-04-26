from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count, IntegerField, F
from django.db.models.functions import Cast
from .models import Dados
from random import sample
import numpy as np
import json
import pandas as pd


# Create your views here.
@login_required
def data_extract(request):
    #### Gráfico 1#####
    query1 = Dados.objects.annotate(
        faixa_idade_int=Cast('faixa_idade', IntegerField())
    ).values('faixa_idade_int'
    ).annotate(inscricoes=Count('inscricao')
    ).order_by('faixa_idade_int')

    queryformated1 = [["Faixa de idade", "Inscritos"]]
    for i in query1:
        queryformated1.append([i['faixa_idade_int'], i['inscricoes']])
    data1 = json.dumps(queryformated1)
    hue1 = [0]
    subtitle = json.dumps({
                        1: "> 17 anos",
                        2: "17 anos",
                        3: "18 anos",
                        4: "19 anos",
                        5: "20 anos",
                        6: "21 anos",
                        7: "22 anos",
                        8: "23 anos",
                        9: "24 anos",
                        10: "25 anos",
                        11: "26 - 30 anos",
                        12: "31 - 35 anos",
                        13: "36 - 40 anos",
                        14: "41 - 45 anos",
                        15: "46 - 50 anos",
                        16: "51 - 55 anos",
                        17: "56 - 60 anos",
                        18: "61 - 65 anos",
                        19: "66 - 70 anos",
                        20: "< 70 anos"
                    }, ensure_ascii=False)
    

    ##########################
    #### Gráfico 2#####
    query2 = Dados.objects.filter(MEDIA__gt=0).values('id', 'MEDIA', 'sexo')
    for item in query2:
        item['MEDIA'] = float(item['MEDIA'])
        item['sexo'] = 0 if item['sexo'] == 'M' else 1
    query2 = sample(list(query2), 1000)
    queryformated2 = [["id", "Media"]]
    hue = []
    for i in query2:
        queryformated2.append([i['id'], i['MEDIA']])
        hue.append(i['sexo'])
    data2 = json.dumps(queryformated2)
    hue2 = json.dumps(hue)
    ##########################
    #### Gráfico 3#####
    query3 = Dados.objects.values('conclusao_status', 'tipo_escola', 'CN', 'CH', 'LC', 'MT', 'REDACAO', 'MEDIA')
    query3 = pd.DataFrame(sample(list(query3), 1000)).corr()['MEDIA'].tolist()
    query3 = [float(correlation) for correlation in query3]
    queryformated3 = [['conclusao_status', 'tipo_escola', 'CN', 'CH', 'LC', 'MT', 'REDACAO', 'MEDIA']]
    queryformated3.append(query3)    
    print(query3)
    print(queryformated3)
    data3 = json.dumps(queryformated3)

    ##########################

    graphs = {
    "graph1": {
        "tag_id": 1,
        "containerId" : "barchart_values",
        "chart_type": "ColumnChart",
        "data": data1,
        "description": "Os dados mostram que a faixa etária com a maior quantidade de inscritos é a de 18 anos, com um total de 15.578 inscrições. Isso sugere um forte interesse ou participação nessa faixa etária em relação aos demais grupos. Por outro lado, faixas etárias mais jovens ou mais avançadas podem apresentar oportunidades para estratégias de captação específicas, considerando-se a diferença de participação em comparação com a faixa dos 18 anos.",
        "legend": "Legenda: \n\u2022 1: Menor de 17 anos \n\u2022 2: 17 anos \n\u2022 3: 18 anos \n\u2022 4: 19 anos \n\u2022 5: 20 anos \n\u2022 6: 21 anos \n\u2022 7: 22 anos \n\u2022 8: 23 anos \n\u2022 9: 24 anos \n\u2022 10: 25 anos \n\u2022 11: Entre 26 e 30 anos \n\u2022 12: Entre 31 e 35 anos \n\u2022 13: Entre 36 e 40 anos \n\u2022 14: Entre 41 e 45 anos \n\u2022 15: Entre 46 e 50 anos \n\u2022 16: Entre 51 e 55 anos \n\u2022 17: Entre 56 e 60 anos \n\u2022 18: Entre 61 e 65 anos \n\u2022 19: Entre 66 e 70 anos \n\u2022 20: Maior de 70 anos",
        "title" : "Quantidade de Inscritos por Faixa Etária",
        "hAxis" : "Faixa Etária",
        "vAxis" : "Quantidade de Inscritos",
        "hue" : hue1,
        "subtitle" : subtitle,
        "theme" : "material"
    },
    "graph2": {
        "tag_id": 2,
        "containerId" : "scatterchart_values",
        "chart_type": "ScatterChart",
        "data": data2,
        "description" : "Analisando o gráfico de dispersão dos resultados do ENEM de 2022, observa-se uma distribuição uniforme dos dados, indicando uma consistência notável nas notas médias dos estudantes. No eixo x, cada ponto representa um estudante, enquanto no eixo y, temos as respectivas notas médias obtidas por eles. Surpreendentemente, a dispersão dos pontos ao longo do gráfico é mínima, sugerindo que houve uma tendência geral de desempenho sem grandes variações. Essa uniformidade nos resultados sugere que os estudantes, de maneira geral, alcançaram pontuações próximas entre si, refletindo uma consistência notável no desempenho coletivo no ENEM de 2022.",
        "legend" : "Cada ponto representa um candidato e sua respectiva média.",
        "title" : "Dispersão das médias dos candidatos",
        "hAxis" : "ID",
        "vAxis" : "Nota Média",
        "hue" : hue2,
        "theme" : "material"
    },
    "graph3": {
        "tag_id": 3,
        "containerId":"correlation_chart",
        "title" : "Correlação das variáveis com a média",
        "hAxis" : "Variáveis",
        "chart_type": "ColumnChart",
        "data": data3,
        "description" : "A análise do gráfico de barras revela insights valiosos sobre a correlação das variáveis com a média das notas dos estudantes no Exame Nacional do Ensino Médio (Enem) de 2022. Observamos que a variável 'tipo de escola' apresenta uma correlação modesta com a média das notas, indicando que o tipo de instituição de ensino frequentada pelos estudantes pode ter um impacto moderado em seu desempenho geral. Por outro lado, as disciplinas específicas - Ciências da Natureza, Ciências Humanas, Linguagens e Códigos e Matemática - exibem correlações significativas com a média das notas. Esses resultados sugerem que o desempenho dos estudantes em disciplinas individuais pode ter uma influência substancial em sua média geral. Além disso, a nota da redação mostra uma forte correlação com a média, destacando a importância da habilidade de escrita na avaliação global dos estudantes. Essas observações fornecem insights valiosos para educadores, formuladores de políticas e pesquisadores interessados em compreender os fatores que contribuem para o desempenho dos estudantes no Enem de 2022.",
        "legend": "Legenda: \n\u2022 tipo_escola: Se a escola é particular ou pública \n\u2022 CN: Ciências da Natureza \n\u2022 CH: Ciências Humanas \n\u2022 LC: Linguagens e Códigos \n\u2022 MT: Matemática",
        "theme" : "material"
    },
}

    request.session['graphs'] = graphs
    return render(request, 'dashboards.html', {'graphs' : graphs})
