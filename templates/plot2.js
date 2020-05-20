function buildPlot() {
    var trainer_1 = [];
    let earnings_1 = [];
    let horses_1 = [];
    let sale_price_1 = [];
    Plotly.d3.csv('../ETL/data/race_11.csv', (data) => {
        console.table(data)
        for (i = 0; i < data.length; i ++) {
            trainer_1.push(data[i].Trainer);
            earnings_1.push(data[i].Earnings);
        }
        console.log(trainer_1);
        console.log(earnings_1);
        for (i = 0; i < data.length; i ++) {
            horses_1.push(data[i].Horse);
            sale_price_1.push(data[i].SalePrice)
        }
        console.log(horses_1);
        console.log(sale_price_1);
        let sale_price_2 = sale_price_1.map(x => x.replace(/k/g, ''));
        let sale_price_3 = sale_price_2.map(x => x.replace(/\$/g, ''));
        console.log(`sale_price_3: ${sale_price_3}`)
        console.log(typeof sale_price_2[0])
        let sale_price_4 = sale_price_3.map(x => x*100000)
        console.log(sale_price_4)

        var data_1 = [
            {
              x: trainer_1,
              y: earnings_1,
              type: 'bar',
              marker: {
                color: 'red'
              }
            }
          ];
        var layout_1 = {
            title: "Trainer vs Earnings",
            xaxis: { title: "Trainer Name" },
            yaxis: { title: "Earnings (USD)"},

          };
        Plotly.newPlot('graph2', data_1, layout_1);

        var data_2 = [
            {
              x: horses_1,
              y: sale_price_4,
              type: 'bar',
              marker: {
                color: '#1f4068'
              }
            }
          ];
        var layout_2 = {
            title: "Horses vs Sale Price",
            xaxis: { title: "Horse Name" },
            yaxis: { title: "Sale Price (USD)"}
          };
        Plotly.newPlot('graph3', data_2, layout_2);
    });
};
buildPlot();