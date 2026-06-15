import {onMounted, onUnmounted, ref} from 'vue'
import { useRouter } from 'vue-router'
import {socket} from "../utils/socket.ts";

export function useAuth(){
    // 初始话路由实例
    const router = useRouter()
    // 响应式状态
    const nickname = ref('')
    const isLoading = ref(false)

    const handleConnect = () =>{
        console.log('已连接至服务器')
    }

    const handleConnectError = () => {
        isLoading.value = false
        alert('无法连接到游戏服务器，请检查后端是否启动或网络是否正常！')
    }

    const handleLoginSuccess = (data: {player_id: string ; nickname: string}) => {
        isLoading.value = false
        // 1 保存玩家信息至本地存储
        localStorage.setItem('player_nickname',data.nickname)
        localStorage.setItem('player_id',data.player_id)

        // 2 路由跳转
        router.push({path:'/lobby'})
    }

    const handleLoginError = (data: { message: string }) => {
    isLoading.value = false
    alert(data.message || '登录失败')
    }

    const handleLogin = () =>{
        const name = nickname.value.trim()
        // 名称校验
        if(!name){
            alert('请输入昵称')
            return
        }
        // 连接服务器
        if(!socket.connected){
            socket.connect()
        }

        // 发送登录事件
        socket.emit('login',{nickname:name})
    }

     onMounted(() => {
        // 注册 Socket 监听
        socket.on('connect', handleConnect)
        socket.on('connect_error', handleConnectError)
        socket.on('login_success', handleLoginSuccess)
        socket.on('login_error', handleLoginError)
    })

    onUnmounted(() => {
        socket.off('connect', handleConnect)
        socket.off('connect_error', handleConnectError)
        socket.off('login_success', handleLoginSuccess)
        socket.off('login_error', handleLoginError)
    })

    return{
        nickname,
        isLoading,
        handleLogin
    }

}