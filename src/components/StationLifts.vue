<template>
    <el-card class="station-lifts">
        <div class="station-header">
            <h3>{{ station.stationName }}</h3>
            <StatusChip :statusCode="makeStatusCode"/>
        </div>
        
        <LiftTile />
    </el-card>
</template>

<script>

import LiftTile from '@/components/LiftTile.vue'
import StatusChip from '@/components/StatusChip.vue'


export default {
  name: 'StationLifts',
  props: {
    station: Object,
  },
  computed: {
    makeStatusCode() {
        const lifts = this.station.lifts;
        return Math.min.apply(Math, lifts.map((lift) => lift.status));
      }
  },
  components: {
    LiftTile,
    StatusChip,
  }
}
</script>

<style lang="scss" scoped>
    .station-lifts {
        margin: 10px;
        .station-header {
            display: flex;
            h3, .status-chip {
                display: flex;
                justify-content: center;
                align-items: center;
                margin-right: 8px;
            }
        }
    }
    h3 {
        display: inline-block;
    }

</style>

