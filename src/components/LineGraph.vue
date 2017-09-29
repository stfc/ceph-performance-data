<template>
    <!-- 
        Component for line graph, by default only show values for main stage
    -->

    <canvas class='line-graph'>
    </canvas>
    


</template>

<script>
    import Chart from 'chart.js'
    export default {
        name: 'LineGraph',
        props: {
            graph_data:Object
        },

        data: function() {
            return {chart: null}
        },

        watch: {
            graph_data : function() {
                if(this.chart != null) {
                    console.log('Updated Graph Data', this.graph_data);
                    // Reset chart data
                    this.chart.data.datasets = [];

                    // Build graph labels
                    this.chart.data.labels = [];
                    for(let d of this.graph_data['data']) {
                        if(!this.chart.data.labels.includes(d['x'])) {
                            this.chart.data.labels.push(d['x']);   
                        }
                    }
                    this.chart.data.labels.sort();
                    
                    // loop over legends and data to add invidual datasets
                    for(let l of this.graph_data['legend']) {
                        var ds = {};
                        ds.label = l;
                        ds.data = [];
                        for(let d of this.graph_data['data']) {
                            if(d['legend'] == l) {
                                ds.data.push({'x': d['x'], 'y':d['y']});
                            }
                        }
                        ds.data.sort(function(e1, e2) {
                            if(e1['x'] < e2['x']) {
                                return -1;
                            } else if(e1['x'] == e2['x']) {
                                return 0;
                            } else { return 1;}
                        });
                        this.chart.data.datasets.push(ds);
                    }
                    this.chart.update();
                }
            }
        },

        mounted: function(){
            console.log('Mounting Graph', this.graph_data);
            this.chart = new Chart(this.$el, {
                type: 'line',
                data: {},
                options: {
                    scales: {
                        xAxes: [{
                            ticks: {
                                beginAtZero: true,
                                autoskip: false,
                                display: true
                            },

                            scaleLabel: {
                                display: true,
                                labelString: this.graph_data['xtitle']
                            }
                        }],
                        yAxes: [{
                            ticks: {
                                beginAtZero: false,
                            },
                            scaleLabel: {
                                display: true,
                                labelString: this.graph_data['ytitle']
                            }
                        }]
                    }
                }
            });
        }
    }

</script>

<style scoped>
    .line-graph { 
        max-width: 800px;
        max-height: 500px;
    }
</style>







