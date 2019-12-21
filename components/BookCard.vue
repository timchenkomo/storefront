<template>
  <div
    @click="onClicked"
    class="overflow-hidden mb-3"
  >
    <div class="flex relative justify-center items-center">
      <img :src="cover" class="rounded w-full">
      <slot name="cover" />
    </div>

    <div class="text-center my-2">
      <div class="font-bold text-sm leading-tight my-1">
        {{ title }}
      </div>
      <p
        class="text-gray-500 text-xs leading-none"
      >
        {{ author }}
      </p>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'

@Component
class BookCard extends Vue {
  /** Title of a book */
  @Prop() readonly title!: string;

  /** URL of cover image */
  @Prop() readonly cover!: string;

  /** Author's name */
  @Prop() readonly author!: string;

  private onClicked(): void {
    this.$emit('click')
  }
}

export default BookCard
</script>
