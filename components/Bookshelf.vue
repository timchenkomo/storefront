<template>
  <div>
    <book-card
      v-for="book in books"
      :key="book.id"
      :title="book.title"
      :author="book.author"
      :cover="book.cover"
    />
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
import { Book } from '~/lib/book'

import BookCard from '@/components/BookCard.vue'

@Component({
  components: { BookCard }
})
class Bookshelf extends Vue {
  @Prop() readonly books: Book[] | undefined
}

export default Bookshelf
</script>
