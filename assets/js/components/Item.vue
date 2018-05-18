<template>
    <div>
        <div v-if="mode === 'show'">
            {{ item.title }}
            <button @click="edit()">Edit</button>
            <button @click="$emit('delete-item', item)">Delete</button>
        </div>

        <div v-else-if="mode === 'edit'">
            <input type="text" v-model="itemData.title"/>
            <button @click="update()">Update</button>
        </div>
    </div>
</template>

<script>
export default {
    props: [
        'item',
    ],

    data() {
        return {
            // Store the item's data in state for modification.
            itemData: this.item,

            // Set a variable for switching between edit and show mode.
            mode: 'show',
        };
    },

    methods: {
        edit() {
            this.mode = 'edit';
        }, 

        update() {
            this.$emit('update-item', this.itemData);
            this.mode = 'show';
        },
    }
}
</script>