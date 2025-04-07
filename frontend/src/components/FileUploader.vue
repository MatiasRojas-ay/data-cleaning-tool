<template>
  <div class="space-y-2">
    <label for="file-upload" class="block text-sm font-medium text-primary-900 flex items-center gap-1">
      <span class="material-icons text-primary-600">attach_file</span>
      Archivo de entrada
    </label>

    <input
      id="file-upload"
      type="file"
      @change="handleFileUpload"
      class="w-full text-sm text-gray-700 file:bg-primary-600 file:text-white file:rounded-lg file:px-4 file:py-2 file:border-0 file:cursor-pointer hover:file:bg-primary-700 border border-primary-200 rounded-lg bg-white/90 shadow-inner"
    />
  </div>
</template>

<script setup>
const emit = defineEmits(['update:file'])

function handleFileUpload(event) {
  const file = event.target.files[0]
  if (file) {
    emit('update:file', file)
  }
}
</script>
