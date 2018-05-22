<template>
    <div class="grid-container">
        <div class="grid-x">
            <div class="cell small-12 medium-6 medium-offset-3">
                <p v-if="otherError.length > 0">{{ otherError }}</p>
                <form @submit.prevent="login">
                    <label for="username">Username
                        <input id="username" name="username" type="text" v-model="username">
                        <small v-if="usernameError.length > 0">{{ usernameError }}</small>
                    </label>
                    <label for="password">Password
                        <input id="password" name="password" type="password" v-model="password">
                        <small v-if="passwordError.length > 0">{{ passwordError }}</small>
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
            usernameError: '',
            passwordError: '',
            otherError: '',
        }
    },
    methods: {
        clearErrors() {
            this.otherError = '';
            this.usernameError = '';
            this.passwordError = '';
        },

        login() {
            this.clearErrors();
            
            auth.login(this.username, this.password, data => {
                if (data) {
                    if ('key' in data) {
                        // If the login is successful, redirect to home.
                        this.$router.push('/home');
                    } else {
                        // If there are validation errors, display them.
                        if ('username' in data) {
                            this.usernameError = data.username[0];
                        }

                        if ('password' in data) {
                            this.passwordError = data.password[0];
                        }

                        if ('non_field_errors' in data) {
                            this.otherError = data.non_field_errors[0];
                        }
                    }
                }
            })
        }
    }
}
</script>