<template>
  <div
    :class="{'bg-blue-500': !inCart, 'bg-red-500': inCart, 'hover:bg-blue-600': !inCart, 'hover:bg-red-600': inCart}"
    @click="onClicked"
    class="py-2 px-4 rounded text-sm font-semibold text-center text-white cursor-pointer whitespace-no-wrap"
  >
    {{ text }}
    <span
      v-if="inCart"
      @click.stop="onRemoveClicked"
      class="float-right opacity-50 hover:opacity-100 pl-2"
    >
      ×
    </span>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'

@Component
class InCartButton extends Vue {
  // Is product already in a cart?
  @Prop({ default: false, type: Boolean }) inCart!: boolean;

  // Price of a product
  @Prop({ type: Number }) price!: number;

  private get text(): string {
    return this.inCart
      ? 'Оформить заказ'
      : 'В корзину ' + this.price + ' р.'
  }

  private onClicked() {
    this.$emit(this.inCart ? 'checkout' : 'add')
  }

  private onRemoveClicked() {
    this.$emit('remove')
  }
}

export default InCartButton
</script>
