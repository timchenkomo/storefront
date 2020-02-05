<template>
  <nav-menu
    ref="navmenu"
    title="Корзина"
    link="/cart"
    fill="true"
  >
    <!-- Main button -->
    <template v-slot:activator>
      <!-- wide screen button -->
      <span>Корзина</span>
      <span v-show="count > 0" class="bg-blue-800 rounded-full inline-block w-5">
        {{ count }}
      </span>
    </template>

    <!-- Cart is empty -->
    <div
      v-if="isEmpty"
      class="text-center w-32 my-2 mx-4"
    >
      Корзина пуста
    </div>

    <!-- Cart -->
    <div
      v-if="!isEmpty"
      class="flex flex-col whitespace-no-wrap"
    >
      <!-- Total price -->
      <div
        v-if="!isEmpty"
        class="my-2 mx-4 flex items-baseline"
      >
        <span class="w-full mx-2">Итого:</span>
        <span class="text-2xl">{{ totalPrice }}</span>&nbsp;₽
      </div>
      <hr class="my-2">

      <!-- List of items in cart -->
      <nuxt-link
        v-for="item in items"
        :key="item.id"
        :to="'/books/' + item.url"
        class="flex mx-2 my-1 px-2 py-2 items-baseline hover:bg-gray-200 rounded"
      >
        <span class="w-full">{{ item.title }}</span>
        <span v-if="item.type" class="ml-4 px-2 text-gray-100 text-xs bg-gray-500 rounded-full">
          {{ item.type }}
        </span>
      </nuxt-link>
      <hr class="my-2">

      <!-- Put an order button -->
      <button
        @click="onCheckoutClicked"
        class="py-2 mx-2 text-white text-center rounded bg-blue-500 hover:bg-blue-600"
      >
        Оформить заказ
      </button>
    </div>
  </nav-menu>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
import { CartItem } from '../lib/cart'

@Component
class CartNavMenu extends Vue {
  @Prop({ default: [] }) readonly items!: CartItem[];

  private get count(): number {
    return this.items.length
  }

  private get isEmpty(): boolean {
    return this.count === 0
  }

  private onCheckoutClicked() {
    this.$refs.navmenu.toggle(false)
    this.$emit('checkout')
  }

  private get totalPrice(): number {
    return this.items.map(x => x.price).reduce((a, b) => a + b, 0)
  }

  public toggle(value: boolean) {
    this.$refs.navmenu.toggle(value)
  }
}

export default CartNavMenu
</script>
