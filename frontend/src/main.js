// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import './plugins/element.js'
import $ from 'jquery'

Vue.config.productionTip = true

$(document).ready(function () {
  $('#jquery_jplayer_1').jPlayer({
    ready: function () {
      $(this).jPlayer('setMedia', {
        title: 'Bubble',
        m4a: 'http://www.jplayer.org/audio/m4a/Miaow-07-Bubble.m4a',
        oga: 'http://www.jplayer.org/audio/ogg/Miaow-07-Bubble.ogg'
      })
    },
    cssSelectorAncestor: '#jp_container_1',
    swfPath: '/js',
    supplied: 'm4a, oga',
    useStateClassSkin: true,
    autoBlur: false,
    smoothPlayBar: true,
    keyEnabled: true,
    remainingDuration: true,
    toggleDuration: true
  })
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: {App},
  template: '<App/>'
})
