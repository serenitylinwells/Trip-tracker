<script setup>
import { ref } from 'vue';
import { RouterLink, RouterView } from 'vue-router'
import checkup from './components/checkup.vue';
import login from './components/login.vue'

const showLogin = ref(true);

const handleLoginStatus = (status) => {
  if (status === "SUCCEED") {
    showLogin.value = false;
  }
}

</script>

<template>
  <div>
    <!-- <login v-if="showLogin" @login-status="handleLoginStatus"></login> -->
    <!-- <checkup v-else></checkup> -->
    <RouterView/>
  </div>
  <!-- <checkup/> -->
</template>

<style scoped>

</style>
