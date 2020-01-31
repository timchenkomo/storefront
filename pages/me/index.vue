<template>
  <div>
    <div class="flex justify-center pb-8">
      <bookshelf-filter v-model="query" class="m-4 w-2/3" />
    </div>

    <!-- List of my products -->
    <bookshelf :books="myProductsFiltered">
      <!-- Add downlaod button to each book. -->
      <template v-slot:cover="{ product }">
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
import Bookshelf from '~/components/Bookshelf.vue'
import BookshelfFilter from '@/components/BookshelfFilter.vue'
import Downloader from '@/components/Downloader.vue'
import DownloadIcon from '~/assets/download.svg'

import { Group, UrlInfo } from '~/lib/book'
import { msgStore } from '@/store/index'

@Component({
  middleware: ['auth'],
  components: {
    Bookshelf, BookshelfFilter, DownloadIcon, Downloader
  }
})
class MeIndexPage extends Vue {
  private myProducts: Group[] = []
  private isDownloaderVisible: boolean = false
  private downloaderOptions: UrlInfo[] = []
  private query: string = ''

  async asyncData({ $axios, redirect }) {
    try {
      const { data } = await $axios.get('/me/products')
      return { myProducts: data }
    } catch (ex) {
      msgStore.add({ msg: 'Необходима авторизация', color: 'red' })
      redirect('/me/signin')
    }
  }

  private get myProductsFiltered(): Group[] {
    return this.myProducts.filter(x =>
      x.title.toLowerCase().includes(this.query.toLowerCase()) ||
      x.author.toLowerCase().includes(this.query.toLowerCase())
    )
  }

  private onProductClicked(group: Group) {
    const getProductUrls = function(product) {
      return product.urls.map(url => ({
        ...url, // get all the data from original object
        'url': '/download/' + product.id + '/' + url.url // fix url to point to right place
      }))
    }

    this.isDownloaderVisible = true
    this.downloaderOptions = group.products
      .filter(x => x.urls !== undefined) // remove products without urls, like printed books
      .map(x => getProductUrls(x)) // fix urls
      .flat()
  }

  private onDownloaderClose() {
    this.isDownloaderVisible = false
  }
}

export default MeIndexPage
</script>
