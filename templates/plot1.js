var years = ['2014', '2015', '2016']

Plotly.d3.csv('../ETL/data/horses.csv', (data) => {
    console.log(data)
//   var data = years.map(y => {
//     var d = rows.filter(r => r.year === y)
    
//     return {
//       type: 'bar',
//       name: y,
//       x: d.map(r => r.dealer),
//       y: d.map(r => r.sales)
//     }
//   })
  
//   Plotly.newPlot('graph', data)
})
