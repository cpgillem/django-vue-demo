<template>
    <div>
        <h1>{{ list.name }}</h1>
        <button class="button" @click="$emit('create-item', list)">New Item</button>
        <ul>
            <li v-for="item in list.items" v-bind:key="item.url">
                <Item 
                    v-bind:item="item" 
                    v-on:update-item="updateItem"
                    v-on:delete-item="$emit('delete-item', item)"
                />
            </li>
        </ul>
    </div>
</template>

<script>
import Item from './Item.vue';

export default {
    props: [
        'list',
    ],

    data() {
        return {
        };
    },

    components: {
        Item,
    },
    
    methods: {
        // Propagates the item change upward for the home component. 
        updateItem(item) {
            this.$emit('update-item', item);
        },
    }
}
</script>