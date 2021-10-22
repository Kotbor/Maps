<template>
 <div>
 <v-toolbar color="dark blue" dark fixed>
        <v-toolbar-title @click="$router.push('renters')">Контакты</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-toolbar-items class="hidden-sm-and-down">
          <v-btn v-for="item in menu" :key="item.icon" :to="item.link" text>{{
            item.title
          }}</v-btn>
        </v-toolbar-items>
        <v-menu class="hidden-md-and-up">
          
          <v-list>
            <v-list-tile v-for="item in menu" :key="item.icon" :to="item.link">
              <v-list-tile-content>
                <v-list-tile-title>{{ item.title }}</v-list-tile-title>
              </v-list-tile-content>
            </v-list-tile>
          </v-list>
        </v-menu>
      </v-toolbar>
<router-view></router-view>
</div>
</template>


<script>
  
  export default {
    data: () => ({
      
      menu: [
        { icon: "home", title: "Пользователи", link:"users" },
        { icon: "info", title: "Cправочники", link:"options" },
      ],
      
    }),

    
  }
</script>