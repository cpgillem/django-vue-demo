<template>
    <div>
        <h1>Lists</h1>
        <ul>
            <li v-for="list in lists" v-bind:key="list.url">
                <List v-bind:list="list" v-on:select-list="selectedList = list"/>
            </li>
        </ul>
        <h1>Items</h1>
        <ListViewer v-bind:list="selectedList"/>
    </div>
</template>

<script>
import List from './List.vue';
import ListViewer from './ListViewer.vue';

import axios from 'axios';
import auth from '../auth';

export default {
    data() {
        return {
            lists: [],
            selectedList: null,
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
                headers: auth.getHeaders(),
            }).then(res => {
                // Once the lists are loaded, store them in the list variable.
                this.lists = res.data;
            });
        }
    },
    components: {
        List,
        ListViewer,
    }
}
</script>