<template>
  <div>
    <div class="flex justify-center pb-8">
      <bookshelf-filter v-model="query" class="m-4 w-2/3" />
    </div>

    <!-- List of my products -->
    <bookshelf :books="myFilteredProducts">
      <!-- Add downlaod button to each book. -->
      <template v-slot:cover="product">
        <div class="absolute flex justify-center items-center w-full h-full opacity-0 hover:opacity-100">
          <div
            @click="onProductClicked(product)"
            class="p-4 bg-blue-500 hover:bg-blue-400 rounded-full cursor-pointer"
          >
            <download-icon class="w-6 h-6 fill-current text-white" />
          </div>
        </div>
      </template>
    </bookshelf>

    <!-- Product downloader -->
    <downloader
      :visible="isDownloaderVisible"
      :options="downloaderOptions"
      @close="onDownloaderClose"
      title="Бхагавад-гита как она есть"
      class="absolute align-center justify-center"
    />
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'nuxt-property-decorator'
import axios from 'axios'
import Bookshelf from '~/components/Bookshelf.vue'
import BookshelfFilter from '@/components/BookshelfFilter.vue'
import Downloader from '@/components/Downloader.vue'
import { Product } from '~/lib/book'
import DownloadIcon from '~/assets/download.svg'

@Component({ components: {
  Bookshelf, BookshelfFilter, DownloadIcon, Downloader
} })
class MeIndexPage extends Vue {
  private myProducts: Product[]
  private isDownloaderVisible: boolean = false
  private downloaderOptions: any = [
    { type: 'epub', url: 'dsdsd' },
    { type: 'fb2', url: 'dsdsd' },
    { type: 'mp3', url: 'dsdsd' }
  ]
  private query: string = ''

  async asyncData() {
    const { data } = await axios.get('http://localhost:8000/me/products')
    return { myProducts: data }
  }

  private get myFilteredProducts(): Product[] {
    return this.myProducts
  }

  private onProductClicked(product: any) {
    this.isDownloaderVisible = true
    console.log(product)
  }

  private onDownloaderClose() {
    this.isDownloaderVisible = false
  }
}

export default MeIndexPage
</script>
