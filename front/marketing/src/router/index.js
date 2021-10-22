import Vue from 'vue'
import VueRouter from 'vue-router'
//import Home from '../views/Home.vue'
import axios from '../plugins/axios'

Vue.use(VueRouter)

const routes = [

  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/tables',
    name: 'Tables',
    alias: '/',
    meta: {
          requiresAuth: true
        },
    children:[
      {path: 'renters',
      component:() => import('../views/Renters.vue')},
      {path: 'options',
      component:() => import('../views/Options.vue')},
      {path: 'users',
      component:() => import('../views/Users.vue')}
    ],
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Tables.vue'),
   
  
    
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})
//Meta Handling
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (localStorage.getItem('access_token') == null) {
      next({
        path: '/login',
        params: { nextUrl: to.fullPath }
      })
    }     
    
    else {
      axios({
        method: 'get',
        url:'http://192.168.10.5:8000/api/auth/user',
      }).then((result) =>{
        console.log(result.data);
      })
      
      let user = JSON.parse(localStorage.getItem('user'))
      if (to.matched.some(record => record.meta.is_admin)) {
        if (user.is_admin == 1) {
          next()
        } else {
          next({ name: '/logout' })
        }
      } else {
        next()
      }
    }
  } else if (to.matched.some(record => record.meta.guest)) {
    if (localStorage.getItem('token') == null) {
      next()
    } else {
      next({ name: 'userboard' })
    }
  } else {
    next()
  }
})



export default router
