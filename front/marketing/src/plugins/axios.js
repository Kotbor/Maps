import axios from 'axios';
import router from '@/router'
// doing something with the request
axios.interceptors.request.use(
    (request) => {
      let token = localStorage.getItem('access_token');
  
      if (token) {
        request.headers['Authorization'] = `Bearer ${ token }`;
      }
      
      return request;
    }, 
  
    (error) => {
      return Promise.reject(error);
    }
  );

// doing something with the response
axios.interceptors.response.use(
  (response) => {
     // all 2xx/3xx responses will end here
     
     return response;
  },
  (error) => {
     // all 4xx/5xx responses will end here
     if (error.response.status === 401){
         if (router.currentRoute.name !='Login'){
        router.push('/login')}
     }
     return Promise.reject(error);
  }
);

export default axios;