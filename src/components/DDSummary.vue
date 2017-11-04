<template>
    <div id='summary-page'>
    </div>
</template>


<script>
    export default {
        
        name: 'DDSummary',
        
        components: {
        },

        data: () => ({
            read: {},
            write: {}
        }),

        created () {
            // fetch the data
            console.log('dd summary component created');
            this.axios.get('http://localhost:3000/fetch_dd_summary?summary=write').then(response => {
                console.log('dd summary workloads result',response.data);
                this.read = response.data;
            })
        },

        methods: {
       
        }
    }
</script>

<style scoped>
</style>

