<template>
  <div>
    <h1>伝えたい</h1>
    <p>{{ keydownCount }}えっほ</p>
    <div>
      <img :src="isRightFoot ? rightImg : leftImg" alt="" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const keydownCount = ref(0)
const isRightFoot = ref(true)

const rightImg = '/right.jpg'
const leftImg = '/left.jpg'

const handleKeydown = () => {
  keydownCount.value++
  localStorage.setItem('keydownCount', keydownCount.value)

  isRightFoot.value = !isRightFoot.value
}

onMounted(() => {
  window.addEventListener('keydown', handleKeydown)

  const local = localStorage.getItem('keydownCount')
  keydownCount.value = local ? parseInt(local) : 0
})
</script>

<style scoped></style>
