<template>
  <div class="flex flex-row">
    <!-- Read sample -->
    <nuxt-link
      :to="readerUrl"
      class="bg-blue-500 rounded text-white text-center px-4 py-2 my-1 md:mr-2 text-sm"
    >
      Читать
    </nuxt-link>

    <!-- Download sample -->
    <div
      class="bg-blue-500 rounded text-white text-center px-4 py-2 my-1 md:mr-2 text-sm"
    >
      {{ actionText }}
      <a
        v-for="url in product.urls"
        :key="url.ext"
        :href="bought ? productUrl(url.ext) : sampleUrl(url.ext)"
        class="hover:text-blue-200"
        download
      >
        {{ url.ext.toUpperCase() }}
      </a>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Prop, Component } from 'vue-property-decorator'
import { Product } from '@/lib/book'
import { getSampleUrl, getProductUrl } from '@/lib/download'

@Component class DigitalBookControls extends Vue {
  @Prop() private readonly product!:Product
  @Prop() private readonly bought!:boolean

  private sampleUrl(ext: string): string {
    return getSampleUrl(this.product, ext)
  }

  private productUrl(ext: string): string {
    return getProductUrl(this.product, ext)
  }

  private get readerUrl(): string {
    return '/reader/?p=' + this.product.slug
  }

  private get actionText(): string {
    return this.bought ? 'Скачать' : 'Фрагмент'
  }
}

export default DigitalBookControls
</script>
