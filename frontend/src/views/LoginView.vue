<script setup lang="ts">
import {useAuth} from "../composables/useAuth.ts";
const {nickname, isLoading, handleLogin} = useAuth()

</script>

<template>
  <div class="main-container">
    <div class="logo">
      <h1>  村长游戏（仅游客登录）  </h1>
    </div>

    <div>
      <input class="input"
             v-model="nickname"
             :disabled="isLoading"
             placeholder="请输入一个名字作为游玩昵称"
      >
    </div>

    <div>
      <button class="confirm-button"
              :disabled="isLoading"
              @click="handleLogin"
      > {{ isLoading ? '正在连接服务器...' : '确认昵称，进入游戏大厅' }} </button>
    </div>


  </div>
</template>

<style scoped>

</style>