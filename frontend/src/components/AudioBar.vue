<template>
  <div class="bottom-bar">
    <audio
      :src="audio.file"
      ref="audio"
      @pause="onPause"
      @play="onPlay"
      @timeupdate="onTimeupdate"
      @loadedmetadata="onLoadedmetadata"
    ></audio>
    <!-- 音频播放控件 -->
    <div class="music-info">
      <el-tooltip
        class="title_item"
        effect="dark"
        :content="audio.full_title"
        placement="top-start"
      >
        <p class="music-title">{{pre_title}}</p>
      </el-tooltip>
      <el-tooltip
        class="artist_item"
        effect="dark"
        :content="audio.full_artist"
        placement="top-end"
      >
        <p class="music-artist">--{{pre_artist}}</p>
      </el-tooltip>
    </div>
    <div class="audio-player">
      <div class="audio-img">
        <!-- music图片 -->
        <img :src="audio.icon" style="position: relative; height: 80px; width:80px">
      </div>
      <div class="audio-controls">
        <el-button :class="button_icon" @click="startPlayOrPause" circle type="primary"></el-button>
        <el-tooltip effect="dark" content="下一首" placement="top">
          <el-button class="el-icon-caret-right" circle size="small"></el-button>
        </el-tooltip>
      </div>
      <div class="audio-progress">
        <div class="audio-slider">
          <el-slider
            v-model="sliderTime"
            :format-tooltip="formatProcessToolTip"
            @change="changeCurrentTime"
            class="slider"
          ></el-slider>
        </div>
        <div class="audio-times">
          <el-tag
            type="info"
          >{{ audio.currentTime | formatSecond}}/{{ audio.maxTime | formatSecond}}</el-tag>
        </div>
        <div class="audio-volume" id="audio-vulume">
          <el-popover class="volume-popover" placement="top" width="100%">
            <el-button
              @click="initVolumeSlider"
              class="el-icon-s-operation"
              slot="reference"
              size="small"
              type="success"
            ></el-button>
            <el-slider class="volume-slider" v-model="sliderVolume" vertical height="60px"></el-slider>
          </el-popover>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// 整数格式化成 分：秒
function realFormatSecond (second) {
  var secondType = typeof second

  if (secondType === 'number' || secondType === 'string') {
    second = parseInt(second)

    var mimute = Math.floor(second / 60)
    second = second - mimute * 60

    return ('0' + mimute).slice(-2) + ':' + ('0' + second).slice(-2)
  } else {
    return '00:00'
  }
}
export default {
  name: 'AudioBar',
  data () {
    return {
      audio: {
        full_title: 'さくら~あなたに出会えてよかった~[清明樱花祭]',
        full_artist: 'RSP',
        file: '/static/RSP-さくら~あなたに出会えてよかった~[清明樱花祭].mp3',
        playing: false,
        icon: '/static/logo.png',
        currentTime: 0,
        maxTime: 0
      },
      sliderTime: 0,
      sliderVolume: 10
    }
  },
  mounted () {
    this.$refs.audio.volume = this.sliderVolume / 100
  },
  computed: {
    button_icon: function () {
      return this.audio.playing ? 'el-icon-video-pause' : 'el-icon-video-play'
    },
    pre_title: function () {
      return this.audio.full_title.substring(0, 80)
    },
    pre_artist: function () {
      return this.audio.full_artist.substring(0, 80)
    }
  },
  watch: {
    sliderVolume: function (val) {
      this.$refs.audio.volume = val / 100
    }
  },
  methods: {
    // 拖动进度条，改变当前时间，index是进度条改变时的回调函数的参数0-100之间，需要换算成实际时间
    changeCurrentTime (index) {
      this.$refs.audio.currentTime = parseInt(index / 100 * this.audio.maxTime)
    },
    initVolumeSlider () {
      this.sliderVolume = this.$refs.audio.volume * 100
    },
    // 控制音频的播放与暂停
    startPlayOrPause () {
      return this.audio.playing ? this.pause() : this.play()
    },
    // 播放音频
    play () {
      this.$refs.audio.play()
    },
    // 暂停音频
    pause () {
      this.$refs.audio.pause()
    },
    // 当音频播放
    onPlay () {
      this.audio.playing = true
    },
    // 当音频暂停
    onPause () {
      this.audio.playing = false
    },
    // 当加载语音流元数据完成后，会触发该事件的回调函数
    // 语音元数据主要是语音的长度之类的数据
    onLoadedmetadata (res) {
      this.audio.maxTime = parseInt(res.target.duration)
    },
    // 当timeupdate事件大概每秒一次，用来更新音频流的当前播放时间
    // 当音频当前时间改变后，进度条也要改变
    onTimeupdate (res) {
      this.audio.currentTime = res.target.currentTime
      this.sliderTime = this.audio.currentTime / this.audio.maxTime * 100
    },
    // 进度条格式化toolTip
    formatProcessToolTip (index = 0) {
      index = parseInt(this.audio.maxTime / 100 * index)
      return '进度条: ' + realFormatSecond(index)
    }
  },
  filters: {
    // 将整数转化成时分秒
    formatSecond (second = 0) {
      return realFormatSecond(second)
    }
  }

}
</script>

<style scoped>
.music-info .title_item {
  float: left;
}
.music-info .artist_item {
  float: right;
}
.music-info {
  display: flex;
}
.music-info .music-artist {
  margin: 0;
  padding-right: 1%;
  text-align: right;
  font-size: 14px;
  flex-grow: 1;
}
.music-info .music-title {
  margin: 0;
  text-align: left;
  font-size: 14px;
  flex-grow: 1;
}
.music-info p {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
.music-info {
  border-bottom-style: solid;
  border-bottom-width: 1px;
  border-bottom-color: #c5c5c5;
  border-top-style: solid;
  border-top-width: 1px;
  border-top-color: #c5c5c5;
}
.audio-controls .el-button + .el-button {
  margin-left: 1%;
}
.audio-player {
  display: flex;
  align-items: center;
  justify-content: center;
}
.audio-player .audio-img {
  flex-grow: 2;
  order: 1;
  border-right-style: solid;
  border-right-width: 1px;
  border-right-color: #c5c5c5;
}
.audio-player .audio-controls {
  flex-grow: 2;
  order: 2;
}
.audio-player .audio-progress {
  flex-grow: 50;
  order: 3;
  display: flex;
  align-items: center;
  justify-content: center;
}
.audio-progress .audio-slider {
  order: 1;
  flex-grow: 20;
}
.audio-slider {
  padding-left: 6%;
}
.audio-progress .audio-times {
  order: 2;
  flex-grow: 1;
}
.audio-progress .audio-volume {
  order: 3;
  flex-grow: 1;
}
.bottom-bar .el-row .el-col {
  height: 100%;
}
.bottom-bar {
  position: fixed;
  width: 100%;
  height: 94px;
  bottom: 0;
}
</style>
