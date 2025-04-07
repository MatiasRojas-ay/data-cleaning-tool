<template>
  <div class="space-y-2">
    <label for="format" class="block text-sm font-medium text-primary-900 flex items-center gap-1">
      <span class="material-icons text-primary-600">download</span>
      Formato de exportación
    </label>

    <select
      id="format"
      v-model="selected"
      @change="emit('update:format', selected)"
      class="w-full border border-primary-200 bg-white/90 text-sm rounded-lg px-4 py-2 shadow-inner focus:outline-none focus:ring-2 focus:ring-primary-500"
    >
      <option v-for="option in formats" :key="option" :value="option">
        {{ option.toUpperCase() }}
      </option>
    </select>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const emit = defineEmits(['update:format'])

const formats = ["csv", "tsv", "xlsx", "json", "parquet"]
const selected = ref("csv")
</script>
