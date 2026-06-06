import { defineStore } from 'pinia'

export const useKeyStore = defineStore('keyStore', {
  state: () => ({
    keydownCount: 0,
    isRightFoot: true,
  }),
  actions: {
    loadLocalStorage() {
      const local = localStorage.getItem('keydownCount')
      this.keydownCount = local ? parseInt(local) : 0
    },
    increment() {
      this.keydownCount++
      this.isRightFoot = !this.isRightFoot
      localStorage.setItem('keydownCount', this.keydownCount)
    },
  },
})
