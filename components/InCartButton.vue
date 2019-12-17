<template>
  <div
    :class="{'bg-blue-500': !inCart, 'bg-red-500': inCart, 'hover:bg-blue-600': !inCart, 'hover:bg-red-600': inCart}"
    class="py-2 px-4 rounded text-sm font-semibold text-center text-white cursor-pointer"
  >
    <div
      v-show="!inCart"
      @click="onAddedToCart"
    >
      В корзину {{ price }}р.
    </div>

    <div
      v-show="inCart"
      @click="onPlaceAnOrderClicked"
    >
      Оформить заказ
    </div>
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

  private onAddedToCart() {
    this.$emit('addToCart')
  }

  private onPlaceAnOrderClicked() {
    this.$emit('placeAnOrder')
  }
}

export default InCartButton
</script>
