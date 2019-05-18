<template>
  <div class="home">

    <ChartSection />

    <BigSearchBar />

    <StationLifts 
      v-for="station in mockStationData"
      :key="station.stationCode"
      :station="station"
    />
  </div>
</template>

<script>

import StationLifts from '@/components/StationLifts.vue'
import BigSearchBar from '@/components/BigSearchBar.vue';
import ChartSection from '@/components/ChartSection.vue';

import mockStationData from '@/assets/mock-data.json'

export default {
  name: 'home',
  components: {
    StationLifts,
    BigSearchBar,
    ChartSection,
  },
  data(){
    return{
      mockStationData,
    }
  },
}
</script>
