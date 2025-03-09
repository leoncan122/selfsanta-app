import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'

// https://vite.dev/config/
export default defineConfig({
  base: '/',
  plugins: [react()],
  server: {
    host: true, // Esto permite que Vite acepte conexiones desde fuera del contenedor
    port: 5173
  }
})
