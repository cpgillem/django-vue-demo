<template>
    <div class="grid-container">
        <div class="grid-x grid-padding-x">
            <div class="cell small-12 medium-4">
                <h1>Lists</h1>
                <button class="button" @click="createList">New List</button>
                <ul>
                    <li v-for="list in lists" v-bind:key="list.url">
                        <List
                            v-bind:list="list" 
                            v-on:select-list="selectedListUrl = list.url"
                            v-on:update-list="updateList"
                            v-on:delete-list="deleteList"
                            v-bind:selected="isListSelected(list)"
                        />
                    </li>
                </ul>
            </div>
            <div class="cell small-12 medium-8">
                <ListViewer 
                    v-if="selectedList !== null"
                    v-bind:list="selectedList" 
                    v-on:update-item="updateItem"
                    v-on:create-item="createItem"
                    v-on:delete-item="deleteItem"
                />
            </div>
        </div>
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

            // The currently selected list url.
            selectedListUrl: null,
        };
    },

    computed: {
        // The currently selected list.
        selectedList() {
            var filter = this.lists.filter(this.isListSelected);

            // If the list was found, return it.
            if (filter.length > 0) {
                return filter[0];
            } else {
                return null;
            }
        }
    },

    created() {
        // Fetch all the list and user data.
        this.fetchData();
    },

    watch: {
        '$route': 'fetchData',
    },

    methods: {
        isListSelected(list) {
            return this.selectedListUrl == list.url;
        },

        // Load all lists and their items.
        fetchData(then) {
            axios.get('/api/lists/', {
                headers: auth.getHeaders(),
            }).then(res => {
                // Once the lists are loaded, store them in the list variable.
                this.lists = res.data;

                // Retrieve the current user.
                auth.getUser(u => {
                    this.user = u;

                    // Select the first list if there are any, after the data has been fetched.
                    if (this.selectedListUrl == null && this.lists.length > 0) {
                        this.selectedListUrl = this.lists[0].url;
                    }

                    // Run the callback function if there is one.
                    if (then) then();
                });
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
                // TODO: Update state more efficiently
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
                // TODO: Update state more efficiently
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
                this.fetchData();
            });
        },

        // Delete a list.
        deleteList(list) {
            axios.delete(list.url, {
                headers: auth.getHeaders(),
            }).then(res => {
                // TODO: Update state more efficiently
                this.fetchData();
            });
        },

        // Delete an item.
        deleteItem(item) {
            axios.delete(item.url, {
                headers: auth.getHeaders(),
            }).then(res => {
                // TODO: Update state more efficiently
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