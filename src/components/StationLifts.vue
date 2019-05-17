<template>
    <el-card class="station-lifts">
        <h3>
            {{station.stationName}}
        </h3>
        <LiftTile />
    </el-card>
</template>

<script>

import LiftTile from '@/components/LiftTile.vue'

export default {
  name: 'StationLifts',
  props: {
    station: Object,
  },
  components: {
    LiftTile
  }
}
</script>

<style lang="scss" scoped>

.station-lifts {
    margin: 10px;
}


</style>

