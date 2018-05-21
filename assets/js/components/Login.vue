<template>
    <div class="grid-container">
        <div class="grid-x">
            <div class="cell small-12 medium-6 medium-offset-3">
                <form @submit.prevent="login">
                    <label for="username">Username
                        <input id="username" name="username" type="text" v-model="username">
                    </label>
                    <label for="password">Password
                        <input id="password" name="password" type="password" v-model="password">
                    </label>
                    <input class="button" type="submit" value="Login">
                </form>
            </div>
        </div>
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