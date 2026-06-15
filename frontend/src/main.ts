import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from "./router";

// 创建vue应用
const app = createApp(App)

// 注册路由
app.use(router)
// 挂载到 #app
app.mount('#app')
