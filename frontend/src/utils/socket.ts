import { io, Socket } from 'socket.io-client'

// 后端 Flask 服务的实际地址和端口
const SOCKET_URL = 'http://localhost:5000'

export const socket: Socket = io(SOCKET_URL, {
  autoConnect: false, // 初始不自动连接，在登录页手动触发
  transports: ['websocket', 'polling'], // 强制优先使用 WebSocket，避免降级为长轮询
  reconnection: true,
  reconnectionAttempts: 5,
})