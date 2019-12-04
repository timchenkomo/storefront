<template>
  <div>
    <input v-model.trim="value" @input="onValueChanged" class="p-2 border border-solid rounded w-full">
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'

@Component
class BookshelfFilter extends Vue {
  private value:string = '';

  private onValueChanged() {
    this.$emit('input', this.value)
  }
}

export default BookshelfFilter
</script>
