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
import axios from 'axios'

Vue.use(Vuex)

Vue.use(BootstrapVue)
Vue.prototype.COMMON = global

Vue.config.productionTip = true

function getList (state, vm) {
  if (localStorage.user_id) {
    axios
      .get(
        vm.COMMON.httpURL +
        'lists/current/all?user_id=' +
        localStorage.user_id
      )
      .then(response => {
        if (JSON.stringify(state.current_list) !== JSON.stringify(response.data.list)) {
          state.current_list = response.data.list
        }
        if (JSON.stringify(state.list_state) !== JSON.stringify(response.data.state)) {
          state.list_state = response.data.state
        }
      })
      .catch(error => {
        if (error.response) {
          vm.$message({
            showClose: true,
            message: error.response.data.error,
            type: 'error',
            duration: 2000
          })
        } else {
          vm.$message({
            showClose: true,
            message: '未知错误',
            type: 'error',
            duration: 2000
          })
          console.log(error)
        }
      })
  }
}

const store = new Vuex.Store({
  state: {
    is_logined: false,
    show_friend: false,
    html_height: 0,
    searchReq: '',
    searchRes: [],
    current_list: [],
    list_state: {}
  },
  mutations: {
    search (state, { req, res }) {
      state.searchReq = req
      state.searchRes = res
    },
    login (state, vm) {
      state.is_logined = true
      if (localStorage.user_id) {
        let userId = String(localStorage.user_id)
        let chatSocket = new WebSocket('ws://' + window.location.host + '/ws/chat/' + userId + '/')
        chatSocket.onmessage = function (e) {
          let data = JSON.parse(e.data)
          let message = data['message']
          if (message === 'change') {
            getList(state, vm)
          }
        }
      }
    },
    logout (state) {
      state.is_logined = false
    },
    toggleShowFriend (state) {
      state.show_friend = !state.show_friend
    },
    changeHeight (state, height) {
      state.html_height = height
    },
    getCurrentList (state, vm) {
      getList(state, vm)
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
