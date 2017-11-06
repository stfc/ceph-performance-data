<template>
    <div class='summary-page'>
        <div class='table-container' v-for='test in getSummary()'>
            <vue-table v-bind:config_obj='test'>
            </vue-table> 
        </div>
    </div>
</template>


<script>
    import VueTable from './VueTable.vue'
    export default {
        name: 'IPerfSummary',
        components: {
            VueTable
        },

        data: () => ({
            tests: []
        }),

        created () {
            this.axios.get('http://localhost:3000/fetch_iperf_tests').then(response => {
                this.tests = response.data;
                console.log('iperf tests', this.tests);
            });
        },

        methods: {
            /*
            Three tables
                columns: [Duration(s), host, all of test_start]
                columns: sum_sent
                columns: cpu-utilisation

            */
            getSummary: function() {
                var res = [];

                for(let test of this.tests) {
                    let data = {};
                    data['title'] = (test.start.test_start.duration / 60) + ' Minutes';
                    data['columns'] = ['Field', 'Result'];
                    data['contents'] = [];
                    data['contents'].push({'Field':'Duration(s)', 'Result':test.start.test_start.duration});
                    data['contents'].push({'Field':'Host', 'Result':test.start.connecting_to.host});
                    data['contents'].push({'Field':'Protocol', 'Result':test.start.test_start.protocol});
                    data['contents'].push({'Field':'BlockSize(bit)', 'Result':test.start.test_start.blksize});

                    data['contents'].push({'Field':'Bytes Sent', 'Result':test.end.sum_sent.bytes});
                    data['contents'].push({'Field':'Speed(Mbits/s)', 'Result':test.end.sum_sent.bits_per_second/(1024 * 1024)});
                    data['contents'].push({'Field':'Retransmits', 'Result':test.end.sum_sent.retransmits});
                    data['contents'].push({'Field':'Host CPU (%)', 'Result':test.end.cpu_utilization_percent.host_total});
                    data['contents'].push({'Field':'Remote CPU (%)', 'Result':test.end.cpu_utilization_percent.remote_total});
                    res.push(data);
                }
                res.sort(function(a,b) {
                    if(parseInt(a['title']) < parseInt(b['title'])) {
                        return -1;
                    } else if(parseInt(a['title']) == parseInt(b['title'])) {
                        return 0;
                    } else {
                        return 1;
                    }
                });
                return res
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

