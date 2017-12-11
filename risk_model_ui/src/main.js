import Vue from 'vue'
import VueRouter from 'vue-router'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import App from './App.vue'
import RiskList from './RiskList.vue'
import RiskDetail from './RiskDetail.vue'
import jQuery from 'jquery';

window.jQuery = jQuery;
window.$ = jQuery;

Vue.use(BootstrapVue);
Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    redirect: '/risks'
  },
  {
    path: '/risks',
    component: RiskList
  },
  {
    path: '/risks/:id',
    component: RiskDetail
  }
];

const router = new VueRouter({
  routes
});

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
