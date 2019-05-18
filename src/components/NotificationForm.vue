<template>
  <div class="notification-form">
    <h2>Create new SMS alert</h2>
    <form>
        <span>
            Create an alert, to recieve lift failure updates 
            for a specific train station (UK mobiles only)
        </span>
        
        <el-divider />
        
        <el-input placeholder="Mobile Number" type="tel" v-model="mobile">
            <template slot="prepend">+44</template>
        </el-input>

        <el-divider />

        <el-autocomplete
            :fetch-suggestions="stationSearch"
            placeholder="Station Name, or Code"
            v-model="station">
        </el-autocomplete>

        <el-divider />
        
        <span>Subscription Expirey</span>
        <el-date-picker
            v-model="date"
            type="date"
            placeholder="Pick a day">
        </el-date-picker>

        <el-divider />

         <span>Maximum Notifications per Day</span>
        <el-slider v-model="numNotifications"></el-slider>

        <el-divider />

        <el-button plain v-on:click="showSuccess">Schedule Notification</el-button>

        <br>

    </form>
  </div>
</template>

<script>
export default {
  name: 'NotificationForm',
  data() {
      return {
        mobile: '',
        station: '',  
        date: '',
        numNotifications: 70,
      };
    },
  methods: {
      stationSearch(queryString, cb) {
          window.setTimeout(()=> {
              cb([{ value: 'Barking'}, { value: 'Ilford'}, {value: 'Dagenham'}])
          }, 500);
      },
      open() {
        this.$message('This is a message.');
      },
      
      showSuccess() {
        const h = this.$createElement;
        this.$message({
          message: h('p', null, [
            h('b', null, `${this.station} Station `),
            h('span', null, 'notifications scheduled for '),
            h('b', null, this.mobile)
          ]),
          type: 'success',
        });
        this.mobile = '', this.station = '', this.date = '';
        // TODO Call to notification end point here
      }
  }
}
</script>

<style scoped lang="scss">
    form {
        display: flex;
        flex-direction: column;
        padding: 0 10px;
    }
</style>
