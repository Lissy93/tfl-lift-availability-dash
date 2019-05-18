<template>
  <div class="home">

    <BigSearchBar @user-is-searchin="searching" />

    <span v-if="searchStation.length > 0" class="result-summary">
      Showing {{filteredStations.length}} 
      result{{filteredStations.length>1? 's': ''}}
      for '{{searchStation}}'
    </span>

    <StationLifts 
      v-for="station in filteredStations"
      :key="station.stationCode"
      :station="station"
    />
  </div>
</template>

<script>

import StationLifts from '@/components/StationLifts.vue'
import BigSearchBar from '@/components/BigSearchBar.vue';

import mockStationData from '@/assets/mock-data.json'

export default {
  name: 'home',
  components: {
    StationLifts,
    BigSearchBar,
  },
  methods: {
    searching(searchStation){
      this.searchStation = searchStation;
    }
  },
  data(){
    return{
      mockStationData,
      searchStation: '',
    }
  },
  computed: {
    filteredStations() {
      return this.mockStationData.filter(station => {
        return station.name.toLowerCase().includes(this.searchStation.toLowerCase())
      })
    }
  },
}
</script>

<style lang="scss" scoped>

.result-summary {
  color: #939393;
   margin: 10px;
}
</style>
