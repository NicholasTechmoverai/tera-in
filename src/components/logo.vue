<template>
  <div class="flex flex-col items-center justify-center ">
    <n-image
      width="120"
      :src="site.logo"
      alt="Logo"
      class="rounded-2xl shadow-md transition hover:scale-105 hover:shadow-lg duration-300 ease-in-out"
    >
      <template #error>
        <n-icon :size="120" color="lightgrey">
          <ImageOutlineIcon />
        </n-icon>
      </template>
    </n-image>

    <p class="mt-4 text-lg font-semibold text-gray-700 dark:text-gray-300">
      <NGradientText type="success">
        {{ site.name }}
      </NGradientText>
    </p>
  </div>
</template>

<script setup lang="ts">
import { ImageOutline as ImageOutlineIcon } from '@vicons/ionicons5'
import { site } from '../composables/index.js'


</script>
