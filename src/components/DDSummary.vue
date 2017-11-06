<template>
    <div id='summary-page'>
        <div class='main-table-container'>
            <div class='table-container'>
                <vue-table
                    v-bind:config_obj='getSummary("read")'
                >
                </vue-table> 

                <p v-if='!show_read_graphs' v-on:click='show_read_graphs=true'> Show Graphs </p>
                <p v-if='show_read_graphs'  v-on:click='show_read_graphs=false'> Hide Graphs </p>
            </div>

            <div class='table-container'>
                <vue-table
                    v-bind:config_obj='getSummary("write")'
                >
                </vue-table>

                <p v-if='!show_write_graphs' v-on:click='show_write_graphs=true'> Show Graphs </p>
                <p v-if='show_write_graphs' v-on:click='show_write_graphs=false'> Hide Graphs </p>
            </div>
        </div>

        <div class='read-graph-container' v-if='show_read_graphs'>
            <div class='graph-container' v-for='gd in getGraphData("read")' v-bind:key='gd.key'>
                <bar-chart v-bind:graph_data='gd'>
                </bar-chart>
            </div>
        </div>

        <div class='write-graph-container' v-if='show_write_graphs'>
            <div class='graph-container' v-for='gd in getGraphData("write")' v-bind:key='gd.key'>
                <bar-chart v-bind:graph_data='gd'>
                </bar-chart>
            </div>
        </div>

    </div>
</template>


<script>
    import VueTable from './VueTable.vue'
    import BarChart from './BarChart.vue'

    export default {
        
        name: 'DDSummary',
        
        components: {
            VueTable,
            BarChart
        },

        data: () => ({
            read: {},
            write: {},
            show_read_graphs: false,
            show_write_graphs: false
        }),

        created () {
            // fetch the data
            this.axios.get('http://localhost:3000/fetch_dd_summary?summary=read').then(response => {
                this.read = response.data;
            });

            this.axios.get('http://localhost:3000/fetch_dd_summary?summary=write').then(response => {
                this.write = response.data;
            });
        },

        methods: {
            getSummary: function(t) {
                var avr = {};
                avr['contents'] = [];
                avr['columns'] = [];
                avr.title = "";

                if(t == 'read') {
                    avr.title = "Read Summary";
                    if(Object.entries(this.read).length == 0) {
                        return avr;
                    }
                    avr['columns'] = this.read['columns'];
                    var results = this.read['results'];

                } else if(t == 'write') {
                    avr.title = "Write Summary";
                    if(Object.entries(this.write).length == 0) {
                        return avr;
                    }
                    avr['columns'] = this.write['columns'];
                    var results = this.write['results'];
                }

                for (let [blocksize, metrics] of Object.entries(results)) {
                    let totals = {};
                    for (let row of metrics) {
                        for (let [field, val] of Object.entries(row)) {
                            if( !(field in totals) ) {
                                totals[field] = []
                            }
                            totals[field].push(val);
                        }
                    }
                    let entry = {};
                    for (let [field, vals] of Object.entries(totals)) {
                        if(isNaN(Number(vals[0]))) {
                            entry[field] = vals[0];
                            continue;
                        }

                        let res = vals.reduce(function(sum, curr) {
                            return (sum + curr);
                        }, 0) / vals.length;
                        res = Number( res.toPrecision(3) );
                        entry[field] = res;
                    }
                    entry['BlockSize(K)'] = blocksize;
                    avr['contents'].push(entry);
                }
                console.log('get summary result', t, avr);
                return avr;
            },
            /*
                [   // Each object represents one of the metrics
                    // Y: Metric, X: block sizes
                    {
                        title: String,
                        ytitle: String,
                        xtitle: String,
                        data: [ {x:Number, y:Number} ]
                    } 
                ]
            */
            getGraphData: function(type) {
                var gdata = [];
                var summary = this.getSummary(type);

                for (let metric of ['Bytes', 'Time(s)', 'TransferRate(MB/s)']) {
                    let gobj = {};
                    let data = {};
                    data['labels'] = []
                    let title = type.charAt(0).toUpperCase() + type.slice(1) + ' ' + metric;
                    data['datasets'] = [{data:[], label: title}]

                    for(let row of summary['contents']) {
                        let entry = {data: []};
                        if(data['labels'].includes(row['BlockSize(K)']) == false ) {
                            data['labels'].push(row['BlockSize(K)']);
                        }
                        data['datasets'][0]['data'].push(row[metric]);
                    }

                    let options = {
                        scales: {
                            xAxes: [{
                                ticks: {
                                    beginAtZero: false,
                                    autoskip: false,
                                    display: true
                                },

                                scaleLabel: {
                                    display: true,
                                    labelString: 'BlockSize(K)'
                                }
                            }],
                            yAxes: [{
                                ticks: {
                                    beginAtZero: true,
                                },
                                scaleLabel: {
                                    display: true,
                                    labelString: metric
                                }
                            }]
                        }
                    }

                    gobj['data'] = data;
                    gobj['options'] = options;
                    gobj['key'] = type + '_' + metric;
                    gdata.push(gobj);
                }
                console.log('gdata', gdata);
                return gdata;
            }
        }
    }
</script>

<style scoped>
    .main-table-container {
        position: relative;
        display: block;
    }

    .table-container {
        position: relative;
        display: inline-block;
        min-width: 400px;
        min-height: 200px;
        box-shadow: 10px 10px 5px grey;
        margin: 10px;
    }

    .read-graph-container {
        position: relative;
        display: block;
    }
    .write-graph-container {
        position: relative;
        display: block;
    }

    .graph-container {
        position: relative;
        display: inline-block;
        width: 600px;
        height: 300px;
        box-shadow: 10px 10px 5px grey;
        margin: 10px;
    }

</style>

