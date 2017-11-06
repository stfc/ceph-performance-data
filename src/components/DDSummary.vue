<template>
    <div id='summary-page'>
        <div class='table-container'>
            <vue-table 
                v-bind:d='getSummary("read")'
            >
            </vue-table> 

            <p> View graph <router-link v-bind:to="{path:'/dd_graph?type=read'}"> here </router-link> </p>
        </div>

        <div class='table-container'>
            <vue-table
                v-bind:d='getSummary("write")'
            >
            </vue-table>

            <p> View graph <router-link v-bind:to="{path:'/dd_graph?type=write'}"> here </router-link> </p>

        </div>
    </div>
</template>


<script>
    import VueTable from './VueTable.vue'
    export default {
        
        name: 'DDSummary',
        
        components: {
            VueTable
        },

        data: () => ({
            read: {},
            write: {}
        }),

        created () {
            // fetch the data
            console.log('dd summary component created');
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
                avr['results'] = [];
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
                    entry['BlockSize'] = blocksize;
                    avr['results'].push(entry);
                }
                console.log('get summary result', t, avr);
                return avr;
            }
        }
    }
</script>

<style scoped>

    .table-container {
        position: relative;
        display: inline-block;
        min-width: 400px;
        min-height: 200px;
        box-shadow: 10px 10px 5px grey;
        margin: 10px;
    }

</style>

