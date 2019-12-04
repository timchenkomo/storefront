<template>
  <div class="flex flex-row flex-wrap justify-around">
    <book-card
      v-for="book in books"
      :key="book.id"
      :title="book.title"
      :author="book.author"
      :cover="book.cover"
      :url="bookUrl(book.id)"
      class="mx-4 w-40"
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

  private bookUrl(bookId: string) {
    return '/books/' + bookId
  }
}

export default Bookshelf
</script>
