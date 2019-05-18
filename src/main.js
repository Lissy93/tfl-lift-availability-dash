import Vue from 'vue'
import Element from 'element-ui'
import VueApexCharts from 'vue-apexcharts'
import 'element-ui/lib/theme-chalk/index.css';

import '@/assets/global-styles.scss';

import App from './App.vue'
import router from './router'

Vue.use(VueApexCharts)
Vue.use(Element)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
