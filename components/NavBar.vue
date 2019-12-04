<template>
  <div class="w-auto py-6 border-b-2 mb-12">
    <div class="container mx-auto flex items-center justify-between px-4 text-sm font-light">
      <div>
        <img src="http://bbt-online.ru/wp-content/uploads/logo.svg">
      </div>

      <nav>
        <span class="px-4">
          Об издательстве
        </span>
        <span class="px-4">
          Библиотека
        </span>
        <span class="px-4">
          Войти
        </span>
      </nav>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'

@Component
class NavBar extends Vue {
  @Prop() readonly price!: string;
}

export default NavBar
</script>
