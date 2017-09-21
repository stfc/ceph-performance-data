import Vue from 'vue'
import Router from 'vue-router'
import Hello from '@/components/Hello'
import SummaryPage from '@/components/SummaryPage'

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            name: 'hello',
            component: SummaryPage
        },

        {
            path: '/home',
            name: 'home',
            component: {template:'<div>Welcome to my ceph performance grapher.</div>'}  
        }
    ]
})
