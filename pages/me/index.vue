<template>
  <div>
    <div class="flex justify-center pb-8">
      <bookshelf-filter v-model="query" class="m-4 w-2/3" />
    </div>

    <bookshelf :books="myProducts">
      <template v-slot:cover="product">
        <div
          @click="onProductClicked(product)"
          class="absolute flex justify-center items-center w-full h-full opacity-0 hover:opacity-100"
        >
          <div class="p-4 bg-blue-500 hover:bg-blue-400 rounded-full">
            <img src="http://bbt-online.ru/wp-content/themes/bbt/img/audio_icon_book.svg">
          </div>
        </div>
      </template>
    </bookshelf>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'
import axios from 'axios'
import Bookshelf from '~/components/Bookshelf.vue'
import BookshelfFilter from '@/components/BookshelfFilter.vue'
import { Product } from '~/lib/book'

@Component({ components: { Bookshelf, BookshelfFilter } })
class MeIndexPage extends Vue {
  private myProducts: Product[];
  private query: string = ''

  async asyncData() {
    const { data } = await axios.get('http://localhost:8000/me/products')
    return { myProducts: data }
  }

  private onProductClicked(product:any) {
    console.log(product)
  }
}

export default MeIndexPage
</script>
