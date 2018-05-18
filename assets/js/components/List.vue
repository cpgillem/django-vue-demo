<template>
    <div>
        <a href="#" @click.prevent="$emit('select-list')"><h3>{{ list.name }}</h3></a>
    </div>
</template>

<script>
export default {
    props: ['list'],
}
</script>