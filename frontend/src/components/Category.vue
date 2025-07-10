<script setup>
import Product from './Product.vue';

defineProps(['cat'])
</script>

<template>
    <div class="container-fluid">
        <div class="row">
            <div class="col-9">
                <p>
                    {{ cat.name }}
                </p>
            </div>
            <div class="col-3">
                <button class="btn btn-primary">Edit</button>
                <button class="btn btn-danger">Delete</button>
            </div>
        </div>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Price</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <Product v-for="product in cat.products" :key="product.id" :product="product"/>
            </tbody>
        </table>

    </div>
</template>