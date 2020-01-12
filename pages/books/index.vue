<template>
  <section>
    <div class="flex justify-center pb-8">
      <bookshelf-filter v-model="query" class="m-4 w-2/3" />
    </div>

    <bookshelf
      @click="onProductClicked"
      :books="books"
      product-class="cursor-pointer"
    />
  </section>
</template>

<script lang="ts">
import { Vue, Component } from 'nuxt-property-decorator'
import axios from 'axios'
import { Product } from '@/lib/book'

import Bookshelf from '@/components/Bookshelf.vue'
import BookshelfFilter from '@/components/BookshelfFilter.vue'

@Component({
  components: { Bookshelf, BookshelfFilter }
})
class BooksIndexPage extends Vue {
  private query: string = '';
  private allBooks: Product[] = [];

  async asyncData() {
    const { data } = await axios.get('http://localhost:8000/products')
    return { allBooks: data }
  }

  get books(): Product[] {
    return this.allBooks.filter(
      x =>
        x.title.toLowerCase().includes(this.query.toLowerCase()) ||
        x.author.toLowerCase().includes(this.query.toLowerCase())
    )
  }

  private onProductClicked(product: Product) {
    this.$router.push('/books/' + product.slug)
  }
}

export default BooksIndexPage
</script>
