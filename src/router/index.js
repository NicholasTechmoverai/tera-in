import { createRouter, createWebHistory } from 'vue-router'

import LandingPage from '../layouts/landinglayout/index.vue'

const routes = [
  {
    path: '/',
    name: 'Landing',
    component: LandingPage,
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router
