import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import UnoCSS from 'unocss/vite'

export default defineConfig({
  plugins: [vue(), UnoCSS()],
  server: {
    allowedHosts: ["tera-in.top", "www.tera-in.top"],
  },
  base: '/',
  build: {
    outDir: 'dist',
    assetsDir: 'static',
    emptyOutDir: true,
    rollupOptions: {
      output: {
        entryFileNames: `static/[name]-[hash].js`,
        chunkFileNames: `static/[name]-[hash].js`,
        assetFileNames: `static/[name]-[hash][extname]`,
      },
    },
  },

  // resolve: {
  //   alias: {
  //     '~': path.resolve(__dirname, '.'),
  //     '@': path.resolve(__dirname, 'src'),
  //   },
  // },
})
