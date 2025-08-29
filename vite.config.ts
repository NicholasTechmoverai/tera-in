import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import UnoCSS from 'unocss/vite'
  
export default defineConfig({
  plugins: [vue(), UnoCSS()],
  server: {
    allowedHosts: ["tera-in.top", "www.tera-in.top"],
  },
})
