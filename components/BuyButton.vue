<template>
  <div class="rounded text-white bg-blue-500 py-2 text-sm font-semibold text-center inline-block px-4 cursor-pointer hover:bg-blue-600">
    Купить и скачать {{ price }}
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'

@Component
class BuyButton extends Vue {
  @Prop() readonly price!: string;
}

export default BuyButton
</script>
