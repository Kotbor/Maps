<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        


      </div>

      <v-spacer></v-spacer>

      Адреса доставки
    </v-app-bar>

    <v-main>
      <v-row>
        <v-col cols="6" style="height: 600px">
      
        <yandex-map v-if="coords" :settings="settings" :coords="coords" zoom=11>
              <ymap-marker 
            marker-id="Blue" 
            :coords="coords"
            marker-type="Circle"
            :circle-radius=blue_radius
          />
            <ymap-marker 
            marker-id="Red" 
            :coords="coords"
            marker-type="Circle"
            :marker-fill="red_fill"
            :marker-stroke="red_stroke"
            :circle-radius=red_radius
          />

      </yandex-map>
       </v-col>
      </v-row>
     
     <v-row>
        <v-col class="px-4" cols="6">
          <v-range-slider
            v-model="range"
            :max="max"
            :min="min"
            step=0.5
            hide-details
            class="align-center"
          >
            <template v-slot:prepend>
              <v-text-field
                :value="range[0]"
                class="mt-0 pt-0"
                hide-details
                single-line
                type="number"
                style="width: 60px"
                @change="$set(range, 0, $event)"
              ></v-text-field>
            </template>
            <template v-slot:append>
              <v-text-field
                :value="range[1]"
                class="mt-0 pt-0"
                hide-details
                single-line
                type="number"
                style="width: 60px"
                @change="$set(range, 1, $event)"
              ></v-text-field>
            </template>
          </v-range-slider>
        </v-col>
      </v-row>

    </v-main>
  </v-app>
</template>

<script>
import { yandexMap, ymapMarker, loadYmap} from 'vue-yandex-maps'
export default {
  
  
  
  name: 'App',
  
  components: {
    yandexMap, ymapMarker
    },


  data: () => ({
    settings: {
      apiKey: 'd5e4d19e-92c9-4d74-9256-02e7bf450f4e',
      lang: 'ru_RU',
      coordorder: 'latlong',
      version: '2.1',
      },
    coords: null, //[59.94, 30.32],
    red_fill:{"color":"#DB709377"},
    red_stroke:{"color":"#DB7093FF"},
    min: 1,
    max: 5,
    range: [1, 5],

  
  }),
  computed:{

    red_radius: function(){
      return this.range[1]*1000
    },
    blue_radius: function(){
      return this.range[0]*1000},
  },
    async mounted() {
    await loadYmap({ ...this.settings, debug: true });

    ymaps.geolocation.get().then((res) => {
      this.coords = res.geoObjects.position;
      console.log(this.coords);
    });
  },
  
};
</script>

<style>
.ymap-container {
  height: 100%;
}
</style>