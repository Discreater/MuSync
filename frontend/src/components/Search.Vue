<template>
  <div class="search-page">
    <el-tabs v-model="activeName" type="border-card">
      <el-tab-pane label="歌曲" name="music">
        <el-pagination
          :currentPage="music.page"
          @current-change="changePage"
          background
          :hide-on-single-page="true"
          :page-size="music.pageSize"
          :pager-count="7"
          layout="prev, pager,next"
          :total="music.musicCount"
        ></el-pagination>
        <b-table :items="music.musicData" :fields="music.fields" fixed hover>
          <template slot="actions" slot-scope="row">
            <el-popover placement="top" title="下一首播放" trigger="hover">
              <el-button @click="addToCurrentList(row.item)" slot="reference" icon="el-icon-circle-plus" circle=""></el-button>
            </el-popover>
          </template>
        </b-table>
        <el-pagination
          :currentPage="music.page"
          @current-change="changePage"
          background
          :hide-on-single-page="true"
          :page-size="music.pageSize"
          :pager-count="7"
          layout="prev, pager,next"
          :total="music.musicCount"
        ></el-pagination>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Search',
  data () {
    return {
      activeName: 'music',
      music: {
        fields: [
          { key: 'order', label: '#' },
          { key: 'title', label: '歌名' },
          { key: 'artist__name', label: '歌手' },
          { key: 'album__title', label: '专辑' },
          { key: 'actions', label: '' }
        ],
        query: '',
        page: 1,
        pageSize: 7,
        musicData: [],
        musicCount: 0
      }
    }
  },
  methods: {
    fetchMusicData: function () {
      this.music.query = this.$route.query.q
      this.music.page = parseInt(this.$route.query.p)
      axios.get(this.COMMON.httpURL + 'musics/search?q=' + this.music.query + '&p=' + String(this.music.page))
        .then(response => {
          this.music.musicData = response.data.musics
          this.music.musicCount = response.data.count
        })
        .catch(error => {
          if (error.response) {
            this.$message({
              showClose: true,
              message: error.response.data.error,
              type: 'error',
              duration: 2000
            })
          } else {
            this.$message({
              showClose: true,
              message: '未知错误',
              type: 'error',
              duration: 2000
            })
            console.log(error)
          }
        })
    },
    changePage: function (page) {
      this.$router.push({
        path: '/search',
        query: {
          q: this.music.query,
          p: page
        }
      })
    },
    addToNextPlay: function (music) {
      axios.post(this.COMMON.httpURL + 'list/current/next', {'music_id': music.id, 'user_id': localStorage.user_id})
        .then(response => {
          // TODO 添加下一首播放
        })
    }
  },
  created () {
    this.fetchMusicData()
  },
  watch: {
    '$route': 'fetchMusicData'
  }
}
</script>

<style scoped>
</style>
