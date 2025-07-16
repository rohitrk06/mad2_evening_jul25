<script setup>

import { useRoute } from 'vue-router';
import { onMounted, ref } from 'vue';
import { useAuthStore } from '@/stores/authStore';

const route = useRoute();
const authStore = useAuthStore();
const categoryName = ref('');
const categoryDescription = ref('');

onMounted(()=>{
    console.log(route.params.id)
    fetch(`http://127.0.0.1:5000/api/categories/${route.params.id}`,{
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authentication-Token': authStore.getAuthToken
        }
    }).then((response)=>{
        if (response.ok){
            return response.json();
        }
    }).then((data)=>{
        console.log(data);
        categoryName.value = data.name;
        categoryDescription.value = data.description;
    }).catch((error)=>{
        console.error('Error fetching category:', error);
    })
})

</script>

<template>
<div>
    <div>
        <label>Category Name</label>
        <input type="text" v-model="categoryName"/>
    </div>
    <div>
        <label>Category Description</label>
        <textarea></textarea>
    </div>
</div>
</template>