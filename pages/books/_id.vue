<template>
  <div class="flex flex-col sm:flex-row">
    <!-- Product cover image -->
    <div class="w-full sm:w-1/3 mr-8 lg:mr-16 mb-8">
      <img :src="group.cover" class="rounded">
    </div>

    <!-- Content -->
    <div class="sm:w-2/3">
      <!-- Title and author -->
      <h1 class="mb-1 sm:mb-3 text-5xl leading-none font-prata">
        {{ group.title }}
      </h1>
      <div class="text-sm text-gray-500">
        Автор: <a href="#" class="underline">{{ group.author }}</a>
      </div>
      <div class="mt-2 sm:mt-4 text-sm text-gray-900 sm:leading-loose">
        {{ group.description }}
      </div>

      <!-- Product type switcher -->
      <ul
        v-if="hasManyProducts"
        class="flex mt-4 mb-4"
      >
        <li
          v-for="product in group.products"
          :key="product.id"
          class="flex-1 mr-2"
        >
          <a
            :class="{'bg-gray-200 text-blue-500': product.id == productId, '': product.id != productId}"
            @click="productId = product.id"
            class="text-center block rounded py-2 px-4 cursor-pointer text-sm"
          >
            {{ productType(product.type) }}
          </a>
        </li>
      </ul>

      <!-- Product additional info -->
      <div
        v-for="product in group.products"
        v-if="product.id == productId"
        :key="product.id"
      >
        <!-- Additional components accoring to product type -->
        <div :is="product.type + '-book'" />

        <!-- Buy product button -->
        <in-cart-button
          @add="putInCart(product)"
          @checkout="checkout"
          :inCart="isInCart(product.id)"
          :price="product.price"
          class="w-full my-4 sm:my-4"
        />

        <!-- Additional info -->
        <div class="text-sm font-light">
          <div v-if="product.series">
            <span class="text-gray-500">Серия: </span><span class="text-gray-900">{{ product.series }}</span>
          </div>
          <div v-if="product.year_published">
            <span class="text-gray-500">Год выпуска: </span><span class="text-gray-900">{{ product.year_published }}</span>
          </div>
          <div v-if="product.publisher">
            <span class="text-gray-500">Издательство: </span><span class="text-gray-900">{{ product.publisher }}</span>
          </div>
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

import DigitalBook from '@/components/product/DigitalBook.vue'
import AudioBook from '@/components/product/AudioBook.vue'
import PrintedBook from '@/components/product/PrintedBook.vue'

@Component({
  components: {
    IconButton,
    InCartButton,
    VarierySwitcher,
    DigitalBook,
    AudioBook,
    PrintedBook
  }
})
class BookPage extends Vue {
  private productId: number = 0
  private group: Product = EmptyBook

  async asyncData(ctx: any) {
    const { data } = await axios.get('/products/' + ctx.params.id)

    if (!data.products) {
      // It is an error to get product without varieties
      throw new Error('There are no products for the specified group.')
    }

    return {
      group: data,
      productId: data.products[0].id
    }
  }

  /** Are there many products in the group? **/
  private get hasManyProducts(): boolean {
    return this.group.products.length > 1
  }

  /** Put specified product into the cart **/
  private putInCart(product: ProductVariety) {
    cartStore.add({
      id: product.id,
      title: this.group.title,
      type: this.productType(product.type),
      price: product.price,
      url: this.group.slug
    })
  }

  /** Go to the checkout page **/
  private checkout() {
    this.$router.push('/cart')
  }

  /** Is the specified product was added to the cart? **/
  private isInCart(id: number): boolean {
    return cartStore.items
      .map(x => x.id)
      .includes(id)
  }

  private productType(type: string): string {
    if (type === 'digital') { return 'Эл. книга' }
    if (type === 'audio') { return 'Аудиокнига' }
    if (type === 'printed') { return 'Печатная' }
  }
}

export default BookPage
</script>
