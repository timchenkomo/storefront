<template>
  <div class="w-auto py-6 border-b-2">
    <div class="container mx-auto flex items-center justify-between px-4 text-sm font-light">
      <div>
        <img src="http://bbt-online.ru/wp-content/uploads/logo.svg">
      </div>

      <nav>
        <nuxt-link to="/about" class="px-4">
          Об издательстве
        </nuxt-link>
        <nuxt-link to="/books" class="px-4">
          Библиотека
        </nuxt-link>
        <nuxt-link to="/login" class="px-4">
          Войти
        </nuxt-link>
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
