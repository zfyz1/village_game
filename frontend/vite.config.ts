import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],   // 开启 Vue 支持
  server:{
    port: 5173,  // 开发服务器端口
    proxy:{
      '/api' : 'http://localhost:3000'  // 后端服务器api
    }
  }
})
