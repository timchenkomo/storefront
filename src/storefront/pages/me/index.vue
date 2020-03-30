<template>
  <div>
    <div class="flex justify-center pb-8">
      <bookshelf-filter v-model="query" class="md:m-4 w-full md:w-2/3" />
    </div>

    <!-- List of my products -->
    <bookshelf
      @click="onProductClicked($event)"
      :books="myProductsFiltered"
    >
      <!-- Add downlaod button to each book. -->
      <template v-slot:cover="{ product }">
        <div class="absolute hidden md:flex justify-center items-center w-full h-full opacity-0 hover:opacity-100">
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
import { Context } from '@nuxt/types'
import { Vue, Component } from 'nuxt-property-decorator'
import Bookshelf from '~/components/Bookshelf.vue'
import BookshelfFilter from '@/components/BookshelfFilter.vue'
import Downloader from '@/components/Downloader.vue'
import DownloadIcon from '~/assets/download.svg'

import { Group } from '~/lib/book'
import { msgStore } from '@/store/index'
import { getProductUrl } from '@/lib/download'

@Component({
  middleware: ['auth'],
  components: {
    Bookshelf, BookshelfFilter, DownloadIcon, Downloader
  }
})
class MeIndexPage extends Vue {
  private myProducts: Group[] = []
  private isDownloaderVisible: boolean = false
  private downloaderOptions: any[] = []
  private query: string = ''

  async asyncData(ctx: Context) {
    try {
      const { data } = await ctx.$axios.get('/me/products')
      return { myProducts: data }
    } catch (ex) {
      msgStore.add({ msg: 'Необходима авторизация', color: 'red' })
      ctx.redirect('/me/signin')
    }
  }

  private get myProductsFiltered(): Group[] {
    return this.myProducts.filter(x =>
      x.title.toLowerCase().includes(this.query.toLowerCase()) ||
      x.author.toLowerCase().includes(this.query.toLowerCase())
    )
  }

  private onProductClicked(group: Group) {
    this.isDownloaderVisible = true
    this.downloaderOptions = group.products
      .map(product => product.formats.map(f => ({
        url: getProductUrl(product.slug, f),
        ext: f
      })))
      .flat()
  }

  private onDownloaderClose() {
    this.isDownloaderVisible = false
  }
}

export default MeIndexPage
</script>
