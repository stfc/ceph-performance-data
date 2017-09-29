<template>
    <div class='graph-container'>
        <!-- Or choose to create the graph here ? -->
        <!-- 
            Maybe just select them manually for now, dont think graph component should know
            what type of graph to draw tbh
        -->
        <line-graph
            v-bind:graph_data="gdata('workers', 'Bandwidth', ['read', 'write'])"
        >
        </line-graph>

        <line-graph
            v-bind:graph_data="gdata('workers', 'Throughput', ['read', 'write'])"
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

        data: function() {
            return {
                workloads: [],
            }
        },

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
            // legend in cosbench context refers to the operation type (read, write)
            gdata: function(xfield, yfield, legend) {
                console.log('Called gdata');
                var graph_obj = {
                    'data': [],
                    'xtitle': xfield,
                    'ytitle': yfield,
                    'legend': legend
                }

                for(let wl of this.workloads) {
                    for(let leg of legend) {
                        var d = {}
                
                        // check if xfield is in 'workload.data' object or 'workload'
                        if(wl[xfield] != null) {
                            d['x'] = wl[xfield];

                        } else {i
                            for(var row of wl['data']) {
                                if(row['Stage'] == 's3-main' && row['Op-Type'] == leg) {
                                    d['x'] = row[xfield]
                                    d['legend'] = row['Op-Type'];
                                }
                            }   
                        }


                        if(wl[yfield] != null) {
                            d['y'] = wl[yfield];

                        } else {
                            for(var row of wl['data']) {
                                if(row['Stage'] == 's3-main' && row['Op-Type'] == leg) {
                                    d['y'] = row[yfield];
                                    d['legend'] = row['Op-Type'];
                                }
                            }
                        }
                        graph_obj.data.push(d);
                    }
                }   
                console.log('returning graph data', graph_obj);
                return graph_obj;
            }
        }
    }

</script>

<style scoped>
</style>
