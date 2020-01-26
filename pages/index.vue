<template>
  <div>
    <div
      class="logo-background w-full object-cover mb-12"
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

    <div class="container mx-auto">
      <p class="mb-12">
        В 1972 году для публикации книг Шрилы Прабхупады было основано издательство «Бхактиведанта Бук Траст», которое является на данный момент самым большим в мире издательством в области индийской религии и философии, публикующим книги более чем на восьмидесяти языках
      </p>

      <bookshelf :books="books" />
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'
import { Group } from '~/lib/book'
import Bookshelf from '~/components/Bookshelf.vue'
import NavBar from '~/components/NavBar.vue'

@Component({ layout: 'plain', components: { NavBar, Bookshelf } })
class IndexPage extends Vue {
  private books: Group[] = [];

  async asyncData({ $axios }) {
    const { data } = await $axios.get('/products')
    return { books: data }
  }
}

export default IndexPage
</script>

<style scoped>
.logo-background {
  background-image: url(~assets/pages/index/bg.png);
  height: 32em;
}
</style>
