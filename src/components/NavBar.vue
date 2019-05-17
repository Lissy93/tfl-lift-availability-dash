<template>
    <div id="nav">
        
<el-menu mode="horizontal">
    <el-menu-item index="0"><router-link to="/">Home</router-link></el-menu-item>
    <el-menu-item index="4"><router-link to="/about">About</router-link></el-menu-item>

    <el-menu-item index="1">Lift Status</el-menu-item>
    <el-menu-item index="2">Plan your Journey</el-menu-item>


</el-menu>
<div class="line"></div>


      <!-- <router-link to="/">Home</router-link>  -->
      <!-- <router-link to="/about">Stuff</router-link> -->
    </div>
</template>

<script>
export default {
  name: 'NavBar',
}
</script>

<style scoped lang="scss">

</style>
