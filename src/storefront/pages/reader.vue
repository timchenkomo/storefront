<template>
  <client-only>
    <div>
      <div id="area" />

      <button
        v-if="ready"
        @click="prevPage"
        class="mx-1 px-1 py-2 rounded text-black left"
      >
        ←
      </button>
      <button
        v-if="ready"
        @click="nextPage"
        class="mx-1 px-1 py-2 rounded text-black right"
      >
        →
      </button>
      <keypress :key-code="39" @pressed="nextPage" event="keydown" />
      <keypress :key-code="37" @pressed="prevPage" event="keydown" />
    </div>
  </client-only>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'
import Epub from 'epubjs'
import Keypress from 'vue-keypress'
import { getSampleUrl } from '@/lib/download'

@Component({
  components: { Keypress },
  layout: 'wide'
})
class ReaderPage extends Vue {
  private rendition: any
  private ready: boolean = false

  private mounted() {
    const productSlug = (this.$route.query.p as string)
    const epubUrl = getSampleUrl(productSlug, 'epub')

    const book = Epub(epubUrl)
    book.ready.then(() => { this.ready = true })

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

  #area {
    background: white url('~assets/pages/reader/loader.gif') center center no-repeat;
  }

  #area .epub-view > iframe {
    background: white;
  }
</style>
