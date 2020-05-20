function buildPlot() {
    var horseData = [];
    let horseBeyer = [];
    Plotly.d3.csv('../../static/data/horses.csv', (data) => {
        for (i = 0; i < data.length; i ++) {
            horseData.push(data[i].Horse);
        }
        console.log(horseData);

        for (i = 0; i < data.length; i ++) {
            horseBeyer.push(data[i].Beyer);
        }
        console.log(horseBeyer);

        let obj_1 = (horseData,horseBeyer).map((a,b) => ({'horse': horseData[b], 'beyer': parseInt(a, 10)}))
        console.log(obj_1)
        var tmp = {};
        obj_1.forEach(function(item){

            var obj =  tmp[item.horse] = tmp[item.horse] || {count:0, total: 0};
            obj.count ++;
            obj.total +=item.beyer
        });
        var res = Object.entries(tmp).map(function(entry){
            return { horse: entry[0], beyerAve: (entry[1].total/entry[1].count)}
        })
        console.log(res)
        beyerAvg = []
        for (i = 0; i < res.length; i ++) {
            beyerAvg.push(res[i].beyerAve);
        }
        console.log(beyerAvg)
        horseSingle = []
        for (i = 0; i < res.length; i ++) {
            horseSingle.push(res[i].horse);
        }
        console.log(horseSingle)

        var data = [
            {
              x: horseSingle,
              y: beyerAvg,
              type: 'bar'
            }
          ];
        var layout = {
            title: "Horse vs Beyer(Avg Speed) ",
            xaxis: { title: "Horse Name" },
            yaxis: { title: "Beyer (Average Speed)"}
          };

        Plotly.newPlot('graph', data, layout);
    });
};
buildPlot();
//         for (i = 0; i < data.length; i ++) {

//             if (data[i].Horse === data[i++].Horse) {
//                 horseData.push(data[i].Horse); 
//             }
//             else {
//                 horseData.push(data[i++].Horse); 
//             }
//         }
//         horseData_1 = [new Set(horseData)]
//         console.log(horseData_1)


//         for (i = 0; i < data.length; i ++) {
//             horseBeyer.push(data[i].Beyer);
//         }
//         console.log(horseBeyer);

//         let dict = (horseData,horseBeyer).map((a,b) => ({'horse': horseData[b], 'beyer': a}))
 
//         console.log(dict)

//         console.log(horseData);

//     });
// };

// buildPlot();
