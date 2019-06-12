<template>
  <div class="friend-main">
    <el-tabs type="border-card">
      <el-tab-pane label="好友">
        <el-table :data="friends" style="width:100%" :show-header="false" :height="list_height">
          <el-table-column>
            <template slot-scope="scope">
              <el-card shadow="hover">
                <div class="friend-card">
                  <div class="name-tag">
                    <span>{{ scope.row.name }}</span>
                  </div>
                  <div class="current-listen">
                    <span>{{ scope.row.id }}</span>
                  </div>
                </div>
              </el-card>
            </template>
          </el-table-column>
        </el-table>
      </el-tab-pane>
      <el-tab-pane label="群组">群组</el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
import axios from 'axios'

function fetchFriends (vm, userId) {
  let url = 'friend/' + String(userId) + '/friends/'
  axios.get(vm.COMMON.httpURL + url)
    .then(response => {
      vm.friends = response.data.friends
    })
    .catch(error => {
      if (error.response) {
        vm.$message({
          showClose: true,
          message: error.response.data.error,
          type: 'error',
          duration: 2000
        })
      } else {
        vm.$message({
          showClose: true,
          message: '未知错误',
          type: 'error',
          duration: 2000
        })
      }
    })
}

export default {
  name: 'Friend',
  data () {
    return {
      count: 0,
      friends: []
    }
  },
  computed: {
    list_height: function () {
      return this.$store.state.html_height - 80 - 94 - 71
    },
    is_logined: function () {
      return this.$store.state.is_logined
    }
  },
  created: function () {
    this.$store.commit('changeHeight', document.body.clientHeight)
  },
  watch: {
    is_logined: function (val) {
      if (val === true) {
        fetchFriends(this, localStorage.user_id)
      }
    }
  }
}
</script>

<style scoped>
.friend-card {
  display: flex;
  flex-direction: column;
}
.infinite-list {
  height: 100%;
  margin: 0;
  padding: 0;
  list-style: none;
  overflow: auto;
}
.friend-main {
  background-color: #5646;
  width: 345px;
  top: 80px;
  bottom: 94px;
  display: flex;
  flex-direction: column;
}
</style>
