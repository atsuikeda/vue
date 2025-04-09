<template>
  <div>
    <h1>DAKEN！</h1>
    <p>打鍵数: {{ dakenCount }}</p>
    <div>
      <p>打鍵してね</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const dakenCount = ref(0)

const isExtension = typeof chrome !== 'undefined' && chrome.storage

onMounted(() => {
  if (isExtension) {
    chrome.storage.local.get(['dakenCount'], (result) => {
      console.log('取得した値:', result)
      dakenCount.value = result.dakenCount || 0
    })

    chrome.storage.onChanged.addListener((changes) => {
      console.log('変更を検出:', changes)
      if (changes.dakenCount) {
        dakenCount.value = changes.dakenCount.newValue
      }
    })
  } else {
    const local = localStorage.getItem('dakenCount')
    dakenCount.value = local ? parseInt(local) : 0

    window.addEventListener('keydown', () => {
      dakenCount.value++
      localStorage.setItem('dakenCount', dakenCount.value)
      console.log('ローカルキー押した！カウント:', dakenCount.value)
    })
  }
})
</script>

<style scoped></style>
