import { createRouter, createWebHistory } from 'vue-router';
import LandingPage from '../views/LandingPage.vue';
import UVTracker from '../views/UVTracker.vue';
import Resources from '../views/ResourcesPage.vue';
import Blog from '../views/BlogPage.vue';

const routes = [
  { path: '/', name: 'Home', component: LandingPage },
  { path: '/uv-tracker', name: 'UV Tracker', component: UVTracker },
  { path: '/resources', name: 'Resources', component: Resources },
  { path: '/blog', name: 'Blog', component: Blog },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;