import Vue from 'vue'
import Router from 'vue-router'
import Hello from '@/components/Hello'
import SummaryPage from '@/components/SummaryPage'
import ComparisonPage from '@/components/ComparisonPage'
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
            path: '/comparison/:workload_ids',
            name: '/comparison_page',
            component: ComparisonPage,
            props:true
        }
    ]
})
