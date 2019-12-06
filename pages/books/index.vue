<template>
  <section>
    <div class="flex justify-center pb-8">
      <bookshelf-filter v-model="query" class="m-4 w-2/3" />
    </div>
    <bookshelf :books="books" />
  </section>
</template>

<script lang="ts">
import { Vue, Component } from 'nuxt-property-decorator'
import axios from 'axios'
import { Book } from '@/lib/book'

import Bookshelf from '@/components/Bookshelf.vue'
import BookshelfFilter from '@/components/BookshelfFilter.vue'

@Component({
  components: { Bookshelf, BookshelfFilter }
})
class BooksIndexPage extends Vue {
  private query: string = '';
  private allBooks: Book[] = [];

  async asyncData() {
    const { data } = await axios.get('http://localhost:8000/books')
    return { allBooks: data }
  }

  get books(): Book[] {
    return this.allBooks.filter(
      x =>
        x.title.toLowerCase().includes(this.query.toLowerCase()) ||
        x.author.toLowerCase().includes(this.query.toLowerCase())
    )
  }
}

export default BooksIndexPage
</script>
