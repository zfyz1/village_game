<script setup lang="ts">
import { Lobby } from "../composables/useLobby"
import OnlinePlayerList from "../components/OnlinePlayerList.vue";


const { current_nickname, current_id} = Lobby()
</script>

<template>
  <div>
    <div>
      <h1>游戏大厅</h1>
      <p>欢迎回来，用户{{ current_nickname }}！你的唯一id是：{{ current_id }}</p>
    </div>

    <div class="player-list-container">
      <OnlinePlayerList />
    </div>
  </div>
</template>