import { createRouter, createWebHistory } from 'vue-router'

const routes = [
    {
        path:'/',
        name:'login',
        component:() => import('../views/LoginView.vue')
    },
    {
        path:'/lobby',
        name:'lobby',
        component:() => import('../views/LobbyView.vue')
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
    }
)

export default router