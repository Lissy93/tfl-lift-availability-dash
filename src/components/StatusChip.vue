<template>
  <div class="status-chip">
    <el-tag v-if="statusCode == 2" type="success">
        Operational
    </el-tag>
    <el-tag v-else-if="statusCode == 1" type="warning">
        Some Restrictions
    </el-tag>
    <el-tag v-else-if="statusCode == 0" type="danger">
        Critical
    </el-tag>
    <el-tag v-else type="info">
        Unknown
    </el-tag>
  </div>
</template>

<script>
export default {
  name: 'StatusChip',
  props: {
    statusCode: Number,
  }
}
</script>

<style lang="scss" scoped>

  .el-tag {
    font-size: 1em;
    display: inline-block;
    cursor: default;
  }

</style>

