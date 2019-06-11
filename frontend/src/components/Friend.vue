<template>
  <div class="friend-main">
    <el-tabs type="border-card">
      <el-tab-pane label="好友">好友</el-tab-pane>
      <el-tab-pane label="群组">群组</el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
export default {
  name: 'Friend',
  data () {
    return {
      select_friend: true,
      count: 0,
      friends: []
    }
  },
  methods: {
    loadFriends () {
      this.count += 0
    }
  }
}
</script>

<style scoped>
.infinite-list {
  height: 100%;
  margin: 0;
  padding: 0;
  list-style: none;
  overflow: auto;
}
.friend-main {
  background-color: #5646;
  width: 400px;
  top: 80px;
  bottom: 94px;
  display: flex;
  flex-direction: column;
}
</style>
