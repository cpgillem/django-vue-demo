<template>
    <div>
        <div v-if="mode === 'show'">
            <a href="#" @click.prevent="$emit('select-list')"><h3>{{ list.name }}</h3></a>
            <button @click="edit()">Edit</button>
            <button @click="$emit('delete-list', list)">Delete</button>
        </div>

        <div v-if="mode === 'edit'">
            <input type="text" v-model="listData.name"/>
            <button @click="update()">Update</button>
        </div>
    </div>
</template>

<script>
export default {
    props: [
        "list"
    ],

    data() {
        return {
            // Store the list object in state for modification.
            listData: this.list,

            // Whether the list component is in edit mode or not.
            mode: 'show',
        }
    },

    methods: {
        // Switches to edit mode.
        edit() {
            this.mode = 'edit';
        },
        
        // Emit an update event and switch back to show.
        update() {
            this.$emit('update-list', this.listData)
            this.mode = 'show';
        }
    }
};
</script>