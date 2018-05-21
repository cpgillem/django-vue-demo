<template>
    <div>
        <div v-if="mode === 'show'" v-bind:class="{ 'selected': this.selected }" class="clearfix list-item">
            <div class="float-left">
                <a href="#" @click.prevent="$emit('select-list')"><h3>{{ list.name }}</h3></a>
            </div>
            <div class="button-group float-right">
                <button class="button" @click="edit()">Edit</button>
                <button class="button alert" @click="$emit('delete-list', list)">Delete</button>
            </div>
        </div>

        <div v-if="mode === 'edit'" v-bind:class="{ 'selected': this.selected }" class="list-item">
            <div class="input-group">
                <input class="input-group-field" type="text" v-model="listData.name"/>
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
        "list",
        "selected",
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