import Vue from 'vue'
import Router from 'vue-router'
import About from '@/components/About'
import Search from '@/components/Search'
import UserInfo from '@/components/UserInfo'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'about',
      component: About
    },
    {
      path: '/search',
      name: 'Search',
      component: Search
    },
    {
      path: '/info',
      name: 'Info',
      component: UserInfo
    }
  ]
})
