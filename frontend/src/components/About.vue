<template>
  <div>
    <div id="test-send">
      <el-button @click="getDetail">add</el-button>
    </div>
    <div id="about">
      When you have a great story about how your product or service was built to change lives, share it. The "About Us"
      page is a great place for it to live, too. Good stories humanize your brand, providing context and meaning for your
      product. What’s more, good stories are sticky -- which means people are more likely to connect with them and pass
      them on.
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'about',
  methods: {
    getDetail: function () {
      axios.get('http://192.168.1.102:8000/musync/5/results/')
        .then(function (response) {
          alert(response.data)
        })
        .catch(function (error) {
          alert('Error!' + error)
        })
    }
  }
}
</script>

<style scoped>
#about {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
