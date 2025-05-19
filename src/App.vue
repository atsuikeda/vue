<template>
  <div class="eho-container">
    <h1>伝えなきゃ</h1>
    <p class="eho-count">{{ store.keydownCount }}えっほ</p>
    <div class="eho-image">
      <img :src="store.isRightFoot ? rightImg : leftImg" alt="" />
    </div>

    <div>
      <p v-if="trivia">{{ trivia }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useKeyStore } from '@/stores/useKeyStore'

import { fetchTrivia } from '@/api/fetchTrivia'
import { translateWithDeepl } from '@/api/translateWithDeepl'

import rightImg from '@/assets/right.jpg'
import leftImg from '@/assets/left.jpg'

const store = useKeyStore()

const trivia = ref('')

const handleKeydown = async () => {
  store.increment()

  if (store.keydownCount % 10 === 0) {
    const rawTrivia = await fetchTrivia()

    if (/[a-zA-Z]/.test(rawTrivia)) {
      trivia.value = await translateWithDeepl(rawTrivia)
    } else {
      trivia.value = rawTrivia
    }
  }
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
  min-height: 100vh;
  background: linear-gradient(to bottom, #e6f4ea, #b2dfdb);
  font-family: 'Zen Maru Gothic', sans-serif;
  text-align: center;
}

h1 {
  font-size: 2.8rem;
  color: #2e7d32; /* 深めのグリーン */
  margin-bottom: 40px;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
}

.eho-count {
  font-size: 3rem;
  font-weight: bold;
  color: #388e3c; /* 明るめの緑 */
  background: #e8f5e9; /* 薄いグリーン背景 */
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
