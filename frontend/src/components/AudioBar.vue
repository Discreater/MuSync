<template>
  <div>
    <audio controls>
      <source src="/static/RSP-さくら~あなたに出会えてよかった~[清明樱花祭].mp3" type="audio/mp3">
    </audio>
    <div>
      <div id="jquery_jplayer_1" class="jp-jplayer"></div>
      <div id="jp_container_1" class="jp-audio" role="application" aria-label="media player">
        <div class="jp-type-single">
          <div class="jp-gui jp-interface">
            <div class="jp-volume-controls">
              <button class="jp-mute" role="button" tabindex="0">mute</button>
              <button class="jp-volume-max" role="button" tabindex="0">max volume</button>
              <div class="jp-volume-bar">
                <div class="jp-volume-bar-value"></div>
              </div>
            </div>
            <div class="jp-controls-holder">
              <div class="jp-controls">
                <button class="jp-play" role="button" tabindex="0">play</button>
                <button class="jp-stop" role="button" tabindex="0">stop</button>
              </div>
              <div class="jp-progress">
                <div class="jp-seek-bar">
                  <div class="jp-play-bar"></div>
                </div>
              </div>
              <div class="jp-current-time" role="timer" aria-label="time">&nbsp;</div>
              <div class="jp-duration" role="timer" aria-label="duration">&nbsp;</div>
              <div class="jp-toggles">
                <button class="jp-repeat" role="button" tabindex="0">repeat</button>
              </div>
            </div>
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
</style>
