<template>
  <div id="app">
    <el-container style="height:100%">
      <el-container>
        <el-aside>Aside</el-aside>
        <el-container>
          <el-header>Header</el-header>
          <el-main>
            <div id="test-send">
              <el-button @click="getDetail">add</el-button>
            </div>
            <router-link v-bind:to="'/'">Home</router-link>
            <router-link v-bind:to="'/about'">About</router-link>
            <router-view></router-view>
          </el-main>
        </el-container>
      </el-container>
      <el-footer height="100">
        <AudioBar></AudioBar>
      </el-footer>
    </el-container>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import axios from 'axios'
import AudioBar from './components/AudioBar'

export default {
  name: 'app',
  components: {
    HelloWorld,
    AudioBar
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
.el-header {
  background-color: #b3c0d1;
  color: #333;
  line-height: 60px;
}
.el-aside {
  background-color: #d3dce6;
  color: #333;
  text-align: center;
  line-height: 200px;
}
.el-footer {
  padding: 0;
}
.el-main {
  background-color: #e9eef3;
  color: #333;
  text-align: center;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 98%;
  width: 98%;
  position: absolute;
}
html,
body {
  width: 98%;
  height: 98%;
}
</style>
