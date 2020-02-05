<template>
  <div class="flex flex-row items-center">
    <button
      class="px-2 py-4"
      @click="onReturnClicked"
    >
      ← Назад
    </button>

    <in-cart-button
      v-if="product.price"
      @add="putInCart(product)"
      @checkout="checkout"
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

  /** Returns slug of a product opened in a reader. **/
  private get productSlug(): string {
    return this.$route.query.p
  }

  /** Fetch all the information about product when opened **/
  private async mounted() {
    const { data } = await this.$axios.get('/product/' + this.productSlug)
    this.product = data
  }

  /** Put specified product into the cart **/
  private putInCart(product: Product) {
    cartStore.add({
      id: product.slug,
      title: product.title,
      type: productType(product.type),
      price: product.price,
      url: product.slug
    })
  }

  /** Go to the checkout page **/
  private checkout() {
    this.$router.push('/cart')
  }

  /** Is the specified product was added to the cart? **/
  private isInCart(slug: String): boolean {
    return cartStore.items
      .map(x => x.id)
      .includes(slug)
  }

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
