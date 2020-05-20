function buildPlot() {
    purse_1 = [];
    RCRace_1 = [];
    conditions = [];
    Plotly.d3.csv('../../static/data/op_races.csv', (data) => {
        console.table(data)
        for (i = 0; i < data.length; i ++) {
            purse_1.push(data[i].Purse);
            RCRace_1.push(data[i].RCRace);
            conditions.push(`Race ${data[i].RCRace}<br>Long Class:<br>${data[i].LongClass}`);
        }
        console.log(purse_1);
        console.log(RCRace_1);
        let purse_2 = purse_1.map(x => x.replace(/k/g, ''));
        console.log(purse_2)
        let purse_3 = purse_2.map(x => x.replace(/\$/g, ''));
        console.log(purse_3)
        let purse_4 = purse_3.map(x => 100000 * parseFloat(x))
        console.log(purse_4)
        RCRace_2 = RCRace_1.map(x => parseInt(x))
        console.log(RCRace_2)
        var data_2 = [
            {
              x: RCRace_2,
              y: purse_4,
              type: 'scatter',
              text: conditions,
              marker: {
                color: '#2b580c'
              }
            }
          ];
        var layout_2 = {
            title: "Race Number vs Total Winnings(USD)",
            xaxis: { title: "Race Number" },
            yaxis: { title: "Total Winnings (USD)"}
          };
        Plotly.newPlot('graph5', data_2, layout_2);
    });
};
buildPlot();