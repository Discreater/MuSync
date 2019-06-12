<template>
  <div id="app">
    <div class="header">
      <HeadBar></HeadBar>
    </div>
    <div class="main">
      <div class="left-bar">
        <transition name="el-fade-in">
          <Friend v-show="is_logined && show_friend"></Friend>
        </transition>
        <div style="width:20px; align-self: center;box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)">
        <i
          style="width: 20px"
          :class="show_friend ? 'el-icon-arrow-left' : 'el-icon-arrow-right'"
          @click="$store.commit('toggleShowFriend')"
        >好友列表</i>
        </div>
      </div>
      <div class="main-display">
        <router-view></router-view>
      </div>
    </div>
    <MusicList class="float-list"></MusicList>
    <AudioBar></AudioBar>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import AudioBar from './components/AudioBar'
import MusicList from './components/MusicList'
import HeadBar from './components/HeadBar'
import Friend from './components/Friend'

export default {
  name: 'app',
  components: {
    HelloWorld,
    AudioBar,
    MusicList,
    HeadBar,
    Friend
  },
  computed: {
    show_friend: function () {
      return this.$store.state.show_friend
    },
    is_logined: function () {
      return this.$store.state.is_logined
    }
  }
}
</script>

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
  right: 30px;
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
  border-bottom-style: solid;
  border-bottom-color: #c5c5c5;
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
  display: flex;
  justify-content: flex-start;
}
.left-bar {
  display: flex;
  justify-content: flex-start;
}
.main-display {
  flex-grow: 1;
  margin: 10px
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
