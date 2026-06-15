<script setup lang="ts">
import { ref, onMounted } from 'vue'

import { socket } from '../utils/socket'

// 1. 类型定义
interface Player {
  player_id: string
  nickname: string

}

interface PlayersListData {
  players: Player[]
  online_count: number
}

// 2. 响应式数据
const playerList = ref<Player[]>([])  // 存储玩家数组
const onlineCount = ref(0)

// 3. 方法/逻辑函数
const handlePlayersList = (data : PlayersListData) => {
  playerList.value = data.players
  onlineCount.value = data.online_count
}



// 4. 声明周期钩子
onMounted( ()=> {

  if(!socket.connected){
    socket.connect()
  }

  socket.on('players_list', handlePlayersList)
  socket.emit('get_players')

  }
)


</script>

<template>
  <div class="online-player-list">
    <span>当前在线人数 {{  }}</span>
    <div>
      <div class="table"
           v-for="player in playerList"
           :key="player.player_id">
        <span class="player-name">  {{ player.nickname }}     </span>
        <span class="player-id">    ID: {{ player.player_id }}</span>
      </div>
    </div>
  </div>
</template>

<style scoped>

</style>