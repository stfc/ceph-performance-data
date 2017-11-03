import Vue from 'vue'
import Router from 'vue-router'
import Hello from '@/components/Hello'
import SummaryPage from '@/components/SummaryPage'
import ComparisonPage from '@/components/ComparisonPage'
import Cosbench from '@/components/Cosbench'

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            name: 'root',
            component: SummaryPage
        },

        {
            path: '/summary',
            name: 'summary_page',
            component: SummaryPage  
        },

        {
            path:'/cosbench',
            name: 'cosbench_page',
            component: Cosbench
        }
       
    ]
})
