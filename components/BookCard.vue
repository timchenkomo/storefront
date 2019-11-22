<template>
  <div>
    <img :src="cover" class="cover">
    <b>{{ title }}</b>
    <small>{{ author }}</small>
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
}

export default BookCard
</script>

<style scoped>
.cover {
  border-radius: 5px;
  max-width: 256px;
}
</style>
