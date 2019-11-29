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
class IndexPage extends Vue {
  get books(): Book[] {
    return [
      {
        id: '123',
        title: 'Бхагавад-гита',
        author: 'А.Ч. Бхактиведанта Свами Прабхупада',
        cover: 'http://bbt-online.ru/wp-content/uploads/Bhagavad-Gita-2.jpg'
      },
      {
        id: '234',
        title: 'Наука самоосознания',
        author: 'А.Ч. Бхактиведанта Свами Прабхупада',
        cover: 'http://bbt-online.ru/wp-content/uploads/Nauka-Samoosoznaniya-1.jpg'
      },
      {
        id: '345',
        title: 'Высший вкус',
        author: '',
        cover: 'http://bbt-online.ru/wp-content/uploads/Vysshiy-Vkus-1.jpg'
      },
      {
        id: '456',
        title: 'Махабхарата, том первый',
        author: 'Кришна-дхарма дас',
        cover: 'http://bbt-online.ru/wp-content/uploads/Mahabharata-1-1.jpg'
      },
      {
        id: '567',
        title: 'Махабхарата, том второй',
        author: 'Кришна-дхарма дас',
        cover: 'http://bbt-online.ru/wp-content/uploads/Mahabharata-2-1.jpg'
      }
    ]
  }
}

export default IndexPage
</script>
