<template>
  <div class="container p-4 mx-auto">
    <div class="flex flex-row">
      <!-- Cover -->
      <div class="w-1/3 mr-16">
        <img class="rounded" src="http://bbt-online.ru/wp-content/uploads/Mahabharata-1-1.jpg">
      </div>

      <!-- Content -->
      <div class="w-2/3">
        <h1 class="font-serif text-5xl leading-none mb-3">
          Махабхарата, том первый
        </h1>
        <div class="text-sm text-gray-500">
          Автор: <a href="#">в пересказе Кришна-Дхармы</a>
        </div>
        <div class="font-light text-sm text-gray-900 mt-4 leading-loose">
          «Махабхарата» Кришна-Дхармы даса представляет собой художественное изложение самой сути одноименного многотомного эпоса. Пересказав сокращенно древнюю поэму, но не упустив при этом ни одной важной детали, автор дает читателю замечательную возможность погрузиться в атмосферу того великого времени, когда на Земле присутствовал Сам Кришна.
        </div>

        <!-- Buttons -->
        <hr class="my-6">

        <div class="inline-block mr-6">
          <img class="h-5 mr-4 inline-block fill-current" src="http://bbt-online.ru/wp-content/themes/bbt/img/vector/digital_1.svg">
          <span class="text-sm font-light">
            Эл. книга
          </span>
        </div>

        <div class="inline-block mr-6">
          <img class="h-5 mr-4 inline-block" src="http://bbt-online.ru/wp-content/themes/bbt/img/vector/press_1.svg">
          <span class="text-sm font-light">
            Аудиокнига
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'
// import { Book } from '@/lib/book'

@Component
class BookPage extends Vue {

}

export default BookPage
</script>
