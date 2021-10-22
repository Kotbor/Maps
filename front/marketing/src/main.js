import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import router from './router'
import VueAxios from 'vue-axios';
import axios from './plugins/axios'
import qs from 'qs';


Vue.config.productionTip = false
Vue.use(VueAxios, axios, qs);
new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
