<template>
  <section>
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
class BooksIndexPage extends Vue {
  get books(): Book[] {
    return [
      {
        id: 'bg',
        title: 'Бхагавад-гита',
        author: 'А.Ч. Бхактиведанта Свами Прабхупада',
        cover: 'http://bbt-online.ru/wp-content/uploads/Bhagavad-Gita-2.jpg'
      },
      {
        id: 'ns',
        title: 'Наука самоосознания',
        author: 'А.Ч. Бхактиведанта Свами Прабхупада',
        cover: 'http://bbt-online.ru/wp-content/uploads/Nauka-Samoosoznaniya-1.jpg'
      },
      {
        id: 'vv',
        title: 'Высший вкус',
        author: '',
        cover: 'http://bbt-online.ru/wp-content/uploads/Vysshiy-Vkus-1.jpg'
      },
      {
        id: 'mh1',
        title: 'Махабхарата, том первый',
        author: 'Кришна-дхарма дас',
        cover: 'http://bbt-online.ru/wp-content/uploads/Mahabharata-1-1.jpg'
      },
      {
        id: 'mh2',
        title: 'Махабхарата, том второй',
        author: 'Кришна-дхарма дас',
        cover: 'http://bbt-online.ru/wp-content/uploads/Mahabharata-2-1.jpg'
      }
    ]
  }
}

export default BooksIndexPage
</script>
