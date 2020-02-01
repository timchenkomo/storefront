<template>
  <nav-menu
    class="block px-4 py-2"
    title="Мой ББТ"
  >
    <div class="flex flex-col text-black">
      <nuxt-link
        to="/me"
        class="mx-4 my-2"
      >
        Мои книги
      </nuxt-link>

      <hr>

      <a
        @click="$auth.logout()"
        href="#"
        class="mx-4 my-2"
      >
        Выйти
      </a>
    </div>
  </nav-menu>
</template>
