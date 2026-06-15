<script setup lang="ts">
import { Lobby } from "../composables/useLobby"

const { current_nickname, current_id, players, onlineCount } = Lobby()
</script>

<template>
  <div>
    <div>
      <h1>游戏大厅</h1>
      <p>欢迎回来，用户{{ current_nickname }}！你的唯一id是：{{ current_id }}</p>
    </div>

    <div>
      <span>当前在线人数 {{ onlineCount }}</span>
      <div>
        <div
          class="player-table"
          v-for="player in players"
          :key="player.player_id"
        >
          <span>{{ player.nickname }}</span>
          <span class="player-id">ID: {{ player.player_id }}</span>
        </div>
      </div>
    </div>
  </div>
</template>