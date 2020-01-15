<template>
  <div class="flex flex-col sm:flex-row">
    <!-- Product cover image -->
    <div class="w-full sm:w-1/3 mr-8 lg:mr-16 mb-8">
      <img :src="product.cover" class="rounded">

    </div>
    <!-- Content -->
    <div class="sm:w-2/3">
      <!-- Title and author -->
      <h1 class="mb-1 sm:mb-3 text-5xl leading-none font-prata">
        {{ product.title }}
      </h1>
      <div class="text-sm text-gray-500">
        Автор: <a href="#" class="underline">{{ product.author }}</a>
      </div>
      <div class="mt-2 sm:mt-4 text-sm text-gray-900 sm:leading-loose">
        {{ product.description }}
      </div>

      <!-- Variety switcher -->
      <variery-switcher
        :active="activeVarietyIdx"
        :varieties="varieties"
        @change="onVarietyChanged"
        class="my-2 sm:my-8"
      />

      <!-- Buy button -->
      <in-cart-button
        @add="onInCartButtonClicked"
        @checkout="onCheckoutButtonClicked"
        :inCart="isInCart"
        :price="variety.price"
        class="w-full my-4 sm:my-8"
      />

      <!-- Additional info -->
      <div class="text-sm font-light">
        <div v-if="variety.series">
          <span class="text-gray-500">Серия: </span><span class="text-gray-900">{{ variety.series }}</span>
        </div>
        <div v-if="variety.year_published">
          <span class="text-gray-500">Год выпуска: </span><span class="text-gray-900">{{ variety.year_published }}</span>
        </div>
        <div v-if="variety.publisher">
          <span class="text-gray-500">Издательство: </span><span class="text-gray-900">{{ variety.publisher }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'nuxt-property-decorator'
import axios from 'axios'
import IconButton from '@/components/IconButton.vue'
import InCartButton from '@/components/InCartButton.vue'
import VarierySwitcher from '@/components/VarietySwitcher.vue'
import { cartStore } from '~/store'
import { Product, EmptyBook, ProductVariety } from '@/lib/book'

@Component({
  components: { IconButton, InCartButton, VarierySwitcher }
})
class BookPage extends Vue {
  private activeVarietyIdx: number = 0
  private product: Product = EmptyBook

  async asyncData(ctx: any) {
    const { data } = await axios.get(
      'http://localhost:8000/products/' + ctx.params.id
    )

    if (!data.varieties) {
      // It is an error to get product without varieties
      throw new Error('There are no varieties for the specified product.')
    }

    return {
      product: data,
      activeVarietyIdx: data.varieties[0].id
    }
  }

  private get isInCart(): boolean {
    return cartStore.items
      .map(x => x.id)
      .includes(this.variety.id)
  }

  private get varieties() {
    return this.product.varieties
  }

  private get variety(): ProductVariety {
    return this.varieties.filter(v => v.id === this.activeVarietyIdx)[0]
  }

  private onVarietyChanged(varietyIdx: number) {
    this.activeVarietyIdx = varietyIdx
  }

  private onInCartButtonClicked() {
    cartStore.add({
      id: this.activeVarietyIdx,
      title: this.product.title,
      type: this.variety.title,
      price: this.variety.price,
      url: this.product.slug
    })
  }

  private onCheckoutButtonClicked() {
    this.$router.push('/cart')
  }
}

export default BookPage
</script>
