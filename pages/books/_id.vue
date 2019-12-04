<template>
  <div class="p-4">
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
        <div class="my-10">
          <icon-button icon-url="http://bbt-online.ru/wp-content/themes/bbt/img/vector/digital_1.svg">
            Эл. книга
          </icon-button>

          <icon-button icon-url="http://bbt-online.ru/wp-content/themes/bbt/img/vector/press_1.svg">
            Аудиокнига
          </icon-button>
        </div>

        <div class="flex py-8">
          <buy-button price="250р" class="flex-auto mr-2" />
          <in-cart-button price="250р" />
        </div>

        <div class="text-sm font-light">
          <div><span class="text-gray-500">Серия: </span><span class="text-gray-900">Махабхарата</span></div>
          <div><span class="text-gray-500">Год выпуска: </span><span class="text-gray-900">2018</span></div>
          <div><span class="text-gray-500">Издательство: </span><span class="text-gray-900"> Фонд "Бхактиведанта"</span></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'
import IconButton from '@/components/IconButton.vue'
import BuyButton from '@/components/BuyButton.vue'
import InCartButton from '@/components/InCartButton.vue'

@Component({
  components: { IconButton, BuyButton, InCartButton }
})
class BookPage extends Vue {
}

export default BookPage
</script>
