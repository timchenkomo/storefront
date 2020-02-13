<template>
  <section>
    <div class="flex justify-center pb-8">
      <bookshelf-filter v-model="query" class="md:m-4 w-full md:w-2/3" />
    </div>

    <bookshelf
      @click="onProductClicked"
      :books="books"
      product-class="cursor-pointer"
    />
  </section>
</template>

<script lang="ts">
import { Context } from '@nuxt/types'
import { Vue, Component } from 'nuxt-property-decorator'
import { Group } from '@/lib/book'
import Bookshelf from '@/components/Bookshelf.vue'
import BookshelfFilter from '@/components/BookshelfFilter.vue'

@Component({
  components: { Bookshelf, BookshelfFilter }
})
class BooksIndexPage extends Vue {
  private query: string = '';
  private allBooks: Group[] = [];

  async asyncData(ctx: Context) {
    const { data } = await ctx.$axios.get('/products')
    return { allBooks: data }
  }

  get books(): Group[] {
    return this.allBooks.filter(x =>
      x.title.toLowerCase().includes(this.query.toLowerCase()) ||
      x.author.toLowerCase().includes(this.query.toLowerCase())
    )
  }

  private onProductClicked(product: Group) {
    this.$router.push('/books/' + product.slug)
  }
}

export default BooksIndexPage
</script>
