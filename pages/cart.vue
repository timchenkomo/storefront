<template>
  <div class="font-light text-sm">
    <cart />
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'
import Cart from '~/components/Cart.vue'

@Component({ components: { Cart } })
class CartPage extends Vue {
}

export default CartPage
</script>
