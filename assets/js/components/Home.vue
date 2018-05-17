<template>
    <div>
        <h1>Lists</h1>
        <ul>
            <li v-for="list in lists" v-bind:key="list.url">
                <List v-bind:list="list"/>
            </li>
        </ul>
    </div>
</template>

<script>
import List from './List.vue';

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
    },
    components: {
        List
    }
}
</script>