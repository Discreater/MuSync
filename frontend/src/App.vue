<template>
  <div id="app">
    <div id="test-send">
      <el-button @click="getDetail">add</el-button>
    </div>
    <router-link v-bind:to="'/'">Home</router-link>
    <router-link v-bind:to="'/about'">About</router-link>
    <router-view></router-view>
    <AudioBar></AudioBar>
  </div>
</template>

<script>
/* eslint-disable */
  import HelloWorld from './components/HelloWorld.vue'
  import axios from 'axios'
  import AudioBar from './components/AudioBar'

  export default {
    name: 'app',
    components: {
      HelloWorld, AudioBar
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
