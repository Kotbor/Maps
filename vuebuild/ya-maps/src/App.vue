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
      
        <yandex-map :settings="settings" :coords="coords" zoom=11 :use-object-manager= true @map-was-initialized="mapLoaded">


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
import { yandexMap} from 'vue-yandex-maps'
export default {
  
  
  
  name: 'App',
  
  

  components: {
    yandexMap
    },


  data: () => ({
    settings: {
      apiKey: 'd5e4d19e-92c9-4d74-9256-02e7bf450f4e',
      lang: 'ru_RU',
      coordorder: 'latlong',
      version: '2.1',
      },
    
    coords: [59.94, 30.32],
    circ_coords: [59.94, 30.32],
    red_fill:{"color":"#DB709377"},
    red_stroke:{"color":"#DB7093FF"},
    min: 1,
    max: 5,
    range: [1, 15],
    red_circle: null,
    blue_circle:null,
    map_inst: null,
    all_objects:null,
  
  }),

watch: {
  range: function(){
    if (this.blue_circle){
    var storage = ymaps.geoQuery(this.all_objects) //.addToMap(this.map_inst)
    this.blue_circle.geometry.setRadius(this.range[0]*1000)
    //var objectsContainingBlue = result.searchInside(this.blue_circle)
    var searched_blue = storage.searchInside(this.blue_circle)
    searched_blue.setOptions({
      fillColor: "#ff001a"
    })
    //console.log(objectsContainingBlue)
    searched_blue.each(function(it){
      console.log(it.properties._data.balloonContent)
    })
    
  }
    
    if (this.red_circle){
    this.red_circle.geometry.setRadius(this.range[1]*1000)
  }}
},


methods: {
   
    mapLoaded: function(inst){
        this.map_inst = inst ;
        var currentId = 0;
        var objectManager = new ymaps.ObjectManager({
        // Включаем кластеризацию.
        clusterize: true,
        // Опции кластеров задаются с префиксом 'cluster'.
        clusterHasBalloon: false,
        // Опции геообъектов задаются с префиксом 'geoObject'.
        geoObjectOpenBalloonOnClick: false
        });
        // Добавляем красный круг.
        var redCircle = new ymaps.GeoObject({
              geometry: {
                          type: "Circle",
                          coordinates: [59.94, 30.32],
                          radius: this.range[1]*1000,
                          
                        },
             
        });
        redCircle.options.set( {
          fillColor:"#DB709377",
          strokeColor:"#DB7093FF"
          })
        
        // копируем круг в data, чтобы иметь к нему доступ вне функции
        this.red_circle=redCircle;
        // Добавляем синий круг.
        var blueCircle = new ymaps.GeoObject({
              geometry: {
                          type: "Circle",
                          coordinates: [59.94, 30.32],
                          radius: this.range[0]*1000,
                        },
        });
        
        blueCircle.options.set( {
        fillColor:"#0099ff77",
        strokeColor:"#0099ffFF"
        })

        // копируем круг в data, чтобы иметь к нему доступ вне функции
        this.blue_circle=blueCircle;

        inst.geoObjects.add(blueCircle)
        inst.geoObjects.add(redCircle)
      
      
      // Добавим единичный объект.
        var map_objects = {
              type: 'Feature',
              id: currentId++,
              geometry: {
                  type: 'Point',
                  coordinates: [59.93, 30.31]
              },
              properties: {
                  hintContent: 'Содержание всплывающей подсказки',
                  balloonContent: 'Содержание балуна'
              }
          }
        
        // Чтобы отображать большое количество объектов на карте бех тормозов - используем objectManager
        objectManager.add(map_objects);
        // Отображаем объекты на карте
        inst.geoObjects.add(objectManager);
        this.all_objects = map_objects
  },
  }

  
};
</script>

<style>
.ymap-container {
  height: 100%;
}
</style>