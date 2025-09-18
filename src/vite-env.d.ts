/// <reference types="vite/client" />

// Allow importing Vue SFCs
declare module "*.vue" {
  import type { DefineComponent } from "vue";
  const component: DefineComponent<{}, {}, any>;
  export default component;
}

// Allow importing local JS modules
declare module "*.js";

// Fallback for Three.js if typings not found
declare module "three";
