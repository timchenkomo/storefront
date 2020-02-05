<template>
  <div class="flex flex-col sm:flex-row items-center">
    <!-- Return back button -->
    <button
      @click="onReturnClicked"
      class="px-4 py-4"
    >
      ← Назад
    </button>

    <!-- Put in cart button -->
    <in-cart-button
      v-if="product.price"
      @add="onPutInCartClicked(product)"
      @checkout="onCheckoutClicked"
      @remove="onRemoveClicked"
      :inCart="isInCart(product.slug)"
      :price="product.price"
    />
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'
import { cartStore } from '~/store'
import { productType } from '~/lib/book'

@Component
class ReaderNavExtension extends Vue {
  private product: any = {}

  /** Fetch all the information about product when opened **/
  private async mounted() {
    const { data } = await this.$axios.get('/product/' + this.productSlug)
    this.product = data
  }

  /** Returns slug of a product opened in a reader. **/
  private get productSlug(): string {
    return this.$route.query.p
  }

  /** Is the specified product was added to the cart? **/
  private isInCart(slug: String): boolean {
    return cartStore.items.map(x => x.id).includes(slug)
  }

  /** Put specified product into the cart **/
  private onPutInCartClicked(product: Product) {
    cartStore.add({
      id: product.slug,
      title: product.title,
      type: productType(product.type),
      price: product.price,
      url: product.group_slug
    })
  }

  /** Go to the checkout page **/
  private onCheckoutClicked() {
    this.$router.push('/cart')
  }

  /** On return button clicker. Return back **/
  private onReturnClicked() {
    this.$router.back()
  }

  /** Remove product from cart. **/
  private onRemoveClicked() {
    cartStore.remove(this.productSlug)
  }
}

export default ReaderNavExtension
</script>
