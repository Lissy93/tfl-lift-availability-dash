<template>
  <div class="home">

    
    <StationLifts 
      v-for="station in mockStationData"
      :key="station.stationCode"
      :station="station"
    />
  </div>
</template>

<script>

import StationLifts from '@/components/StationLifts.vue'

import mockStationData from '@/assets/mock-data.json'

export default {
  name: 'home',
  components: {
    StationLifts
  },
  data(){
    return{
      mockStationData,
    }
  },
}
</script>
