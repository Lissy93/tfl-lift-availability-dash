<template>
  <div class="lift-tile">
      <span class="lift-name">{{ liftName }}</span>
      <span class="lift-status">{{ statusCode }}</span>
      
  </div>
</template>

<script>

export default {
  name: 'LiftTile',
  props: {
    liftName: String,
    statusCode: Number, // 0 = Red, 1 = Amber, 2 = Green
    details: String,
  }
}
</script>

<style scoped lang="scss">
    .lift-tile {

    }

</style>
