<script setup>

import { RouterLink, RouterView} from 'vue-router';
import { useMessageStore } from './stores/messageStore';
import { useAuthStore } from './stores/authStore';



const messageStore = useMessageStore();
const authStore = useAuthStore();

async function logout(){
    //Sent the fetch request to the backend to logout
    // Once you get response ok

    authStore.logout();
    messageStore.setMessage('You have been logged out successfully');
}

</script>

<template>
  <div class="container">
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container-fluid">
        <RouterLink class="navbar-brand" to="/" >Grocery Store</RouterLink>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item" v-if="!authStore.isAuthenticated">
              <RouterLink class="nav-link active" to="/login">Login</RouterLink>
            </li>
            <li class="nav-item" v-if="!authStore.isAuthenticated">
              <RouterLink class="nav-link active" to="/register">Register</RouterLink>
            </li>
            <li class="nav-item" v-if="authStore.isAuthenticated">
              <p class="nav-link">Welcome {{ authStore.getUserDetail.username }}</p>
            </li>
            <li class="nav-item" v-if="authStore.isAuthenticated">
              <button class="nav-link active" @click="logout">Logout</button>
            </li>
          </ul>
          <form class="d-flex" role="search">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search"/>
            <button class="btn btn-outline-success" type="submit">Search</button>
          </form>
        </div>
      </div>
    </nav>

    <div class="alert alert-success" v-if="messageStore.getMessage">
      {{ messageStore.getMessage }}
    </div>

    <RouterView/>

  </div>
</template>

