<template>
  <div class="overflow-hidden mb-3">
    <nuxt-link :to="url">
      <img :src="cover" class="rounded w-full">
      <div class="text-center">
        <div class="font-bold text-sm leading-none py-1">
          {{ title }}
        </div>
        <p
          class="text-gray-500 text-xs leading-none"
        >
          {{ author }}
        </p>
      </div>
    </nuxt-link>
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

  /** Url to go on click */
  @Prop() readonly url!: string;
}

export default BookCard
</script>
