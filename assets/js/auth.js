import axios from 'axios';

export default {
    // Takes a username, password, and callback function. The callback function takes a boolean.
    login (username, password, next) {
        if (localStorage.token) {
            // If the token already exists, send true to the callback.
            next(true);
        } else {
            // If not, send a request for a new token.
            axios.post('/rest-auth/login/', {
                username,
                password,
            }).then(response => {
                if (response.data.key) {
                    // If the response has a key string, store that in localStorage.
                    localStorage.token = response.data.key
                    next(true);
                } else {
                    // If not, there has been an error.
                    next(false);
                }
            }).catch(error => {
                next(false);
            });
        }
    },

    getToken() {

    },

    logout() {

    },

    loggedIn() {
        return false;
    },
}