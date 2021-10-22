<template>
  <v-main>
    <v-container fluid fill-height>
      <v-layout align-center justify-center>
        <v-flex xs12 sm8 md4>
          <v-card class="elevation-12">
            <v-toolbar dark color="primary">
              <v-toolbar-title>{{appName}}</v-toolbar-title>
              <v-spacer></v-spacer>
            </v-toolbar>
            <v-card-text>
              <v-form @keyup.enter="submit">
                <v-text-field @keyup.enter="submit" v-model="email"  name="login" label="Логин" type="text"></v-text-field>
                <v-text-field @keyup.enter="submit" v-model="password" name="password" label="Пароль" id="password" type="password"></v-text-field>
              </v-form>
              <div v-if="loginError">
                <v-alert :value="loginError" transition="fade-transition" type="error">
                  Неверный пароль или логин
                </v-alert>
              </div>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn @click.prevent="submit">Войти</v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-main>
</template>

<script>
//import axios from 'axios';
import qs from 'qs';
  export default {
    name: 'Login',

    data: () => ({
      loginError:null,
      password:null,
      email:null,
      appName:"Адреса"
    }),
    methods: {
      submit: function(){
        var reqData = qs.stringify({"username":this.email,"password":this.password})
        this.axios({
          method: 'post',
          url:'http://192.168.10.5:8000/api/token',
          headers: { 'content-type': 'application/x-www-form-urlencoded' },
          data: reqData,
        }).then((result) =>{
        
          localStorage.access_token = result.data.access_token;
          this.$router.push('/tables/renters')
        }).catch(()=> {this.loginError=true})
        
      }
    }
  }
</script>