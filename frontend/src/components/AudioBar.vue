<template>
  <div>
    <div class="bottom-bar">
      <div id="jquery_jplayer_1" class="jp-jplayer"></div>
      <div id="jp_container_1" class="jp-audio" role="application" aria-label="media player">
        <div class="jp-type-single">
          <div class="jp-gui jp-interface">
            <el-row>
              <el-col :span="20">
                <div class="jp-controls-holder">
                  <el-row>
                    <el-col :span="4">
                      <div class="jp-controls">
                        <el-row>
                          <button class="jp-play" role="button" tabindex="0">play</button>
                          <button class="jp-stop" role="button" tabindex="0">stop</button>
                        </el-row>
                      </div>
                    </el-col>
                    <el-col :span="20">
                      <div class="jp-progress">
                        <div class="jp-seek-bar">
                          <div class="jp-play-bar"></div>
                        </div>
                      </div>
                    </el-col>
                  </el-row>
                  <el-row>
                    <el-col :span="8">
                      <div class="jp-current-time" role="timer" aria-label="time">&nbsp;</div>
                    </el-col>
                    <el-col :span="8">
                      <div class="jp-toggles">
                        <button class="jp-repeat" role="button" tabindex="0">repeat</button>
                      </div>
                    </el-col>
                    <el-col :span="8">
                      <div class="jp-duration" role="timer" aria-label="duration">&nbsp;</div>
                    </el-col>
                  </el-row>
                </div>
              </el-col>
              <el-col :span="4">
                <div class="jp-volume-controls">
                  <el-row>
                    <el-col :span="4">
                      <button class="jp-mute" role="button" tabindex="0">mute</button>
                    </el-col>
                    <el-col :span="16">
                      <div class="jp-volume-bar">
                        <div class="jp-volume-bar-value"></div>
                      </div>
                    </el-col>
                    <el-col :span="4">
                      <button class="jp-volume-max" role="button" tabindex="0">max volume</button>
                    </el-col>
                  </el-row>
                </div>
              </el-col>
            </el-row>
          </div>
          <div class="jp-details">
            <div class="jp-title" aria-label="title">&nbsp;</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import 'jplayer'
import $ from 'jquery'

$(document).ready(function () {
  $('#jquery_jplayer_1').jPlayer({
    ready: function () {
      $(this).jPlayer('setMedia', {
        title: 'Bubble',
        mp3: 'http://127.0.0.1:8888/music/000/000602_s.mp3'
      })
    },
    cssSelectorAncestor: '#jp_container_1',
    swfPath: '/js',
    supplied: 'mp3',
    useStateClassSkin: true,
    autoBlur: false,
    smoothPlayBar: true,
    keyEnabled: true,
    remainingDuration: true,
    toggleDuration: true
  })
})
export default {
  name: 'AudioBar',
  data () {
    return {
      file: '/static/RSP-さくら~あなたに出会えてよかった~[清明樱花祭].mp3'
    }
  },
  components: {

  },
  methods: {
    audioFinish () {
      console.log('You see this means audio finish.')
    }
  }

}
</script>

<style scoped>
.bottom-bar {
  position: relative;
}
</style>
