<template>
    <div id="app">
        <div class="grid-container fluid">
            <div class="top-bar">
                <div class="top-bar-left">
                    <ul class="menu">
                        <li class="menu-text">Django+Vue Demo</li>
                        <li><router-link to="/home">Home</router-link></li>
                        <li v-if="loggedIn()"><a href="#" @click.prevent="logout">Logout</a></li>
                        <li v-else><router-link to="/login">Login</router-link></li>
                        <li v-if="!loggedIn()"><router-link to="/register">Register</router-link></li>
                    </ul>
                </div>
            </div>
        </div>
        <router-view></router-view>
    </div>
</template>

<script>
import auth from './auth.js';

export default {
    name: 'app',
    methods: {
        loggedIn() {
            console.log('checking logged in');
            return auth.loggedIn();
        },

        logout() {
            auth.logout();
            this.$router.push('/');
        }
    },
    computed: {
        
    }
}
</script>