<template>
  <div class="eho-container">
    <h1>伝えたいっ...</h1>
    <p class="eho-count">{{ store.keydownCount }}えっほっほ</p>
    <div class="eho-image">
      <img :src="store.isRightFoot ? rightImg : leftImg" alt="" />
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useKeyStore } from '@/stores/useKeyStore'

import rightImg from '@/assets/right.jpg'
import leftImg from '@/assets/left.jpg'

const store = useKeyStore()

const handleKeydown = () => {
  store.increment()
}

onMounted(() => {
  store.loadLocalStorage()
  window.addEventListener('keydown', handleKeydown)
})
</script>

<style scoped>
.eho-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 20px;
  min-height: 100vh;
  background: linear-gradient(to bottom, #fceabb, #f8b500);
  font-family: 'Zen Maru Gothic', sans-serif;
  text-align: center;
}

h1 {
  font-size: 2.8rem;
  color: #5d4037;
  margin-bottom: 40px;
  text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.1);
}

.eho-count {
  font-size: 3rem;
  font-weight: bold;
  color: #d84315;
  background: #fff3e0;
  padding: 20px 40px;
  border-radius: 20px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
  margin-bottom: 40px;
  transition: transform 0.1s ease-in-out;
}

.eho-image img {
  max-width: 100%;
  border-radius: 20px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}
</style>
