<template>
  <div class="w-screen h-screen flex flex-col items-center justify-center bg-gray-900 text-white">
    <!-- 3D Canvas Background -->
    <canvas ref="canvasRef" class="absolute inset-0 -z-1"></canvas>

    <!-- Content -->
    <div class="relative z-10 text-center">
      <h1 class="text-5xl font-bold mb-4">Welcome to Tera-In</h1>
      <p class="text-lg mb-6 opacity-80">
        A modern landing page built with Vue 3, Naive UI, UnoCSS & Three.js 🚀
      </p>

      <n-button type="primary" size="large" @click="goNext">
        Get Started
      </n-button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";
import * as THREE from "three";
import { useMessage } from "naive-ui";

// refs
const canvasRef = ref<HTMLCanvasElement | null>(null);
const message = useMessage();

// navigation or CTA
const goNext = () => {
  message.success("You clicked Get Started!");
};

// 3D background setup
onMounted(() => {
  if (!canvasRef.value) return;

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(
    75,
    window.innerWidth / window.innerHeight,
    0.1,
    1000
  );
  const renderer = new THREE.WebGLRenderer({ canvas: canvasRef.value });
  renderer.setSize(window.innerWidth, window.innerHeight);

  // Add geometry (rotating cube)
  const geometry = new THREE.BoxGeometry();
  const material = new THREE.MeshBasicMaterial({ color: 0x00ffcc, wireframe: true });
  const cube = new THREE.Mesh(geometry, material);
  scene.add(cube);

  camera.position.z = 3;

  const animate = () => {
    requestAnimationFrame(animate);
    cube.rotation.x += 0.01;
    cube.rotation.y += 0.01;
    renderer.render(scene, camera);
  };

  animate();

  // Resize handling
  window.addEventListener("resize", () => {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
  });
});
</script>

<style>
/* optional if you want smoother visuals */
canvas {
  display: block;
}
</style>
