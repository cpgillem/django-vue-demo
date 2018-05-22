import axios from 'axios';

export default {
    // Takes a username, password, and callback function. The callback function takes an object.
    login(username, password, done) {
        if (localStorage.token) {
            // If the token already exists, send the key to the callback.
            done({
                "key": localStorage.token,
            });
        } else {
            // If not, send a request for a new token.
            axios.post('/rest-auth/login/', {
                username,
                password,
            }).then(response => {
                if ('key' in response.data) {
                    // If the response has a key string, store that in localStorage.
                    localStorage.token = response.data.key
                }
                done(response.data);
            }).catch(error => {
                if (error.response) {
                    done(error.response.data);
                }
            });
        }
    },

    // Takes a username, password, password confirmation, email, and a callback function.
    // The callback function takes a boolean as an argument.
    register(username, password1, password2, email, done) {
        // If there is someone logged in, log them out.
        if (this.loggedIn()) {
            this.logout();
        }

        // Send a request to create a new user.
        axios.post('/rest-auth/registration', {
            username,
            password1,
            password2,
            email,
        }).then(response => {
            // If successful, log the user in.
            if (response.data.key) {
                localStorage.token = response.data.key;
                done(true);
            } else {
                done(false);
            }
        });
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
    getUser(done) {
        if (this.loggedIn()) {
            axios.get('/rest-auth/user/', {
                headers: {
                    'Authorization': 'Token ' + this.getToken(),
                }
            }).then(response => {
                // Send the user to the callback function.
                done(response.data);
            });
        }
    }
}