<template>
  <div>
    <div class="flex justify-center pb-8">
      <bookshelf-filter v-model="query" class="m-4 w-2/3" />
    </div>

    <!-- List of my products -->
    <bookshelf :books="myFilteredProducts">
      <!-- Add downlaod button to each book. -->
      <template v-slot:cover="product">
        <div
          @click="onProductClicked(product)"
          class="absolute flex justify-center items-center w-full h-full opacity-0 hover:opacity-100"
        >
          <div class="p-4 bg-blue-500 hover:bg-blue-400 rounded-full">
            <download-icon class="w-6 h-6 fill-current text-white" />
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
import DownloadIcon from '~/assets/download.svg'

@Component({ components: { Bookshelf, BookshelfFilter, DownloadIcon } })
class MeIndexPage extends Vue {
  private myProducts: Product[] = [];
  private query: string = ''

  async asyncData() {
    const { data } = await axios.get('http://localhost:8000/me/products')
    return { myProducts: data }
  }

  private get myFilteredProducts(): Product[] {
    return this.myProducts
  }

  private onProductClicked(product:any) {
    console.log(product)
  }
}

export default MeIndexPage
</script>
