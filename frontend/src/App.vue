<script setup>
import CleanForm from './components/CleanForm.vue'
</script>

<template>
  <main class="min-h-screen bg-gradient-to-br from-indigo-50 via-white to-cyan-100 text-gray-800 font-sans flex items-center justify-center p-6">
    <div class="w-full max-w-3xl space-y-8">
      <!-- Header -->
      <div class="text-center">
        <h1 class="text-4xl font-extrabold text-primary-800 flex items-center justify-center gap-2">
          <span class="material-icons text-primary-600">auto_fix_high</span>
          Data Cleaner
        </h1>
        <p class="mt-2 text-lg text-gray-700">
          Subí tu archivo, seleccioná las operaciones de limpieza que necesitás y descargá una versión mejorada y lista para análisis.
        </p>
      </div>

      <!-- Formulario -->
      <CleanForm />
    </div>
  </main>
</template>