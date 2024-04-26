google.charts.load('current', {
    packages: ['corechart', 'geochart']
  });
  google.charts.setOnLoadCallback(drawCharts);
  
  function drawCharts() {
    // Gráfico Geográfico
    var dataBrazil = google.visualization.arrayToDataTable([
        ['Estado', 'Inscritos'],
        ['ACRE',  2500], // Acre
        ['ALAGOAS',  7000], // Alagoas
        ['AMAPÁ',  5000], // Amapá
        ['AMAZONAS',  4000], // Amazonas
        ['BAHIA',  8000], // Bahia
        ['CEARÁ',  3000], // Ceará
        ['DISTRITO FEDERAL',  5500], // Distrito Federal
        ['ESPÍRITO SANTO',  8500], // Espírito Santo
        ['GOIÁS',  4500], // Goiás
        ['MARANHÃO',  6500], // Maranhão
        ['MATO GROSSO',  7500], // Mato Grosso
        ['MATO GROSSO DO SUL',  2500], // Mato Grosso do Sul
        ['MINAS GERAIS',  9500], // Minas Gerais
        ['PARÁ',  7200], // Pará
        ['PARAÍBA',  4000], // Paraíba
        ['PARANÁ',  8800], // Paraná
        ['PERNAMBUCO',  5500], // Pernambuco
        ['PIAUÍ',  7000], // Piauí
        ['RIO DE JANEIRO',  9000], // Rio de Janeiro
        ['RIO GRANDE DO NORTE',  4000], // Rio Grande do Norte
        ['RIO GRANDE DO SUL',  8000], // Rio Grande do Sul
        ['RONDÔNIA',  3500], // Rondônia
        ['RORAIMA',  2500], // Roraima
        ['SANTA CATARINA',  9000], // Santa Catarina
        ['SÃO PAULO',  11000], // São Paulo
        ['SERGIPE',  4500], // Sergipe
        ['TOCANTINS',  5000] // Tocantins
    ]);
  
    var optionsBrazil = {
      region: 'BR',
      displayMode: 'regions',
      resolution: 'provinces',
      colorAxis: { colors: ['#f0ad4e', '#d9534f'] },
      legend: { textStyle: { color: 'blue', fontSize: 14 } }
    };
  
    var chartBrazilWrapper = new google.visualization.ChartWrapper({
      chartType: 'GeoChart',
      containerId: 'brazil_chart',
      dataTable: dataBrazil,
      options: optionsBrazil
    });
  
    chartBrazilWrapper.draw();
  
    // Gráfico de Colunas
    var Graph1 = google.visualization.arrayToDataTable(dataGraph1);
    
    var optionsGraph1 = {
      height: 300,
      bar: { groupWidth: "95%" },
      legend: { position: "none" },
      chartArea: { width: '90%', height: '70%' },
      colors: ['#b87333'],
      hAxis: { title: 'Faixa Etária' },
      vAxis: { title: 'Quantidade de Inscritos' },
      tooltip: { isHtml: true, trigger: 'focus' },
      theme : 'material',
    };
  
    var chartGraph1Wrapper = new google.visualization.ChartWrapper({
      chartType: 'ColumnChart',
      containerId: 'barchart_values',
      dataTable: Graph1,
      options: optionsGraph1
    });
  
    chartGraph1Wrapper.draw();
  
    /////////////////////////////////////////////////////////////////////////////////////////
        ///////////////////Gráfico 2//////////////////////
        var Graph2 = google.visualization.arrayToDataTable(dataGraph2);
    
        var optionsGraph2 = {
          height: 300,
          bar: { groupWidth: "95%" },
          legend: { position: "none" },
          chartArea: { width: '90%', height: '70%' },
          colorAxis: { colors: ['#f0ad4e', '#d9534f'] },
          series : {},
          hAxis: { title: 'Estudantes', ticks : [] },
          vAxis: { title: 'Média de Nota' },
          theme : 'material',
        };
      
        var chartGraph2Wrapper = new google.visualization.ChartWrapper({
          chartType: 'ScatterChart',
          containerId: 'scatterchart_values',
          dataTable: Graph2,
          options: optionsGraph2
        });
      
        chartGraph2Wrapper.draw();
        /////////////////////////////////////////////////////////////////////////////////////////
        ///////////////////Gráfico 3//////////////////////
        var Graph3 = google.visualization.arrayToDataTable(dataGraph3);
    
        var optionsGraph3 = {
          height: 300,
          bar: { groupWidth: "90%" },
          legend: { position: "none" },
          chartArea: { width: '80%', height: '70%' },
          colorAxis: { colors: ['#f0ad4e', '#d9534f'] },
          series : {},
          hAxis: { title: 'Variáveis', ticks : []},
          vAxis: { title: 'Correlação' },
          theme : 'material',
        };
  
        var chartGraph3Wrapper = new google.visualization.ChartWrapper({
          chartType: 'ColumnChart',
          dataTable: Graph3,
          options: optionsGraph3,
          containerId: 'correlation_chart'
        });
  
        chartGraph3Wrapper.draw();
        /////////////////////////////////////////////////////////////////////////////////////////
}