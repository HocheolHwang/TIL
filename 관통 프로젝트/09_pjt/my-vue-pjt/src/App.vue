<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <nav>
    <RouterLink :to="{ name: 'home' }" class="logo">Home</RouterLink>
    <div class="nav-links">
      <RouterLink :to="{ name: 'movieList' }">최고평점 영화조회</RouterLink>
      <RouterLink :to="{ name: 'reviewSearch' }">리뷰검색</RouterLink>
      <RouterLink :to="{ name: 'recommended' }">영화추천</RouterLink>
    </div>
  </nav>

  <RouterView />
</template>

<style scoped>
nav {
  background-color: #333;
  color: white;
  padding: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
  text-decoration: none; /* 로고에 밑줄 제거 */
  color: white; /* 로고 색상 */
}

.nav-links {
  display: flex;
  gap: 1rem;
}

nav a {
  color: white;
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 0.25rem;
  transition: background-color 0.3s ease;
}

nav a:hover {
  background-color: #555;
}

nav a.router-link-exact-active {
  background-color: #555;
}
</style>
