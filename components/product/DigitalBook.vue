<template>
  <!-- Download sample -->
  <div
    class="bg-blue-500 rounded text-white text-center px-4 py-2 my-1 md:mr-2 text-sm"
  >
    {{ actionText }}
    <a
      v-for="url in product.urls"
      :key="url.ext"
      :href="bought ? productUrl(url) : sampleUrl(url)"
      class="hover:text-blue-200"
      download
    >
      {{ url.ext.toUpperCase() }}
    </a>
  </div>
</template>

<script lang="ts">
import { Vue, Prop, Component } from 'vue-property-decorator'
import { Product, Group, UrlInfo } from '@/lib/book'
import { getSampleUrl, getProductUrl } from '@/lib/download'

@Component class DigitalBookControls extends Vue {
  @Prop() private readonly product!:Product
  @Prop() private readonly group!:Group
  @Prop() private readonly bought!:boolean

  private sampleUrl(url: UrlInfo): string {
    return getSampleUrl(this.group, url.url)
  }

  private productUrl(url: UrlInfo): string {
    return getProductUrl(this.product, url.url)
  }

  private get actionText(): string {
    return this.bought ? 'Скачать' : 'Фрагмент'
  }
}

export default DigitalBookControls
</script>
