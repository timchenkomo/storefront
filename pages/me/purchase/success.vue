<template>
  <div class="flex flex-col items-center">
    <h1 class="w-64 mb-4 text-xl text-center">
      Покупка завершена!
    </h1>

    <nuxt-link to="/me">
      Перейти к моим покупкам
    </nuxt-link>
    <nuxt-link to="/books">
      Перейти в библиотеку
    </nuxt-link>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'

@Component
class PurchaseSuccessPage extends Vue {
}

export default PurchaseSuccessPage
</script>
