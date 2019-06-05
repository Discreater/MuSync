<template>
  <div id="app">
    <div id="test-send">
      <el-button @click="getDetail">el-button</el-button>
    </div>
    <router-link v-bind:to="'/'">Home</router-link>
    <router-link v-bind:to="'/about'">About</router-link>
    <router-view></router-view>
    <AudioBar></AudioBar>
    <aplayer autoplay
             :music="{
             title: 'sakura',
             artist: 'Me',
             src: '/static/RSP-さくら~あなたに出会えてよかった~[清明樱花祭].mp3'
             }"/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import axios from 'axios'
import AudioBar from './components/AudioBar'
import Aplayer from 'vue-aplayer'

export default {
  name: 'app',
  components: {
    HelloWorld, AudioBar, Aplayer
  },
  methods: {
    getDetail: function () {
      axios.get('http://192.168.1.102:8000/musync/5/results/').then(function (response) {
        alert(response.data)
      }).catch(function (error) {
        alert('Error!' + error)
      })
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
