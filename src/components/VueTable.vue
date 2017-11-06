<template>
    <table>
        <thead>
            <tr>
                <th class='table-title'>
                    {{ d.title }}
                </th>
            </tr>
            <tr class='table-headers'>
                <th v-for='col in d.columns'>
                    {{ col }}
                </th>
            </tr>
         </thead>
         <tbody>
            <tr v-for='row in d.results'>
                <td v-for='col in d.columns'>
                    {{ row[col] }}
                </td>
            </tr>
        </tbody>
    </table>            
</template>

<script>

export default {
    name: 'VueTable',
    props: {
        d: Object
    }

}


</script>

<style scoped>
    table {
        border-collapse: collapse;
        border: 1px solid black;
        padding: 10px;
    }

    th, td {
        border: 1px solid black;
    }

    th {
        background-color: lightblue;
    }
</style>
