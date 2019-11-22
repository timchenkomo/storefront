<template>
  <section class="section">
    <bookshelf :books="books" />
  </section>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'
import { Book } from '@/lib/book'

import Bookshelf from '@/components/Bookshelf.vue'

@Component({
  components: { Bookshelf }
})
class IndexPage extends Vue {
  get books(): Book[] {
    return [
      {
        id: '123',
        title: 'Бхагавад-гита',
        author: 'А.Ч. Бхактиведанта Свами Прабхупада',
        cover: 'http://bbt-online.ru/wp-content/uploads/Bhagavad-Gita-2.jpg'
      }
    ]
  }
}

export default IndexPage
</script>
