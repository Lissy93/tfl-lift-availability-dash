<template>
  <div class="contracotr">
    <h1>Lift Maintenance Contractor Dashboard</h1>
    <el-divider></el-divider>
    <ChartSection />
    <el-divider></el-divider>
    <el-card>
      <h2>Top Priority Maintenance Jobs</h2>
      <el-table
        :data="tableData"
        style="width: 100%">
        <el-table-column
          prop="date"
          label="Date"
          width="180">
        </el-table-column>
        <el-table-column
          prop="name"
          label="Line"
          width="180">
        </el-table-column>
        <el-table-column
          prop="address"
          label="Address">
        </el-table-column>
      </el-table>
    </el-card>
  </div>
</template>

<script>
import ChartSection from '@/components/ChartSection.vue';

export default {
    components: {
        ChartSection,
    },
    data() {
        return {
          tableData: [{
            date: '2016-05-03',
            name: 'Central Line',
            address: 'Liverpool St, London EC2M 7QH'
          }, {
            date: '2016-05-02',
            name: 'Central Line',
            address: 'Mile End Rd, Mile End, London E3 4DH'
          }, {
            date: '2016-05-04',
            name: 'Northern Line',
            address: 'Euston Rd, Kings Cross, London N1 9AL'
          }, {
            date: '2016-05-01',
            name: 'District Line',
            address: 'Barking Station, Station Parade, Barking IG11 8TU'
          }]
        }
      }
}
</script>

<style lang="scss" scoped>
.contracotr {
    margin: 10px;
    padding: 15px;
}
</style>


