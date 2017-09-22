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
            graph_data:Array
        },

        data: function() {
            return {chart: null}
        },

        watch: {
            graph_data : function() {
                if(this.chart != null) {
                    this.chart.data.datasets = [];
                    var labels = [];
                    this.graph_data.forEach(function(el) {
                        labels.push(el['x']);
                    });
                    this.chart.data.labels = labels;
                    this.chart.data.datasets.push({data:this.graph_data});
                    console.log(this.chart.data);
                    this.chart.update();
                }
            }
        },

        mounted: function(){
            console.log('datapassed to chart', this.graph_data);
            var lc = new Chart(this.$el, {
                type: 'line',
                data: this.graph_data,
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
                                labelString: 'Workers'
                            }
                        }],
                        yAxes: [{
                            ticks: {
                                beginAtZero: false,
                            },
                            scaleLabel: {
                                display: true,
                                labelString: 'Bandwidth'
                            }
                        }]
                    }
                }
            });
            this.chart = lc;
        }
    }

</script>

<style scoped>
    .line-graph { 
        max-width: 800px;
        max-height: 500px;
    }
</style>







