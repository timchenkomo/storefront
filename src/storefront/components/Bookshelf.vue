<template functional>
  <div class="flex flex-row flex-wrap justify-center">
    <book-card
      v-for="book in props.books"
      :key="book.slug"
      :title="book.title"
      :author="book.author"
      :cover="'/downloads/' + book.slug + '/cover.jpg'"
      :url="'/book/' + book.slug"
      :class="props.productClass"
      @click="listeners.click ? listeners.click(book) : null"
      class="mx-4 w-64 sm:w-40"
    >
      <template v-slot:cover>
        <slot v-bind:product="book" name="cover" />
      </template>
    </book-card>

    <div v-if="props.books.length == 0" class="text-xl">
      Ничего не найдено
    </div>
  </div>
</template>
