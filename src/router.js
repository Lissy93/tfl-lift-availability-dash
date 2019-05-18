import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import Contractor from './views/Contractor.vue';
import Map from './views/Map.vue';
import Planner from './views/Planner.vue';

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/contractor',
      name: 'contractor',
      component: Contractor
    },
    {
      path: '/map',
      name: 'map',
      component: Map
    },
    {
      path: '/planner',
      name: 'planner',
      component: Planner
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    }
  ]
})
