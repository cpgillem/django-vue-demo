<template>
    <div>
        <h3>{{ list.name }}</h3>
    </div>
</template>

<script>
import auth from '../auth';

export default {
    props: ['list'],
}
</script>