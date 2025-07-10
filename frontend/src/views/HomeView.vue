<script setup>
import Category from '@/components/Category.vue';


const categories = [
  {
    'id':1,
    'name':'Fruits',
    'products':[
      {'id':1, 'name':'Apple', 'price':1.2, 'image':'apple.jpg'},
      {'id':2, 'name':'Banana', 'price':0.5, 'image':'banana.jpg'},
      {'id':3, 'name':'Orange', 'price':0.8, 'image':'orange.jpg'}
    ]
  },
  {
    'id':2,
    'name':'Vegetables',
    'products':[
      {'id':4, 'name':'Carrot', 'price':0.6, 'image':'carrot.jpg'},
      {'id':5, 'name':'Broccoli', 'price':1.0, 'image':'broccoli.jpg'},
      {'id':6, 'name':'Spinach', 'price':0.7, 'image':'spinach.jpg'}
    ]
  },
  {
    'id':3,
    'name':'Dairy',
    'products':[
      {'id':7, 'name':'Milk', 'price':1.5, 'image':'milk.jpg'},
      {'id':8, 'name':'Cheese', 'price':2.0, 'image':'cheese.jpg'},
      {'id':9, 'name':'Yogurt', 'price':1.2, 'image':'yogurt.jpg'}
    ]
  }
]
</script>

<template>
<Category v-for="category in categories" :cat="category"/>
</template>
