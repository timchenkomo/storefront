<template>
  <div
    v-if="canRead || hasSamples"
    class="flex flex-col sm:flex-row"
  >
    <!-- Read sample -->
    <nuxt-link
      v-if="canRead"
      :to="readerUrl"
      class="w-full bg-blue-500 rounded text-white text-center px-4 py-2 my-1 mr-2 text-sm"
    >
      Читать
    </nuxt-link>

    <!-- Download sample -->
    <div
      v-if="hasSamples"
      class="w-full bg-blue-500 rounded text-white text-center px-4 py-2 my-1 md:mr-2 text-sm whitespace-no-wrap"
    >
      {{ actionText }}
      <a
        v-for="format in bought ? product.formats : product.sample_formats"
        :key="format"
        :href="bought ? productUrl(format) : sampleUrl(format)"
        class="hover:text-blue-200"
        download
      >
        {{ format.toUpperCase() }}
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
    return getSampleUrl(this.product.slug, ext)
  }

  private productUrl(ext: string): string {
    return getProductUrl(this.product.slug, ext)
  }

  private get readerUrl(): string {
    return '/reader/?p=' + this.product.slug
  }

  private get actionText(): string {
    return this.bought ? 'Скачать' : 'Фрагмент'
  }

  private get hasSamples(): boolean {
    return !!this.product.sample_formats
  }

  private get canRead(): boolean {
    if (!this.hasSamples) {
      return false
    }
    // our online reader can read epubs only
    return this.product.sample_formats.includes('epub')
  }
}

export default DigitalBookControls
</script>
