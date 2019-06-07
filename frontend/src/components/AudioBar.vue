<template>
  <div>
    <aplayer :list='musics' :music="music"></aplayer>
  </div>
</template>

<script>
/* eslint-disable */
  import Aplayer from 'vue-aplayer'

  export default {
    name: 'AudioBar',
    data: function () {
      return {
        music: {
          title: 'sakura',
          artist: 'Me',
          src: 'http://192.168.1.102:8888/music/000/000010_s.mp3'
        },
        musics: [{
          title: 'sakura',
          artist: 'Me',
          src:'/static/RSP-さくら~あなたに出会えてよかった~[清明樱花祭].mp3'
        }]
      }
    },
    components:{
      Aplayer
    }
  }
</script>

<style scoped>

</style>
