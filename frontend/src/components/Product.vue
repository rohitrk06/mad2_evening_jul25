<script setup>
defineProps(['product'])
</script>

<template>
    <tr>
        <td>{{ product.name }}</td>
        <td>{{ product.price }}</td>
        <td>
            <button class="btn btn-primary">Edit</button>
            <button class="btn btn-danger">Delete</button>
        </td>
    </tr>
</template>