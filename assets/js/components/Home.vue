<template>
    <div>
        {{ lists }}
    </div>
</template>

<script>
import axios from 'axios';
import auth from '../auth';

export default {
    data() {
        return {
            lists: [],
        };
    },
    created() {
        this.fetchData();
    },
    watch: {
        '$route': 'fetchData',
    },
    methods: {
        fetchData() {
            axios.get('/api/lists', {
                headers: {
                    'Authorization': 'Token ' + auth.getToken(),
                }
            }).then(res => {
                // Once the lists are loaded, store them in the list variable.
                this.lists = res.data;
            });
        }
    }
}
</script>