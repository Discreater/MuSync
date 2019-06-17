<template>
  <div>
    <el-popover placement="top" width="500">
      <el-table :data="list">
        <el-table-column label="序号" width="50">
          <template slot-scope="scope">
            <i v-if="is_current(scope.row.order)" class="el-icon-loading" ></i>
            <span v-else>{{ scope.row.order }}</span>
          </template>
        </el-table-column>
        <el-table-column prop="track__title" label="歌名" width="200"></el-table-column>
        <el-table-column prop="track__artist__name" label="歌手"></el-table-column>
        <el-table-column label="">
          <template slot-scope="scope">
            <el-button @click="delete_by_order(scope.row.order)" class="el-icon-delete" type="danger" size="small" circle></el-button>
          </template>
        </el-table-column>
      </el-table>
      <el-button @click="getCurentList" class="el-icon-s-fold" slot="reference" type="info"></el-button>
    </el-popover>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MusicList',
  data () {
    return {
    }
  },
  computed: {
    list () {
      return this.$store.state.current_list
    }
  },
  methods: {
    getCurentList () {
      this.$store.commit('getCurrentList', this)
    },
    is_current (order) {
      if (order === this.$store.state.list_state.playing_order) {
        return true
      } else {
        return false
      }
    },
    delete_by_order (order) {
      axios.delete(this.COMMON.httpURL + 'lists/current/delete?order=' + order + '&user_id=' + localStorage.user_id)
        .then(response => {
          this.$store.commit('getCurrentList', this)
        })
    }
  }
}
</script>

<style scoped>
</style>
