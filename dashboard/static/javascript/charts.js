google.charts.load('current', {
    packages: ['corechart', 'geochart']
  });
  google.charts.setOnLoadCallback(drawCharts);
  
  function drawCharts() {
    // Gráfico Geográfico
    var dataBrazil = google.visualization.arrayToDataTable([
        ['Estado', 'Inscritos'],
        ['ACRE',  2500], 
        ['ALAGOAS',  7000],
        ['AMAPÁ',  5000], 
        ['AMAZONAS',  4000],
        ['BAHIA',  8000], 
        ['CEARÁ',  3000], 
        ['DISTRITO FEDERAL',  5500], 
        ['ESPÍRITO SANTO',  8500], 
        ['GOIÁS',  4500], 
        ['MARANHÃO',  6500],
        ['MATO GROSSO',  7500],
        ['MATO GROSSO DO SUL',  2500], 
        ['MINAS GERAIS',  9500], 
        ['PARÁ',  7200],
        ['PARAÍBA',  4000],
        ['PARANÁ',  8800], 
        ['PERNAMBUCO',  5500], 
        ['PIAUÍ',  7000], 
        ['RIO DE JANEIRO',  9000],
        ['RIO GRANDE DO NORTE',  4000], 
        ['RIO GRANDE DO SUL',  8000], 
        ['RONDÔNIA',  3500], 
        ['RORAIMA',  2500], 
        ['SANTA CATARINA',  9000],
        ['SÃO PAULO',  11000], 
        ['SERGIPE',  4500], 
        ['TOCANTINS',  5000]
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