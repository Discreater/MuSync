// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import './plugins/element.js'
import 'jplayer'

import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import global from './components/Common'

import Vuex from 'vuex'

Vue.use(Vuex)

Vue.use(BootstrapVue)
Vue.prototype.COMMON = global

Vue.config.productionTip = true

const store = new Vuex.Store({
  state: {
    is_logined: false,
    show_friend: true,
    html_height: 0,
    searchReq: '',
    searchRes: []
  },
  mutations: {
    search (state, {req, res}) {
      state.searchReq = req
      state.searchRes = res
    },
    login (state) {
      state.is_logined = true
    },
    logout (state) {
      state.is_logined = false
    },
    toggleShowFriend (state) {
      state.show_friend = !state.show_friend
    },
    changeHeight (state, height) {
      state.html_height = height
    }
  }
})

window.onresize = function () {
  store.commit('changeHeight', document.body.clientHeight)
}

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  router,
  components: { App },
  template: '<App/>'
})
