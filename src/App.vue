<template>
  <div id="app">
    <DemoBanner />
    <NavBar />
    <router-view/>
  </div>
</template>


<script>
import NavBar from '@/components/NavBar.vue'
import DemoBanner from '@/components/DemoBanner.vue'
export default {
  name: 'App',
  components: {
    NavBar,
    DemoBanner,
  }
}
</script>

<style lang="scss">

body {
  background: #f1f1f1;
  margin: 0;
}

</style>
