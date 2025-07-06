<template>
<div class="container-fluid">
    <div class="row justify-content-center">
        <div class="col-6">
            <h1 class="text-center">Login</h1>
            <form v-on:submit.prevent="login">
                <div class="mb-3">
                    <label for="exampleInputEmail1" class="form-label">Username</label>
                    <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" v-model="username">
                </div>
                <div class="mb-3">
                    <label for="exampleInputPassword1" class="form-label">Password</label>
                    <input type="password" class="form-control" id="exampleInputPassword1" v-model="password" @input = "validatePassword">
                    <div id="passwordHelp" class="form-text">{{ passwordError  }}</div>
                </div>
                <button type="submit" class="btn btn-primary">Submit</button>
            </form>
        </div>
    </div>
</div>
</template>

<script setup>
import {ref} from 'vue';

const username = ref('');
const password = ref('');


const passwordError = ref('');

const validatePassword = () => {
    if (password.value.length < 6){
        passwordError.value = 'Password must be at least 6 characters long';
        return false;
    } else {
        passwordError.value = '';
        return true;
    }
}



async function login(){
    if (!validatePassword()){
        alert('Invalid password length')
        return;
    }

    if (username.value === '' || password.value === '') {
        alert('Please fill in all fields');
        return;
    }

    const user = {
        username: username.value,
        password: password.value
    }

    const response = await fetch("http://127.0.0.1:5000/api/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(user)
    });

    console.log(response);

    if(!response.ok){
        const errorData = await response.json();
        console.error(errorData)
        alert(`Login failed: ${errorData.message}`);
        return;
    }
    else{
        const data = await response.json();
        console.log(data);

        localStorage.setItem('auth_token',data.data.auth_token);
        alert(data.message)
        return;
        // localStorage.removeItem('token')
        
    }

}

</script>