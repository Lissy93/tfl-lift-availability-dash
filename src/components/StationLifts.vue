<template>
    <el-card class="station-lifts">
        <el-collapse v-model="collapseViewActive">
            <el-collapse-item name="tab">
                <template slot="title">
                    <div class="station-header">
                    <h3>{{ station.stationName }}</h3>
                    <StatusChip :statusCode="makeStatusCode"/>
                </div>
                </template>
                <div>
                    <StationStatusTable :liftData="station.lifts"/>
                </div>
            </el-collapse-item>
        </el-collapse>
    </el-card>
</template>

<script>

import StatusChip from '@/components/StatusChip.vue'
import StationStatusTable from '@/components/StationStatusTable.vue';

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
  data() {
      return {
        collapseViewActive: ['tab']
      };
    },
  components: {
    StatusChip,
    StationStatusTable,
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
                font-size: 1.8em;
            }
        }
        .station-lifts {
            display: flex;
            flex-direction: column;
        }
    }
    h3 {
        display: inline-block;
    }

</style>

