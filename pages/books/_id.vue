<template>
  <div class="flex flex-row xl:mx-8">
    <!-- Cover -->
    <div class="w-1/3 mr-16">
      <img :src="book.cover" class="rounded">
    </div>

    <!-- Content -->
    <div class="w-2/3">
      <h1 class="font-serif text-5xl leading-none mb-3">
        {{ book.title }}
      </h1>
      <div class="text-sm text-gray-500">
        Автор: <a href="#">{{ book.author }}</a>
      </div>
      <div class="font-light text-sm text-gray-900 mt-4 leading-loose">
        {{ book.desc }}
      </div>

      <!-- Buttons -->
      <variery-switcher
        :active="activeVariery"
        :varieties="varieties"
        @change="onVarietyChanged"
      />

      <div class="flex my-8">
        <buy-button price="250р" class="flex-auto mr-2" />
        <in-cart-button @click="onInCartButtonClicked" price="250р" />
      </div>

      <div class="text-sm font-light">
        <div><span class="text-gray-500">Серия: </span><span class="text-gray-900">Махабхарата</span></div>
        <div><span class="text-gray-500">Год выпуска: </span><span class="text-gray-900">2018</span></div>
        <div><span class="text-gray-500">Издательство: </span><span class="text-gray-900"> Фонд "Бхактиведанта"</span></div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'nuxt-property-decorator'
import axios from 'axios'
import IconButton from '@/components/IconButton.vue'
import BuyButton from '@/components/BuyButton.vue'
import InCartButton from '@/components/InCartButton.vue'
import VarierySwitcher from '@/components/VarietySwitcher.vue'
import { cartStore } from '~/store'
import { Book } from '@/lib/book'

@Component({
  components: { IconButton, BuyButton, InCartButton, VarierySwitcher }
})
class BookPage extends Vue {
  private activeVariery: string = 'digital';
  private book: Book = { id: '1', title: '', author: '', cover: '' }

  async asyncData(ctx) {
    const { data } = await axios.get('http://localhost:8000/books/' + ctx.params.id)
    return { book: data }
  }

  private get varieties() {
    return [
      'digital', 'audio', 'press'
    ]
  }

  private onVarietyChanged(variety: string) {
    this.activeVariery = variety
  }

  private onInCartButtonClicked() {
    cartStore.add(this.book)
  }
}

export default BookPage
</script>
