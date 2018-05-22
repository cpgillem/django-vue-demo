<template>
    <div class="grid-container">
        <div class="grid-x">
            <div class="cell small-12 medium-6 medium-offset-3">
                <p v-if="otherError.length > 0">{{ otherError }}</p>
                <form @submit.prevent="register">
                    <label for="username">Username
                        <input id="username" name="username" type="text" v-model="username">
                        <small v-if="usernameError.length > 0">{{ usernameError }}</small>
                    </label>
                    <label for="email">Email
                        <input id="email" name="email" type="email" v-model="email">
                        <small v-if="emailError.length > 0">{{ emailError }}</small>
                    </label>
                    <label for="password1">Password
                        <input id="password1" name="password1" type="password" v-model="password1">
                        <small v-if="password1Error.length > 0">{{ password1Error }}</small>
                    </label>
                    <label for="password2">Confirm Password
                        <input id="password2" name="password2" type="password" v-model="password2">
                        <small v-if="password2Error.length > 0">{{ password2Error }}</small>
                    </label>
                    <input class="button" type="submit" value="Register">
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
            password1: '',
            password2: '',
            email: '',
            otherError: '',
            usernameError: '',
            emailError: '',
            password1Error: '',
            password2Error: '',
        };
    }, 

    methods: {
        clearErrors() {
            this.otherError = '';
            this.usernameError = '';
            this.emailError = '';
            this.password1Error = '';
            this.password2Error = '';
        },

        register() {
            auth.register(this.username, this.password1, this.password2, this.email, res => {
                this.clearErrors();
                
                if ('key' in res) {
                    // Redirect to the home page.
                    this.$router.push('/home');
                } else {
                    if ('username' in res) {
                        this.usernameError = res.username[0];
                    }

                    if ('email' in res) {
                        this.emailError = res.email[0];
                    }

                    if ('password1' in res) {
                        this.password1Error = res.password1[0];
                    }

                    if ('password2' in res) {
                        this.password2Error = res.password2[0];
                    }

                    if ('non_field_errors' in res) {
                        this.otherError = res.non_field_errors[0];
                    }
                }
            });
        },
    }
}
</script>