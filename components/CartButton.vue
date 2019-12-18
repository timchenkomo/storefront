<template>
  <span class="relative">
    <!-- Main button -->
    <button @click="onClicked" class="py-2 px-4 bg-blue-500 text-white rounded">
      Корзина
      <span v-show="count > 0" class="px-2 bg-red-600 rounded-full inline-block">
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

    <!-- Cart is empty -->
    <div
      v-if="open && isEmpty"
      class="absolute right-0 bg-white rounded mt-2 w-64 shadow-md text-gray-900 py-4 px-4 text-center"
    >
      Корзина пуста
    </div>

    <!-- Cart -->
    <div
      v-if="open && !isEmpty"
      class="absolute right-0 flex flex-col bg-white rounded py-2 mt-2 w-64 shadow-md border-gray-300 text-gray-900"
    >
      <!-- Total price -->
      <div class="my-2 mx-4 flex">
        <span class="w-full">Итого:</span>
        <span>{{ totalPrice }}</span>&nbsp;₽
      </div>
      <hr class="my-2">

      <!-- List of items in cart -->
      <nuxt-link
        v-for="item in items"
        :key="item.id"
        :to="'/books/' + item.url"
        class="flex mx-4 my-2 items-baseline"
      >
        <span class="w-full">{{ item.title }}</span>
        <span v-if="item.type" class="px-2 text-gray-100 text-xs bg-gray-600 rounded-full">
          {{ item.type }}
        </span>
      </nuxt-link>
      <hr class="my-2">

      <!-- Put an order button -->
      <nuxt-link to="/cart" class="py-2 mx-2 text-white text-center rounded bg-blue-500 hover:bg-blue-600">
        Оформить заказ
      </nuxt-link>
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

  private get isEmpty(): boolean {
    return this.count === 0
  }

  private onClicked() {
    this.$emit('click')
  }

  private onCloseClicked() {
    this.$emit('close')
  }

  private get totalPrice(): number {
    return this.items.map(x => x.price).reduce((a, b) => a + b, 0)
  }
}

export default CartButton
</script>
