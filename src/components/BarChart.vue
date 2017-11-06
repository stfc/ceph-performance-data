<template>
    <!-- 
        Component for line graph, by default only show values for main stage
    -->

    <canvas class='bar-chart'>
    </canvas>
    


</template>

<script>
    import Chart from 'chart.js'
    export default {
        name: 'BarChart',
        props: {
            graph_data:Object
        },

       data: () => ({
           chart: null
        }),

        created () {            

        },

        watch: {
            graph_data : function() {
                if(this.chart != null) {
                    console.log('Updated Graph Data', this.graph_data);

                    // Reset chart data
                    this.chart.data = this.graph_data['data'];
                    this.chart.update();
                }
            }
        },

        mounted: function(){
            console.log('Mounting Graph', this.graph_data);
            this.chart = new Chart(this.$el, {
                type: 'bar',
                data: this.graph_data['data'],
                options: this.graph_data['options']
            });
        }
    }

</script>

<style scoped>
    .bar-chart { 
    }
</style>







