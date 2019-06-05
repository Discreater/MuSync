<template>
  <div>
    <audio ref="audio"
           @pause="onPause"
           @play="onPlay"
           @timeupdate="onTimeupdate"
           @loadedmetadata="onLoadedmetadata"
           src="/static/RSP-さくら~あなたに出会えてよかった~[清明樱花祭].mp3"
           controls></audio>
    <div>
      <el-button type="text" @click="startPlayOrPause">{{ audio.playing | transPlayPause}}</el-button>
      <el-tag type="info">{{ audio.currentTime | formatSecond}}</el-tag>
      <el-tag type="info">{{ audio.maxTime | formatSecond()}}</el-tag>
      <el-slider v-model="sliderTime" :format-tooltip="formatProcessToolTip" @change="changeCurrentTime" ></el-slider>
    </div>
  </div>
</template>

<script>
  /* eslint-disable */
  function realFormatSecond(second) {
    let secondType = typeof second
    if (secondType === 'number' || secondType === 'string') {
      second = parseInt(second)

      let hours = Math.floor(second / 3600)
      second = second - hours * 3600
      let minute = Math.floor(second / 60)
      second = second - minute * 60

      return hours + ':' + ('0' + minute).slice(-2) + ':' + ('0' + second).slice(-2)
    } else {
      return '0:00:00'
    }
  }

  export default {
    name: 'AudioBar',
    data: function () {
      return {
        audio: {
          playing: false,
          currentTime: 0,
          maxTime: 0
        },
        sliderTime: 0
      }
    },
    methods: {
      startPlayOrPause() {
        return this.audio.playing ? this.pause() : this.play()
      },
      play() {
        this.$refs.audio.play()
      },
      pause() {
        this.$refs.audio.pause()
      },
      onPlay() {
        this.audio.playing = true
      },
      onPause() {
        this.audio.playing = false
      },
      onTimeupdate(res){
        console.log('timeupdate');
        console.log(res);
        this.audio.currentTime = res.target.currentTime;
        this.sliderTime = parseInt(this.audio.currentTime / this.audio.maxTime * 100);
      },
      onLoadedmetadata(res){
        console.log('loadedmetadata')
        console.log(res)
        this.audio.maxTime = parseInt(res.target.duration)
      },
      changeCurrentTime: function (index) {
        this.$refs.audio.currentTime = parseInt(index / 100 * this.audio.maxTime)
      },
      // 进度条格式化toolTip
      formatProcessToolTip(index = 0){
        index = parseInt(this.audio.maxTime / 100 * index)
        return '进度条：' + realFormatSecond(index)
      }
    },
    filters: {
      transPlayPause(value) {
        return value ? '暂停' : '播放'
      },
      formatSecond(second = 0){
        return realFormatSecond(second)
      }
    }
  }
</script>

<style scoped>

</style>
