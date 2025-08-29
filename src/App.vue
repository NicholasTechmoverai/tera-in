
<template>
  <n-config-provider :theme="resolvedTheme">
    <n-loading-bar-provider>
      <n-message-provider>
        <n-notification-provider>
          <n-dialog-provider>
            <RouterView/>
          </n-dialog-provider>
        </n-notification-provider>
      </n-message-provider>
    </n-loading-bar-provider>
  </n-config-provider>
</template>


<script setup>
import { computed } from 'vue'
import { darkTheme } from 'naive-ui'
import LandingLayout from './layouts/landinglayout/index.vue'

// import { useUserStore } from './store/userStore'

// const userStore  = useUserStore()
const resolvedTheme = computed(() =>
  // userStore.theme === 'dark' ? darkTheme : null
  darkTheme
)
</script>
