<template>
  <nav-menu
    ref="navmenu"
    class="block px-4 py-2"
    title="Мой ББТ"
    link="/me"
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

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'
import NavMenu from '@/components/nav/NavMenu.vue'

@Component class AccountNavMenu extends Vue {
  public toggle(value: boolean) {
    (this.$refs.navmenu as NavMenu).toggle(value)
  }
}

export default AccountNavMenu
</script>
