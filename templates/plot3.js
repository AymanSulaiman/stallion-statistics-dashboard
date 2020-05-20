function buildPlot() {

    var rcRace = [];
    var distance = [];

    Plotly.d3.csv('../ETL/data/op_races.csv', (data) => {

        for (i = 0; i < data.length; i ++) {
            rcRace.push(data[i].RCRace);
            distance.push(data[i].Distance);
        }
        console.log(rcRace);
        console.log(distance);

        var rcRaceInt = rcRace.map(x => parseInt(x));
        var distanceInt = distance.map(y => parseFloat(y));

        console.log(rcRaceInt);
        console.log(distanceInt);

        var data = [{
            x: rcRaceInt,
            y:distanceInt,
            mode: 'markers',
            type: 'scatter',
            text: ['Race 1','Race 2','Race 3','Race 4','Race 5','Race 6','Race 7','Race 8','Race 9','Race 10','Race 11','Race 12','Race 13','Race 14'],
            marker: {size: 12, color: '#900c3f'}
          }];
          
          var layout = {
            title:'Race Number vs Distance (Furlong)',
            xaxis: { title: "Horse Name", range: [0,15] },
            yaxis: { title: "Sale Price (USD)", range: [0,12]},
          };
          
          Plotly.newPlot('graph4', data, layout); 
        });
};

buildPlot();