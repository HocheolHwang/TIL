<template>
  <div>
    <h1>리뷰 검색</h1>
    <div class="search-container">
      <input v-model="searchQuery" placeholder="검색어를 입력하세요" class="search-input" />
      <button @click="searchReviews" class="search-button">검색</button>
    </div>

    <div v-if="movies.length > 0">
      <h2>검색 결과</h2>
      <div v-for="video in movies" :key="video.id.videoId" class="movie-container">
        <div class="video-container">
          <div class="video-info">
            <iframe
              width="100%"
              height="200"
              :src="'https://www.youtube.com/embed/' + video.id.videoId"
              frameborder="0"
              allowfullscreen
              class="video-frame"
            ></iframe>
          </div>
          <div class="video-info">
            <div class="video-title">{{ video.snippet.title }}</div>
            <div class="video-description">{{ video.snippet.description }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const movies = ref([])
const apiKey = 'AIzaSyBxYQzCKvA_h_HW66UT-vw1nBv9LmZKXKo'
const apiUrl = 'https://www.googleapis.com/youtube/v3/search'
const searchQuery = ref('')

const searchReviews = async () => {
  try {
    const response = await axios.get(apiUrl, {
      params: {
        key: apiKey,
        part: 'snippet',
        type: 'video',
        q: searchQuery.value,
      },
    })
    movies.value = response.data.items
  } catch (error) {
    console.error('Error:', error.message)
  }
}
</script>

<style scoped>
.search-container {
  display: flex;
  margin-bottom: 20px;
}

.search-input {
  flex: 1;
  padding: 8px;
  margin-right: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.search-button {
  padding: 8px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.movie-container {
  border: 1px solid #ccc;
  margin-bottom: 20px;
  padding: 10px;
}

.video-container {
  display: flex;
  gap: 20px; /* Add some spacing between the video and the info */
}

.video-info {
  flex: 1;
}

.video-frame {
  width: 100%;
}

.video-title {
  font-size: 18px;
  font-weight: bold;
  margin-top: 10px;
}

.video-description {
  font-size: 14px;
  font-weight: lighter;
  margin-top: 5px;
}
</style>