<template>
  <client-only>
    <div>
      <div id="area" />
      <button
        @click="prevPage"
        class="mx-1 px-1 py-2 rounded text-black left"
      >
        ←
      </button>
      <button
        @click="nextPage"
        class="mx-1 px-1 py-2 rounded text-black right"
      >
        →
      </button>
    </div>
  </client-only>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'
import Epub from 'epubjs'
import { getSampleUrl } from '@/lib/download'

@Component({ layout: 'wide' })
class ReaderPage extends Vue {
  private redention: any;

  private mounted() {
    const productSlug = this.$route.query.p
    const epubUrl = this.downloadUrl(productSlug)

    console.log(epubUrl)

    const book = Epub(epubUrl)
    this.rendition = book.renderTo('area', {
      width: '100%', height: 600, spread: 'always'
    })
    this.rendition.display()
  }

  private prevPage() {
    this.rendition.prev()
  }

  private nextPage() {
    this.rendition.next()
  }

  private downloadUrl(productSlug: str) {
    return 'http://localhost' + getSampleUrl({ slug: productSlug }, 'epub')
  }
}

export default ReaderPage
</script>

<style>
  .left {
    position: fixed;
    top: 50%;
    left: 0%;
    transform: translate(0%, -50%);
  }
  .right {
    position: fixed;
    top: 50%;
    right: 0%;
    transform: translate(0%, -50%);
  }
</style>
