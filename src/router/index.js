import { createRouter, createWebHistory } from 'vue-router';
import Login from '../components/login.vue';
import Checkup from '../components/checkup.vue';
import ThreeDayWeather from '../components/ThreeDayWeather.vue';
import HourlyWeather from '../components/HourlyWeather.vue';
import CurrentWeather from '../components/CurrentWeather.vue';

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/checkup',
    name: 'Checkup',
    component: Checkup
  },
  {
    path: '/',
    name: 'Home',
    component: Login,
  },
  {
  path: '/three-days',
    name: 'ThreeDays',
    component: ThreeDayWeather,
  },
  {
    path: '/hours',
    name: 'Hours',
    component: HourlyWeather,
  },
  {
    path: '/now',
    name: 'Now',
    component: CurrentWeather,
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
});


export default router;