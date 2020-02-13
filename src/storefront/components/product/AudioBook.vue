<template>
  <button
    @click="onPlayClicked"
    class="bg-blue-500 rounded text-white px-4 py-2 my-1 md:mr-2 text-sm"
  >
    Слушать фрагмент
    <span v-if="progress" class="bg-blue-700 rounded ml-3 px-2 py-1">
      {{ Math.floor(progress * 100) }}%
    </span>
  </button>
</template>

<script lang="ts">
import { Vue, Prop, Component } from 'vue-property-decorator'
import { getSampleUrl } from '~/lib/download.ts'
import { Product } from '@/lib/book.ts'

@Component class AudioBookControls extends Vue {
  @Prop() private readonly product!:Product
  @Prop() private readonly bought!:boolean

  private audio: HTMLAudioElement | undefined
  private playing: boolean = false
  private progress: number = 0

  private destroyed() {
    if (this.audio) { this.audio.pause() }
  }

  private onPlayClicked() {
    const url = getSampleUrl(this.product.slug, 'mp3')

    if (!this.audio) {
      this.audio = this.createAudio(url)
      this.audio.play()
    } else if (this.playing) {
      this.audio.pause()
    } else {
      this.audio.play()
    }
  }

  private createAudio(url: string) {
    const audio = new Audio(url)
    audio.onplay = () => { this.playing = true }
    audio.onpause = () => { this.playing = false }
    audio.ontimeupdate = (value: Event) => {
      if (value !== null && value !== undefined && value.target) {
        const target = (value.target as HTMLMediaElement)
        this.progress = target.currentTime / target.duration
      }
    }
    return audio
  }
}

export default AudioBookControls
</script>
