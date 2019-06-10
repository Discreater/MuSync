<template>
  <div id="app">
    <div class="header">
      <HeadBar></HeadBar>
    </div>
    <div class="main">
      <div id="test-send">
        <el-button @click="getDetail">add</el-button>
      </div>
      <router-link v-bind:to="'/'">Home</router-link>
      <router-link v-bind:to="'/about'">About</router-link>
      <router-view></router-view>
    </div>
    <MusicList class="float-list"></MusicList>
    <AudioBar></AudioBar>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import axios from 'axios'
import AudioBar from './components/AudioBar'
import MusicList from './components/MusicList'
import HeadBar from './components/HeadBar'

export default {
  name: 'app',
  components: {
    HelloWorld,
    AudioBar,
    MusicList,
    HeadBar
  },
  methods: {
    getDetail: function () {
      axios
        .get('http://192.168.1.102:8000/musync/5/results/')
        .then(function (response) {
          alert(response.data)
        })
        .catch(function (error) {
          alert('Error!' + error)
        })
    }
  }
}
</script>

<style lang="scss">
@import '../static/blue.monday/scss/jplayer.blue.monday.scss';
</style>

<style>
.el-popover__title {
  text-align: center;
}
.el-slider.is-vertical .el-slider__runway {
  margin: 0;
}
.el-popover {
  min-width: 0px;
}
.float-list {
  position: absolute;
  bottom: 150px;
  right: 10px;
}
body.main-body {
  overflow: hidden;
}
.header {
  position: fixed;
  width: 100%;
  top: 0;
  z-index: 1500;
  height: 80px;
}
.main {
  overflow: auto;
  padding: 0;
  margin-top: 0;
  min-height: auto;
  position: absolute;
  top: 80px;
  bottom: 94px;
  width: 100%;
  background-color: #b3c0d1;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100%;
  width: 100%;
  position: absolute;
}
html,
body {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  -webkit-font-smoothing: antialiased;
  -webkit-tap-highlight-color: transparent;
}
</style>
