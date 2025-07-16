import { defineStore } from "pinia";
import { ref, computed } from "vue";

export const useMessageStore = defineStore(
    "messageStore",
    () => {
        const message = ref("");

        const getMessage = computed(() => message.value);

        function setMessage(newMessage) {
            message.value = newMessage;
            setTimeout(() =>{
                message.value = "";
            },5000);
        }
        return {getMessage, setMessage};
    }
)