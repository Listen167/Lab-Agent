import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', redirect: '/manager/home' },
    {
      path: '/manager', // 所有/manager开头的地址都是使用Layout这个框架，并且默认先跳到首页
      name: 'Layout',
      component: () => import('@/layouts/layout.vue'),
      children: [
        { path: 'home', name: 'Home', component: () => import('@/views/home.vue') },
        { path: 'lab', name: 'lab', component: () => import('@/views/Lab.vue') },
        { path: 'equ', name: 'equ', component: () => import('@/views/Equ.vue') },
        { path: 'user', name: 'user', component: () => import('@/views/User.vue') }
      ]
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('@/views/Login.vue')
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('@/views/Register.vue')
    }
  ]
})

export default router

// App.vue
//  └── <router-view />          ← 第一层路由出口
//        └── Layout.vue         ← 父路由组件
//              ├── 顶栏
//              ├── 侧边栏
//              └── <router-view />   ← 第二层路由出口
//                    └── Home.vue / User.vue / Lab.vue ...  ← 子路由组件
