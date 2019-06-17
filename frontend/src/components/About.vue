<template>
  <div>
    <h1 id="about">Good {{ time }}!</h1>
  </div>
</template>

<script>

export default {
  name: 'about',
  computed: {
    time () {
      let date = new Date()
      if (date.getHours() > 5 && date.getHours() <= 12) {
        return 'morning'
      } else if (date.getHours() > 12 && date.getHours() < 18) {
        return 'afternoon'
      } else {
        return 'evening'
      }
    }
  },
  methods: {

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
