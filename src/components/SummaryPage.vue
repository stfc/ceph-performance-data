<template>
    <div id='summary-page'>
        <div class='summary-container' v-for='tst in tests' >
            <h2> Click here to see <router-link v-bind:to="{path: '/' + tst}"> {{ tst }} tests</router-link> </h2>
        </div>
    </div>
</template>


<script>
    export default {
        
        name: 'SummaryPage',
        
        components: {
        },

        data: () => ({
            tests: []
        }),

        created () {
            this.axios.get('http://localhost:3000/tests').then(response => {
                console.log('Axios tests result',response.data);
                this.tests = response.data;
            })
        },

        methods: {
        }
    }
</script>

<style scoped>

.summary-container {
    position: relative;
    display: inline-block;
    min-width: 800px;
    min-height: 200px;
    box-shadow: 10px 10px 5px grey;
    margin: 10px;
}

</style>

