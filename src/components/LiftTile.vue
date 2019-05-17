<template>
  <div class="lift-tile">

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
        width: 60px;
        height: 25px;
        background: grey;
    }

</style>
