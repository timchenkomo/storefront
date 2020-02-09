<template>
  <div class="flex flex-col items-center">
    <h1 class="w-64 mb-4 text-xl text-center">
      Ошибка при совершении покупки!
    </h1>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'

@Component
class PurchaseFailPage extends Vue {
}

export default PurchaseFailPage
</script>
