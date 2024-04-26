from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.contrib.auth.decorators import login_required

def mainpage(request):
    return render(request, 'mainpage.html')


@login_required
def detail_dashboard(request, id):
    graphs = request.session.get('graphs')
    
    graph_data = graphs.get(f'graph{id}')
    if graph_data:
        return render(request, 'detail_dashboard.html', {'graph_data': graph_data})
    else:
        return HttpResponseNotFound("Gráfico não encontrado")



# Create your views here.


