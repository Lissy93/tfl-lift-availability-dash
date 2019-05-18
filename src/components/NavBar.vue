<template>
    <div id="nav">
      <el-menu mode="horizontal">
          <el-menu-item index="1"><router-link to="/">Customer View</router-link></el-menu-item>
          <el-menu-item index="2"><router-link to="/contractor">Contractor View</router-link></el-menu-item>
          <el-menu-item index="3"><router-link to="/planner">Accesibility Journey PLanner</router-link></el-menu-item>
          <el-menu-item index="4"><router-link to="/map">Interactive Map</router-link></el-menu-item>
      </el-menu>
      <div class="line"></div>
    </div>
</template>

<script>
export default {
  name: 'NavBar',
}
</script>

<style scoped lang="scss">

</style>
