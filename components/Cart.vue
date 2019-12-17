<template>
  <span class="relative">
    <!-- Main button -->
    <button @click="onClicked" class="py-2 px-4 bg-blue-500 text-white rounded">
      Корзина

      <span v-show="count > 0" class="px-2 bg-red-600 rounded-lg">
        {{ count }}
      </span>
    </button>

    <!-- Overlay -->
    <button
      v-if="open"
      @click="onCloseClicked"
      tabindex="-1"
      class="fixed inset-0 w-full h-full cursor-default"
    />

    <!-- Menu items -->
    <div
      v-if="open"
      class="absolute right-0 flex flex-col bg-white rounded py-2 mt-2 w-64 shadow-md border-gray-300 text-gray-900"
    >
      <!-- List of items in cart -->
      <nuxt-link
        v-for="item in items"
        :key="item.product.id"
        :to="'/books/' + item.product.id"
        class="px-4 py-2 hover:bg-blue-500 hover:text-white"
      >
        {{ item.product.title }}
      </nuxt-link>

      <!-- Delimiter -->
      <hr class="my-2">

      <!-- Order -->
      <button class="py-2 mx-2 bg-blue-500 text-white rounded">
        Оформить заказ
      </button>
    </div>
  </span>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
import { CartItem } from '../lib/cart'

@Component
class CartButton extends Vue {
  @Prop({ default: false }) readonly open!: boolean;
  @Prop({ default: [] }) readonly items!: CartItem[];

  private get count(): number {
    return this.items.length
  }

  private onClicked() {
    this.$emit('click')
  }

  private onCloseClicked() {
    this.$emit('close')
  }
}

export default CartButton
</script>
