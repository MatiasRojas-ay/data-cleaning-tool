<template>
  <div class="space-y-2">
    <label class="block text-sm font-medium text-primary-900 flex items-center gap-1">
      <span class="material-icons text-primary-600">tune</span>
      Operaciones de limpieza
    </label>

    <div class="grid grid-cols-2 gap-2 max-h-48 overflow-y-auto bg-white/70 backdrop-blur-sm rounded-xl p-3 border border-primary-100 shadow-inner">
      <label
        v-for="op in operations"
        :key="op"
        class="flex items-center gap-2 text-sm text-primary-800 hover:bg-primary-50 px-2 py-1 rounded transition-all"
      >
        <input
          type="checkbox"
          :value="op"
          v-model="selected"
          class="accent-primary-600 rounded focus:ring-primary-400"
        />
        <span>{{ op.replaceAll('_', ' ') }}</span>
      </label>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
const emit = defineEmits(['update:operations'])

const operations = [
  "drop_empty_columns",
  "remove_empty_rows",
  "drop_duplicate_rows",
  "remove_constant_cols",
  "remove_high_null_cols",
  "drop_outliers",
  "fill_missing_values",
  "strip_whitespace",
  "remove_special_chars",
  "remove_numeric_rows",
  "remove_stopwords",
  "standardize_columns",
  "convert_dtypes",
  "parse_dates",
  "round_numeric",
  "normalize_text",
]

const selected = ref([])

watch(selected, (newVal) => {
  emit('update:operations', newVal)
})
</script>
