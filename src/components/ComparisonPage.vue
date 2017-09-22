<template>
    <div class='graph-container'>
        <!-- Or choose to create the graph here ? -->
        <!-- 
            Maybe just select them manually for now, dont think graph component should
            what type of graph to draw tbh
        -->
        <line-graph
            v-bind:graph_data="gdata('workers', 'Bandwidth')"
        >
        </line-graph>

    </div>
</template>

<script>
    import LineGraph from './LineGraph.vue'
    export default {
        name: 'ComparisonPage',
        components: {
            LineGraph
        },

        // acceps a CSV string from vue-router containing all the workloads to compare
        props: {
            workload_ids: String,
            graph_config: String
        },

        data: () => ({
            workloads: []
        }),

        created() {
            for(const id of this.workload_ids.split(',')) {
                var url = 'http://vm236.nubes.stfc.ac.uk:3000/fetch_workload?id='+id 
                this.axios.get(url).then(response => {
                    console.log('Fetched workloads',response.data);
                    this.workloads.push(response.data);
                });
            }
        },

        methods: {
            gdata: function(xfield, yfield) {
                var graph_data = []
                for(var wl of this.workloads) {
                    var d = {}
                    if(wl[xfield] != null) {
                        d['x'] = wl[xfield];
                    } else {
                        for(var row of wl['data']) {
                            if(row['Stage'] == 's3-main' && row['Op-Type'] == 'read') {
                                d['x'] = row[xfield]
                            }
                        }
                    }

                    if(wl[yfield] != null) {
                        d['y'] = wl[yfield];
                    } else {
                        for(var row of wl['data']) {
                            if(row['Stage'] == 's3-main' && row['Op-Type'] == 'read') {
                                d['y'] = row[yfield] / (1024 * 1024)
                            }
                        }
                    }
                    graph_data.push(d);

                }
                console.log('returning graph data', graph_data);
                return graph_data;
            }
        }
    }

</script>

<style scoped>
</style>
