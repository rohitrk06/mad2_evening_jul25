<template>
<div class="container-fluid">
    <div class="row justify-content-center">
        <div class="col-6">
            <h1 class="text-center">Register</h1>
            <form @submit.prevent="register">
                <div class="mb-3">
                    <label for="exampleInputEmail1" class="form-label">Username</label>
                    <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" v-model="username" @input="checkUserAvailabilty">
                    <div id="usernameHelp" class="form-text text-danger">{{ usernameError }}</div>
                </div>
                <div class="mb-3">
                    <label for="exampleInputEmail1" class="form-label">Email</label>
                    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" v-model="email">
                </div>
                <div class="row mb-3">
                    <div class="col-6">
                        <label for="exampleInputPassword1" class="form-label">Password</label>
                        <input type="password" class="form-control" id="exampleInputPassword1" v-model="password">
                        <div id="passwordHelp" class="form-text">{{ passwordCheck }}</div>
                    </div>
                    <div class="col-6">
                        <label for="exampleInputPassword1" class="form-label">Confirm Password</label>
                        <input type="password" class="form-control" id="exampleInputPassword1" v-model="confirm_password">
                        <div id="passwordHelp" class="form-text">{{ confirmPassword }}</div>
                    </div>
                </div>
                <button type="submit" class="btn btn-primary">Submit</button>
            </form>
        </div>
    </div>
</div>
</template>

<script setup>
import {ref, computed} from 'vue';
import {useRouter} from 'vue-router';

const router = useRouter();

const username = ref('');
const email = ref('');
const password = ref('');
const confirm_password = ref('');

const passwordCheck = computed(()=>{
    if (password.value.length < 6) {
        return 'Password must be at least 6 characters long';
    } else {
        return '';
    }
})

const confirmPassword = computed(() => {
    if (confirm_password.value !== password.value) {
        return 'Passwords do not match';
    } else {
        return '';
    }
})

const usernameError = ref('');
function checkUserAvailabilty(){
    fetch('http://127.0.0.1:5000/api/check_username', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({username: username.value})
    }).then((response)=>{
        if (response.ok){
            return response.json();
        }
    }).then(
        (data) =>{
            if (data.available){
                usernameError.value = 'Username is already taken';
            }
            else {
                usernameError.value = '';
            }
        }
    )
}


async function register(){
    if (username.value === '' || email.value === '' || password.value === '' || confirm_password.value === '') {
        alert('Please fill in all fields');
        return;
    }

    if (passwordCheck.value !== '' || confirmPassword.value !== '') {
        alert('Please fix the errors before submitting');
        return;
    }

    const user = {
        username: username.value,
        email: email.value,
        password: password.value
    }

    const response = await fetch("http://127.0.0.1:5000/api/register",{
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(user)
    });

    if (response.ok){
        const data = await response.json();
        alert(data.message);
        router.push('/login');
    }
    else {
        const errorData = await response.json();
        alert(`Registration failed: ${errorData.message}`);
    }
}
</script>