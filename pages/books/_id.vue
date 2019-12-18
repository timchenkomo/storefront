<template>
  <div class="flex flex-row xl:mx-8">
    <!-- Cover -->
    <div class="w-1/3 mr-16">
      <img :src="product.cover" class="rounded">
    </div>

    <!-- Content -->
    <div class="w-2/3">
      <h1 class="font-serif text-5xl leading-none mb-3">
        {{ product.title }}
      </h1>
      <div class="text-sm text-gray-500">
        Автор: <a href="#">{{ product.author }}</a>
      </div>
      <div class="font-light text-sm text-gray-900 mt-4 leading-loose">
        {{ product.description }}
      </div>

      <variery-switcher
        :active="variery"
        :varieties="varieties"
        @change="onVarietyChanged"
      />

      <in-cart-button
        @addToCart="onInCartButtonClicked"
        @placeAnOrder="onPlaceAnOrderButtonClicked"
        :inCart="isInCart"
        :price="variety.price"
        class="w-full my-8"
      />

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
      title: (this.product.title + ' ' + (this.variety.title || '')).trim(),
      price: this.variety.price
    })
  }

  private onPlaceAnOrderButtonClicked() {
    console.log('Here is a new order')
  }

  private get variety(): ProductVariety {
    return this.product.varieties.filter(x => x.id === this.variery)[0] || EmptyProductVariety
  }
}

export default BookPage
</script>
