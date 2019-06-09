<template>
  <div>
    <el-popover placement="top" width="320">
      <el-table :data="list">
        <el-table-column prop="order" label="序号" width="50"></el-table-column>
        <el-table-column prop="full_title" label="歌名" width="200"></el-table-column>
        <el-table-column prop="full_artist" label="歌手"></el-table-column>
      </el-table>
      <el-button class="el-icon-s-fold" slot="reference"></el-button>
    </el-popover>
  </div>
</template>

<script>
export default {
  name: 'MusicList',
  data () {
    return {
      list: [
        {
          order: 1,
          full_title: 'さくら~あなたに出会えてよかった~[清明樱花祭]',
          full_artist: 'RSP'
        },
        {
          order: 2,
          full_title: 'さくら~あなたに出会えてよかった~[清明樱花祭]',
          full_artist: 'RSP'
        },
        {
          order: 3,
          full_title: 'さくら~あなたに出会えてよかった~[清明樱花祭]',
          full_artist: 'RSP'
        }
      ]
    }
  }
}
</script>

<style scoped>
</style>
