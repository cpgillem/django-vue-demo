<template>
    <ul>
        <li v-for="item in list.items" v-bind:key="item.url">
            <Item v-bind:item="item"/>
        </li>
    </ul>
</template>

<script>
import Item from './Item.vue';

import auth from '../auth';

export default {
    props: [
        'list',
    ],
    components: {
        Item,
    }
}
</script>