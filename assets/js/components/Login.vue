<template>
    <div>
        <form @submit.prevent="login">
            <label for="username">Username
                <input id="username" name="username" type="text" v-model="username">
            </label>
            <label for="password">Password
                <input id="password" name="password" type="password" v-model="password">
            </label>
            <input type="submit" value="Login">
        </form>
    </div>
</template>

<script>
import auth from '../auth';

export default {
    data() {
        return {
            username: '',
            password: '',
        }
    },
    methods: {
        login() {
            auth.login(this.username, this.password, res => {
                if (res) {
                    // If the login is successful, redirect to home.
                    this.$router.push('/home');
                }
            })
        }
    }
}
</script>