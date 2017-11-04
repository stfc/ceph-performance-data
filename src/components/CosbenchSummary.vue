<template>
    <div class='summary-page'>
        <div class='table-container' v-for='wl in workloads'>
             <cosbench-summary-table
                v-bind:id='wl.id'
                v-bind:title='wl.title'
                v-bind:columns='wl.columns'
                v-bind:data='wl.data'
                v-bind:key='wl.id'
             >
             </cosbench-summary-table> 
        </div>
    </div>
</template>


<script>
    // Accepts Array of workload Objects in the format
    /*
        workload : {
            id: String,
            title: String [optional],
            columns: Array[String],
            data: Array[{colname:Value}]
    */
    import CosbenchSummaryTable from './CosbenchSummaryTable.vue'
    export default {
        
        name: 'CosbenchSummary',
        
        components: {
            CosbenchSummaryTable
        },

        data: () => ({
            workloads: []
        }),

        created () {
            console.log('cosbench summary component created');
            this.axios.get('http://localhost:3000/fetch_cosbench_summary').then(response => {
                console.log('Axios workloads result',response.data);
                this.workloads = response.data;
            })

        },

        methods: {
            add_workload: function(wl) {
                this.workloads.push(wl);
            },

            remove_workload: function(id) {
                for ([index, el] of this.workloads.entries()) {
                    if(el.id == id) {
                        this.workload.splice(index,1);
                    }
                }
            }
        }
    }
</script>

<style scoped>
    .table-container {
        position: relative;
        display: inline-block;
        min-width: 800px;
        min-height: 200px;
        box-shadow: 10px 10px 5px grey;
        margin: 10px;
    }

</style>

