<template>
    <table>
        <thead>
            <tr>
                <th class='table-title'>
                    {{ getTitle() }}
                </th>
            </tr>
            <tr class='table-headers'>
                <th v-for='col in getColumns()'>
                    {{ col }}
                </th>
            </tr>
         </thead>
         <tbody>
            <tr v-for='row in getContents()'>
                <td v-for='col in getColumns()'>
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
        title:String,
        columns:Array,
        contents:Array,
        config_obj: Object
    },

    methods: {
        getTitle() {
            return this.title || this.config_obj.title;
        },

        getColumns() {
            return this.columns || this.config_obj.columns;
        },

          getContents() {
            return this.contents || this.config_obj.contents;
        }
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
