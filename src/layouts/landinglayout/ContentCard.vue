<template>
    <n-card title="Development in Progress" class="max-w-140 flex flex-col items-center p-6 space-y-4 rounded-2xl shadow-lg">
        <p class="font-bold text-2xl">This site is under development,we will hit back on you once done 😁</p>

        <div class="flex flex-row items-center mt-4 space-x-2">
            <n-input v-model:value="email" type="text" placeholder="your email(me@gmail.com)">
                <template #prefix>
                    <n-icon :component="Envelope" />
                </template>
            </n-input>
            <n-button type="primary" :loading="loading" @click="submitEmail">Notify Me</n-button>
        </div>
    </n-card>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { Envelope } from '@vicons/fa'


const email = ref<string>('')
const loading = ref(false)


const submitEmail = (): void => {
  loading.value = true
  console.log('📧 Email submitted:', email.value)

  setTimeout(() => {
    loading.value = false
  }, 1000)
}
</script>
