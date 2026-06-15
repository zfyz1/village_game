import {ref} from "vue";

export function useAuth(){
    const nickname = ref('')

    // 响应式
    const loading = ref<boolean>(false)
    // 错误信息
    const error = ref<string | null>(null)

    const handleLogin = () => {
        // 1 校验昵称
        const trimmedNickname = nickname.value.trim()
        if( !trimmedNickname){
            error.value = ' 请输入昵称 '
            alert('请输入昵称')
            return
        }

        // 2 登录
        loading.value = true
        error.value = null

        try{
            loacalStorage.setItem('nickname', trimmedNickname)
            router
        }
    }

}