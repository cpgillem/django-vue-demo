import axios from 'axios';

export default {
    // Takes a username, password, and callback function. The callback function takes a boolean.
    login(username, password, next) {
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
        return localStorage.token;
    },

    // Creates a headers object for axios requests.
    getHeaders() {
        return {
            'Authorization': 'Token ' + this.getToken(),
        };
    },

    logout() {
        delete localStorage.token;
    },

    loggedIn() {
        return !!localStorage.token;
    },

    // Takes a callback function to be called upon retrieval of the user. 
    // This function takes an object representing the user as an argument.
    getUser(next) {
        if (this.loggedIn()) {
            axios.get('/rest-auth/user/', {
                headers: {
                    'Authorization': 'Token ' + this.getToken(),
                }
            }).then(response => {
                // Send the user to the callback function.
                next(response.data);
            });
        }
    }
}