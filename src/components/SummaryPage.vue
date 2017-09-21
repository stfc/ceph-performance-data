<template>
    <div id='summary-page'>
        <div class='table-container'>
             <summary-table v-for='wl in workloads'
                v-bind:id='wl.id'
                v-bind:title='wl.title'
                v-bind:columns='wl.columns'
                v-bind:data='wl.data'
                v-bind:key='wl.id'
             >
             </summary-table> 
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
    import SummaryTable from './SummaryTable.vue'
    export default {
        
        name: 'SummaryPage',
        
        components: {
            SummaryTable
        },

        data: () => ({
            workloads: []
        }),

        created () {
            this.axios.get('http://vm236.nubes.stfc.ac.uk:3000/fetchall').then(response => {
                console.log('Axios workloads result',response.data);
                this.workloads = response.data;
            })

        },

        methods: {
            add_workload(wl) {
                this.workloads.push(wl);
            },

            remove_workload(id) {
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
        height: 200px;
        box-shadow: 10px 10px 5px grey;
        margin: 10px;
    }

</style>

