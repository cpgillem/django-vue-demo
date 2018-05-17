import Vue from 'vue'
import VueRouter from 'vue-router'

import App from './App.vue'
import Landing from './components/Landing.vue';
import Home from './components/Home.vue';
import Login from './components/Login.vue';
import Register from './components/Register.vue';

Vue.config.productionTip = false
Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        component: Landing
    },
    {
        path: '/home',
        component: Home
    },
    {
        path: '/login',
        component: Login
    },
    {
        path: '/register',
        component: Register
    },
];

const router = new VueRouter({
    routes
});

new Vue({
    render: h => h(App),
    components: {
        App,
        Landing,
        Home,
        Login,
        Register
    },
    router,
}).$mount('#app')