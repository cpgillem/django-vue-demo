<template>
    <div>
        <div v-if="mode === 'show'">
            {{ item.title }}
            <div class="button-group">
                <button class="button" @click="edit()">Edit</button>
                <button class="button alert" @click="$emit('delete-item', item)">Delete</button>
            </div>
        </div>

        <div v-else-if="mode === 'edit'">
            <div class="input-group">
                <input class="input-group-field" type="text" v-model="itemData.title"/>
                <div class="input-group-button">
                    <button class="button" @click="update()">Update</button>
                </div>
            </div>
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