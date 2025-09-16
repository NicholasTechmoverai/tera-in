<template>
  <div class="scene-container">
    <canvas ref="canvasRef" class="three-canvas"></canvas>
    
    <div class="controls-panel">
      <h2>3D Text Controls</h2>
      
      <div class="control-group">
        <label for="rotationSpeed">Rotation Speed</label>
        <input 
          type="range" 
          id="rotationSpeed" 
          v-model="rotationSpeed" 
          min="0" 
          max="0.05" 
          step="0.001"
        >
        <span class="value">{{ rotationSpeed }}</span>
      </div>
      
      <div class="control-group">
        <label for="textColor">Text Color</label>
        <input 
          type="color" 
          id="textColor" 
          v-model="textColor"
        >
      </div>
      
      <div class="control-group">
        <label for="bevelSize">Bevel Size</label>
        <input 
          type="range" 
          id="bevelSize" 
          v-model="bevelSize" 
          min="0" 
          max="0.1" 
          step="0.01"
        >
        <span class="value">{{ bevelSize }}</span>
      </div>
      
      <div class="control-group">
        <label for="textContent">Text Content</label>
        <input 
          type="text" 
          id="textContent" 
          v-model="textContent"
        >
      </div>
    </div>
    
    <div v-if="loading" class="loading-overlay">
      <div class="spinner"></div>
      <p>Loading 3D text...</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch, onUnmounted } from 'vue';
import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { FontLoader } from 'three/addons/loaders/FontLoader.js';
import { TextGeometry } from 'three/addons/geometries/TextGeometry.js';

const canvasRef = ref(null);
const rotationSpeed = ref(0.01);
const textColor = ref('#00aaff');
const bevelSize = ref(0.03);
const textContent = ref('Hello World');
const loading = ref(true);

let scene, camera, renderer, controls, textMesh;
let animationId = null;

onMounted(() => {
  initScene();
  createText();
  setupEventListeners();
  animate();
});

onUnmounted(() => {
  if (animationId) {
    cancelAnimationFrame(animationId);
  }
  
  if (controls) {
    controls.dispose();
  }
  
  if (renderer) {
    renderer.dispose();
  }
});

function initScene() {
  // Create scene
  scene = new THREE.Scene();
  scene.background = new THREE.Color(0x0a0a20);
  
  // Create camera
  camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
  camera.position.z = 5;
  
  // Create renderer
  renderer = new THREE.WebGLRenderer({ 
    canvas: canvasRef.value, 
    antialias: true 
  });
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  
  // Add lights
  const ambientLight = new THREE.AmbientLight(0x404040, 0.6);
  scene.add(ambientLight);
  
  const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
  directionalLight.position.set(1, 1, 1);
  scene.add(directionalLight);
  
  const backLight = new THREE.DirectionalLight(0xffffff, 0.5);
  backLight.position.set(-1, -1, -1);
  scene.add(backLight);
  
  // Add controls
  controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;
  controls.dampingFactor = 0.05;
}

function createText() {
  // Remove existing text if any
  if (textMesh) {
    scene.remove(textMesh);
  }
  
  const loader = new FontLoader();
  
  // Load a font
  loader.load('https://cdn.jsdelivr.net/npm/three@0.132.2/examples/fonts/helvetiker_bold.typeface.json', (font) => {
    const geometry = new TextGeometry(textContent.value, {
      font: font,
      size: 0.8,
      height: 0.5,
      curveSegments: 12,
      bevelEnabled: true,
      bevelThickness: bevelSize.value,
      bevelSize: bevelSize.value,
      bevelOffset: 0,
      bevelSegments: 5
    });
    
    geometry.computeBoundingBox();
    geometry.center();
    
    const material = new THREE.MeshPhongMaterial({ 
      color: textColor.value,
      shininess: 100,
      specular: 0x222222
    });
    
    textMesh = new THREE.Mesh(geometry, material);
    scene.add(textMesh);
    
    loading.value = false;
  });
}

function setupEventListeners() {
  window.addEventListener('resize', onWindowResize);
}

function onWindowResize() {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
}

function animate() {
  animationId = requestAnimationFrame(animate);
  
  if (textMesh) {
    textMesh.rotation.x += rotationSpeed.value;
    textMesh.rotation.y += rotationSpeed.value;
  }
  
  controls.update();
  renderer.render(scene, camera);
}

// Watchers for reactive properties
watch(textColor, (newColor) => {
  if (textMesh) {
    textMesh.material.color.set(newColor);
  }
});

watch(bevelSize, () => {
  loading.value = true;
  createText();
});

watch(textContent, () => {
  loading.value = true;
  createText();
});
</script>

<style scoped>
.scene-container {
  position: relative;
  width: 100%;
  height: 100vh;
  overflow: hidden;
}

.three-canvas {
  display: block;
  width: 100%;
  height: 100%;
}

.controls-panel {
  position: absolute;
  top: 20px;
  right: 20px;
  background: rgba(0, 0, 0, 0.7);
  backdrop-filter: blur(10px);
  padding: 20px;
  border-radius: 12px;
  color: white;
  width: 300px;
  box-shadow: 0 5px 25px rgba(0, 0, 0, 0.5);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.controls-panel h2 {
  margin-top: 0;
  margin-bottom: 20px;
  font-size: 1.5rem;
  color: #00aaff;
  text-align: center;
}

.control-group {
  margin-bottom: 15px;
}

.control-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: 500;
  color: #cccccc;
}

.control-group input[type="range"] {
  width: 100%;
  margin-right: 10px;
}

.control-group input[type="color"] {
  width: 100%;
  height: 40px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.control-group input[type="text"] {
  width: 100%;
  padding: 8px;
  border-radius: 4px;
  border: 1px solid #444;
  background: rgba(255, 255, 255, 0.1);
  color: white;
}

.value {
  display: inline-block;
  width: 40px;
  text-align: right;
  color: #00aaff;
  font-weight: 600;
}

.loading-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: rgba(10, 10, 32, 0.8);
  color: white;
  z-index: 10;
}

.spinner {
  width: 50px;
  height: 50px;
  border: 5px solid rgba(255, 255, 255, 0.3);
  border-top: 5px solid #00aaff;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin-bottom: 20px;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

@media (max-width: 768px) {
  .controls-panel {
    top: 10px;
    right: 10px;
    left: 10px;
    width: auto;
  }
}
</style>