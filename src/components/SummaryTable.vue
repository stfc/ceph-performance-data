<template>
    <table>
        <thead>
            <tr>
                <th class='table-title'>
                    {{ title }}
                </th>
            </tr>
            <tr class='table-headers'>
                <th v-for='col in columns'>
                    {{ col }}
                </th>
            </tr>
         </thead>
         <tbody>
            <tr v-for='row in data'>
                <td v-for='col in columns'>
                    {{ row[col] }}
                </td>
            </tr>
        </tbody>
    </table>            
</template>

<script>

export default {
    name: 'SummaryTable',
    props: {
        id: String,
        title: String,
        columns: Array,
        data: Array
    }

}


</script>

<style scoped>
    table {
        border-collapse: collapse;
        border: 1px solid black;
    }

    th, td {
        border: 1px solid black;
    }

    th {
        background-color: lightblue;
    }
</style>
