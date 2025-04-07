<template>
  <form
    @submit.prevent="handleSubmit"
    class="bg-white/80 backdrop-blur p-8 rounded-2xl shadow-xl w-full max-w-3xl space-y-6 border border-primary-100"
  >
    <h2 class="text-3xl font-bold text-primary-800 flex items-center gap-2">
      <span class="material-icons text-primary-600">cleaning_services</span>
      Limpieza de Datos
    </h2>

    <FileUploader @update:file="file = $event" />
    <OperationSelector @update:operations="operations = $event" />
    <FormatSelector @update:format="format = $event" />

    <button
      type="submit"
      class="bg-primary-600 text-white font-semibold py-3 px-6 rounded-lg hover:bg-primary-700 disabled:opacity-50 w-full"
      :disabled="loading || !file"
    >
      {{ loading ? "Procesando..." : "Limpiar archivo" }}
    </button>

    <!-- Footer con el texto de derechos de autor -->
    <div class="text-center mt-4">
      <p class="text-sm text-gray-700">
        &#169; 2025 - <a href="https://matiasrojas.netlify.app/" target="_blank" class="text-primary-500 hover:text-primary-600">Matías Rojas</a>
      </p>
    </div>
  </form>
</template>

<script setup>
import { ref } from 'vue'
import FileUploader from './FileUploader.vue'
import OperationSelector from './OperationSelector.vue'
import FormatSelector from './FormatSelector.vue'
import axios from 'axios'

const file = ref(null)
const operations = ref([])
const format = ref('csv')
const loading = ref(false)

const handleSubmit = async () => {
  if (!file.value) return

  const formData = new FormData()
  formData.append('file', file.value)
  formData.append('format', format.value)
  operations.value.forEach(op => formData.append('operations', op))

  try {
    loading.value = true
    const response = await axios.post('/api/clean/', formData, {
      responseType: 'blob',
    })

    const blob = new Blob([response.data], { type: response.headers['content-type'] })
    const link = document.createElement('a')
    link.href = URL.createObjectURL(blob)
    link.download = `archivo_limpio.${format.value}`
    link.click()
  } catch (error) {
    alert('❌ Ocurrió un error al limpiar el archivo.')
    console.error(error)
  } finally {
    loading.value = false
  }
}
</script>
