import Vue from 'vue'
import VueRouter from 'vue-router'

import App from './App.vue'
import Landing from './components/Landing.vue';
import Home from './components/Home.vue';
import Login from './components/Login.vue';
import Register from './components/Register.vue';

import auth from './auth';

/* Import the styling for the app. */
import '../css/app.css';

/* Configure Vue. */
Vue.config.productionTip = false
Vue.use(VueRouter);

/* Create a guard to add to private routes. */
function authGuard(to, from, next) {
    if (auth.loggedIn()) {
        next();
    } else {
        next('/login');
    }
}

/* Define the routes. */
const routes = [
    {
        path: '/',
        component: Landing,
        beforeEnter(to, from, next) {
            if (auth.loggedIn()) {
                next('/home');
            } else {
                next();
            }
        }
    },
    {
        path: '/home',
        component: Home,
        beforeEnter: authGuard,
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

/* Create a router. */
const router = new VueRouter({
    routes,
});

/* Create a new Vue instance with the router. */
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