import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

export default defineConfig({
  base: './',
  plugins: [vue(), vueDevTools()],
  build: {
    outDir: 'dist',
    rollupOptions: {
      input: {
        index: fileURLToPath(new URL('./src/index.html', import.meta.url)),
        background: fileURLToPath(new URL('./src/background.js', import.meta.url)),
        content: fileURLToPath(new URL('./src/content.js', import.meta.url)),
      },
      output: {
        entryFileNames: 'assets/[name].js',
      },
    },
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
})
