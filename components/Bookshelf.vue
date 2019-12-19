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

    <div v-if="isNothingFound" class="text-xl">
      Ничего не найдено
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
import { Product } from '~/lib/book'

import BookCard from '@/components/BookCard.vue'

@Component({
  components: { BookCard }
})
class Bookshelf extends Vue {
  @Prop() readonly books: Product[] | undefined

  private bookUrl(bookId: string) {
    return '/books/' + bookId
  }

  private get isNothingFound(): boolean {
    return (this.books || []).length === 0
  }
}

export default Bookshelf
</script>
