<template>
  <div>
    <!-- index page hero component -->
    <div
      class="logo-background w-full object-cover mb-6 lg:mb-12 pb-2"
    >
      <nav-bar :borders="false" :inverted="true" />

      <div class="my-8 h-64 flex flex-col justify-center align-middle items-center text-white text-center">
        <h1 class="max-w-xl text-5xl font-serif leading-none">
          Жемчужины ведической литературы
        </h1>

        <h2 class="max-w-xl my-4 text-lg">
          Все книги издательства «Бхактиведанта Бук Траст» теперь доступны здесь в электронном формате
        </h2>
      </div>
    </div>

    <!-- description -->
    <div class="px-2 container mx-auto">
      <p class="mb-12">
        В 1972 году для публикации книг Шрилы Прабхупады было основано издательство «Бхактиведанта Бук Траст», которое является на данный момент самым большим в мире издательством в области индийской религии и философии, публикующим книги более чем на восьмидесяти языках
      </p>

      <!-- list of books -->
      <bookshelf
        @click="onGroupClicked"
        :books="groups"
        product-class="cursor-pointer"
      />
    </div>
  </div>
</template>

<script lang="ts">
import { Context } from '@nuxt/types'
import { Vue, Component } from 'nuxt-property-decorator'
import { Group } from '~/lib/book'
import Bookshelf from '~/components/Bookshelf.vue'

@Component({ layout: 'plain', components: { Bookshelf } })
class IndexPage extends Vue {
  private groups: Group[] = [];

  async asyncData(ctx: Context) {
    const { data } = await ctx.$axios.get('/products')
    return { groups: data }
  }

  private onGroupClicked(group: Group) {
    this.$router.push('/books/' + group.slug)
  }
}

export default IndexPage
</script>

<style scoped>
.logo-background {
  background-image: url(~assets/pages/index/bg.jpg);
  min-height: 32em;
}
</style>
