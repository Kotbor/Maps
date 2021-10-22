
<template>
   <v-container fill-height>
          <v-layout align-center justify-center>
          
            <login-page></login-page>
          </v-layout>
        </v-container>
    
</template>
<script>
// @ is an alias to /src
import LoginPage from '../components/LoginPage.vue'

export default {
  name: 'Login',
  components: {
    LoginPage
  }
}
</script>
