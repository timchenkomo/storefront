<template>
  <div class="font-light text-sm">
    <cart :items="items" />
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'
import { CartItem } from '../lib/cart'
import Cart from '~/components/Cart.vue'
import { cartStore } from '~/store/index'

@Component({ components: { Cart } })
class CartPage extends Vue {
  private get items(): CartItem[] {
    return cartStore.items
  }
}

export default CartPage
</script>
