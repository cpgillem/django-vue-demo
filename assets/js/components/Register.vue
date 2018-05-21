<template>
    <div class="grid-container">
        <div class="grid-x">
            <div class="cell small-12 medium-6 medium-offset-3">
                <form @submit.prevent="register">
                    <label for="username">Username
                        <input id="username" name="username" type="text" v-model="username">
                    </label>
                    <label for="email">Email
                        <input id="email" name="email" type="email" v-model="email">
                    </label>
                    <label for="password1">Password
                        <input id="password1" name="password1" type="password" v-model="password1">
                    </label>
                    <label for="password2">Confirm Password
                        <input id="password2" name="password2" type="password" v-model="password2">
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
        };
    }, 

    methods: {
        register() {
            auth.register(this.username, this.password1, this.password2, this.email, res => {
                if (res) {
                    // Redirect to the home page.
                    this.$router.push('/home');
                } else {
                    // TODO: Show errors.
                }
            });
        },
    }
}
</script>