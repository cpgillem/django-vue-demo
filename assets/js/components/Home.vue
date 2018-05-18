<template>
    <div>
        <h1>Lists</h1>
        <button @click="createList">New List</button>
        <ul>
            <li v-for="list in lists" v-bind:key="list.url">
                <List
                    v-bind:list="list" 
                    v-on:select-list="selectedList = list"
                    v-on:update-list="updateList"
                    v-on:delete-list="deleteList"
                />
            </li>
        </ul>
        <h1>Items</h1>
        <ListViewer 
            v-bind:list="selectedList" 
            v-on:update-item="updateItem"
            v-on:create-item="createItem"
            v-on:delete-item="deleteItem"
        />
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
            // Central store of lists with their items.
            lists: [],

            // The logged in user.
            user: null,

            // The currently selected list.
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
        // Load all lists and their items.
        fetchData() {
            axios.get('/api/lists/', {
                headers: auth.getHeaders(),
            }).then(res => {
                // Once the lists are loaded, store them in the list variable.
                this.lists = res.data;
            });
            
            // Retrieve the current user.
            auth.getUser(u => {
                this.user = u;
            });
        },

        // Add a new list.
        createList() {
            // Create a new list with default values.
            axios.post('/api/lists/', {
                name: 'New List',
                owner: this.user.profile,
            }, {
                headers: auth.getHeaders(),
            }).then(res => {
                this.fetchData();
            })
        },

        // Add a new item.
        createItem(list) {
            // Create a new item in the list.
            axios.post('/api/items/', {
                title: 'New Item',
                parent_list: list.url,
            }, {
                headers: auth.getHeaders(),
            }).then(res => {
                // TODO: Update selectedList
                this.fetchData();
            })
        },

        // Update a list.
        updateList(list) {
            axios.put(list.url, list, {
                headers: auth.getHeaders(),
            }).then(res => {
                // TODO: Update state more efficiently
                this.fetchData();
            });
        },

        // Update an item.
        updateItem(item) {
            axios.put(item.url, item, {
                headers: auth.getHeaders(),
            }).then(res => {
                // TODO: Update state more efficiently
                // TODO: Update selectedList
                this.fetchData();
            });
        },

        // Delete a list.
        deleteList(list) {
            axios.delete(list.url, {
                headers: auth.getHeaders(),
            }).then(res => {
                this.fetchData();
            });
        },

        // Delete an item.
        deleteItem(item) {
            axios.delete(item.url, {
                headers: auth.getHeaders(),
            }).then(res => {
                this.fetchData();
            });
        },
    },
    components: {
        List,
        ListViewer,
    }
}
</script>