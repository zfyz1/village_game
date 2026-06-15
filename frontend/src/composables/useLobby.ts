import {onMounted, ref} from "vue";
import {useRouter} from 'vue-router'
import { socket } from '../utils/socket'



export function Lobby(){
    const router = useRouter()
    // 响应式变量nickname
    const current_nickname = ref('')
    const current_id = ref('')
    const players = ref([])
    const onlineCount = ref(0)

    const handleNickname = () => {
        const player_id = localStorage.getItem('player_id')
        const player_name = localStorage.getItem('player_nickname')

        if(!player_name || !player_id){
            router.push('/')
            return
        }

        current_nickname.value = player_name
        current_id.value = player_id
    }

    const handlePlayerList = (data:any) => {
        players.value = data.players
        onlineCount.value = data.online_count
    }

    onMounted(() => {
        handleNickname()
        if(!socket.connected){
            socket.connect()
        }
        socket.on('players_list',handlePlayerList)
        socket.emit('get_players')
        if (!socket.connected) {
            // 刷新了，连接断开，清除登录状态
            localStorage.removeItem('player_nickname')
            localStorage.removeItem('player_id')
            router.push('/')
            return
        }
    })

    return {
        current_nickname,
        current_id,
        players,
        onlineCount
    }
}