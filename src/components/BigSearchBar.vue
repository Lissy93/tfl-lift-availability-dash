<template>
    <el-card>
        <h2>Search </h2>
        <el-input 
          placeholder="Start typint station name or code"
          v-model="input"
          v-on:input="userIsTypingShit"
        ></el-input>
    </el-card>
</template>


<script>
export default {
  name: 'BigSearchBar',
  data() {
    return {
      input: ''
    }
  },
  methods: {
    userIsTypingShit(stuff) {
      this.$emit('user-is-searchin', stuff)
    }
  },
}
</script>

<style scoped lang="scss">
    .el-card {
        margin: 10px;
    }
    h2 {
      margin-top: 0;
    }
    /deep/ .el-input__inner {
        font-size: 2em;
        padding: 1em;
    }
</style>
