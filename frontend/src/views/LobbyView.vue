<script setup lang="ts">
import {ref} from "vue";

import { Lobby } from "../composables/useLobby"
import OnlinePlayerList from "../components/OnlinePlayerList.vue";


const { current_nickname, current_id} = Lobby()

const showPlayerListDialog = ref(false)
</script>

<template>
  <div>
    <div>
      <h1>游戏大厅</h1>
      <p>欢迎回来，用户{{ current_nickname }}！你的唯一id是：{{ current_id }}</p>
    </div>

    <div>
      <button @click="showPlayerListDialog = true"> 显示在线玩家 </button>
    </div>

    <!-- 在线列表弹窗 -->
    <div v-if="showPlayerListDialog" class="Dialog">
      <div>
        <h3> 在线玩家 </h3>
        <button @click="showPlayerListDialog = false"> 关闭 </button>
      </div>
      <div>
        <OnlinePlayerList/>
      </div>
    </div>
  </div>

</template>