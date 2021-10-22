import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';

import ru from 'vuetify/lib/locale/ru'

Vue.use(Vuetify);

Vue.component('my-component', {
    methods: {
      changeLocale () {
        this.$vuetify.lang.current = 'ru'
      },
    },
  })

export default new Vuetify({
    lang: {
        locales: { ru },
        current: 'ru',
      },
});
