<template>
  <div id="app">
    <NavBar />
    <router-view/>
  </div>
</template>


<script>
import NavBar from '@/components/NavBar.vue'
export default {
  name: 'App',
  components: {
    NavBar,
  }
}
</script>

<style lang="scss">

body {
  background: #f1f1f1;
  margin: 0;
}

</style>
