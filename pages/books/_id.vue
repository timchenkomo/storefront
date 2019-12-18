<template>
  <div class="flex flex-col sm:flex-row">
    <!-- Product cover image -->
    <div class="w-full sm:w-1/3 mr-8 mb-8">
      <img :src="product.cover" class="rounded">
    </div>

    <!-- Content -->
    <div class="sm:w-2/3">
      <!-- Title and author -->
      <h1 class="mb-1 sm:mb-3 font-serif text-5xl leading-none">
        {{ product.title }}
      </h1>
      <div class="text-sm text-gray-500">
        Автор: <a href="#">{{ product.author }}</a>
      </div>
      <div class="mt-2 sm:mt-4 text-gray-900 sm:leading-loose">
        {{ product.description }}
      </div>

      <!-- Variety switcher -->
      <variery-switcher
        :active="variery"
        :varieties="varieties"
        @change="onVarietyChanged"
        class="my-2 sm:my-8"
      />

      <!-- Buy button -->
      <in-cart-button
        @addToCart="onInCartButtonClicked"
        @placeAnOrder="onPlaceAnOrderButtonClicked"
        :inCart="isInCart"
        :price="variety.price"
        class="w-full my-4 sm:my-8"
      />

      <!-- Additional info -->
      <div class="text-sm font-light">
        <div>
          <span class="text-gray-500">Серия: </span><span class="text-gray-900">Махабхарата</span>
        </div>
        <div>
          <span class="text-gray-500">Год выпуска: </span><span class="text-gray-900">2018</span>
        </div>
        <div>
          <span class="text-gray-500">Издательство: </span><span class="text-gray-900"> Фонд "Бхактиведанта"</span>
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
import { Product, EmptyBook, ProductVariety, EmptyProductVariety } from '@/lib/book'

@Component({
  components: { IconButton, InCartButton, VarierySwitcher }
})
class BookPage extends Vue {
  private variery: string = 'digital';
  private product: Product = EmptyBook;

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
      variery: data.varieties[0].id // set first variety as an active
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

  private onVarietyChanged(variety: string) {
    this.variery = variety
  }

  private onInCartButtonClicked() {
    cartStore.add({
      id: this.variery,
      title: this.product.title,
      type: this.variety.title,
      price: this.variety.price,
      url: this.product.id
    })
  }

  private onPlaceAnOrderButtonClicked() {
    this.$router.push('/cart')
  }

  private get variety(): ProductVariety {
    return this.product.varieties.filter(x => x.id === this.variery)[0] || EmptyProductVariety
  }
}

export default BookPage
</script>
