import {defineStore} from 'pinia';
import {ref, computed} from 'vue';

export const useAuthStore = defineStore('authStore', () => {
    const auth_token = ref(localStorage.getItem('auth_token') || '');
    const user_detail = ref(JSON.parse(localStorage.getItem('user_detail')) || {username: '', email: ''});


    const isAuthenticated = computed(()=> auth_token.value !== '');
    const getAuthToken = computed(() => auth_token.value);
    const getUserDetail = computed(() => user_detail.value);

    function setAuthToken(token) {
        localStorage.setItem('auth_token', token);
        auth_token.value = token;
    }

    function setUserDetails(user_details){
        localStorage.setItem('user_detail', JSON.stringify(user_details));
        user_detail.value = user_details;
    }

    function logout(){
        localStorage.removeItem('auth_token');
        localStorage.removeItem('user_detail');
        auth_token.value = '';
        user_detail.value = {username: '', email: ''};
    }

    return { isAuthenticated, getAuthToken, getUserDetail, setAuthToken, setUserDetails, logout };
})