import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MovieDetailView from '../views/MovieDetailView.vue'
import MovieListView from '../views/MovieListView.vue'
import RecommendedView from '../views/RecommendedView.vue'
import ReviewSearchView from '../views/ReviewSearchView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      // 메인 페이지
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      // 영화 상세 정보 페이지
      path: '/:movieId',
      name: 'movieDetail',
      component: MovieDetailView
    },
    {
      // 전체 영화 목록 페이지
      path: '/movies',
      name: 'movieList',
      component: MovieListView
    },
    {
      // 날씨 기반 영화 추천 페이지
      path: '/recommended',
      name: 'recommended',
      component: RecommendedView
    },
    {
      // 유튜브 검색 및 출력 페이지
      path: '/review-search',
      name: 'reviewSearch',
      component: ReviewSearchView
    },
  ]
})

export default router
