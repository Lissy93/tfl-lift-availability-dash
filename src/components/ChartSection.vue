<template>
    <el-card>
        <h2>Stats</h2>

        <div class="charts">
            <apexchart
                type="donut"
                width="350"
                height="350"
                :options="donutOptions"
                :series="donutSeries"
            />

            <apexchart
                type="bar"
                width="350"
                height="250"
                :options="barOptions"
                :series="barSeries" />

            <apexchart
                type="bubble"
                width="350"
                height="250"
                :options="bubbleOptions"
                :series="bubbleSeries"
                />

        </div>
    </el-card>
</template>

<script>

import VueApexCharts from 'vue-apexcharts'

 function generateData(baseval, count, yrange) {
      var i = 0;
      var series = [];
      while (i < count) {
        var x = Math.floor(Math.random() * (750 - 1 + 1)) + 1;
        var y = Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;
        var z = Math.floor(Math.random() * (75 - 15 + 1)) + 15;

        series.push([x, y, z]);
        baseval += 86400000;
        i++;
      }
      return series;
    }

export default {
  name: 'ChartSection',
  components: {
    apexchart: VueApexCharts
    },
  data: function() {
      return {
        donutOptions: {
          labels: ['Operational', 'Restricted', 'Critical'],
          colors:['#67C23A', '#E6A23C', '#F56C6C'],
          title: {
              text: 'Proportion of Operational Lifts',
              style: {
                fontSize:  '18px',
                color:  '#113B92'
              },
          },
        },
        donutSeries: [91, 3, 6],

        barSeries: [{
          name: 'Operational',
          data: [98, 94, 95, 81, 98]
        }, {
          name: 'Restricted',
          data: [2, 2, 4, 10, 1]
        }, {
          name: 'Critical',
          data: [0, 4, 1, 9, 1]
        }
        ],
        barOptions: {
          title: {
              text: 'Operational Lifts Per Week',
              style: {
                fontSize:  '18px',
                color:  '#113B92'
              },
          },
          colors:['#67C23A', '#E6A23C', '#F56C6C'],
          chart: {
            stacked: true,
            toolbar: {
              show: false,
            },
          },
          plotOptions: {
            bar: {
              horizontal: false,
            },
          },
          xaxis: {
            type: 'datetime',
            categories: ['01/01/2011 GMT', '01/02/2011 GMT', '01/03/2011 GMT', '01/04/2011 GMT',
              '01/05/2011 GMT'
            ],
          },
          legend: {
            position: 'right',
            offsetY: 40
          },
          fill: {
            opacity: 1
          }
        },


        bubbleSeries: [{
            name: 'Operational',
            data: generateData(new Date('11 Feb 2017 GMT').getTime(), 20, {
              min: 10,
              max: 60
            })
          },
          {
            name: 'Restricted',
            data: generateData(new Date('11 Feb 2017 GMT').getTime(), 20, {
              min: 10,
              max: 60
            })
          },
          {
            name: 'Critical',
            data: generateData(new Date('11 Feb 2017 GMT').getTime(), 20, {
              min: 10,
              max: 60
            })
          },
        ],

        bubbleOptions: {
          colors:['#67C23A', '#E6A23C', '#F56C6C'],
          dataLabels: {
            enabled: false
          },
          chart: {
              toolbar: {
              show: false,
            },
          },
          fill: {
            opacity: 0.8
          },
          title: {
            text: 'Incident Duration over Time',
            style: {
                fontSize:  '18px',
                color:  '#113B92'
              },
          },
          xaxis: {
            tickAmount: 12,
            type: 'category',
          },
          yaxis: {
            max: 70
          }
        }
      }
    },
}
</script>

<style scoped lang="scss">

.el-card {
    display: flex;
    flex-direction: row;
    margin: 10px;
    //height: 320px;
}

h2 {
  margin-top: 0;
}

.charts {
    display: flex;
    flex-direction: row;
    div {
        margin: 0 30px;
    }
}

</style>
