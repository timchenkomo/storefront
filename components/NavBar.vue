<template>
  <header
    :class="{'border-b-2': borders}"
    class="sm:flex sm:justify-between sm:items-center sm:px-4 sm:py-3 text-sm font-light"
  >
    <div class="flex items-center justify-between px-4 py-3 sm:p-0">
      <nuxt-link to="/">
        <img :src="logoUrl">
      </nuxt-link>

      <div class="sm:hidden">
        <button @click="isOpen = !isOpen" type="button" class="block focus:outline-none">
          <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24">
            <path v-if="isOpen" fill-rule="evenodd" d="M18.278 16.864a1 1 0 0 1-1.414 1.414l-4.829-4.828-4.828 4.828a1 1 0 0 1-1.414-1.414l4.828-4.829-4.828-4.828a1 1 0 0 1 1.414-1.414l4.829 4.828 4.828-4.828a1 1 0 1 1 1.414 1.414l-4.828 4.829 4.828 4.828z"/>
            <path v-if="!isOpen" fill-rule="evenodd" d="M4 5h16a1 1 0 0 1 0 2H4a1 1 0 1 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2z"/>
          </svg>
        </button>
      </div>
    </div>

    <nav
      :class="{'text-white': inverted, 'block': isOpen, 'hidden': !isOpen }"
      class="px-2 pt-2 pb-4 sm:flex sm:p-0 items-center"
    >
      <nuxt-link to="/about" class="block px-4 py-2">
        Об издательстве
      </nuxt-link>

      <nuxt-link to="/books" class="block px-4 py-2">
        Библиотека
      </nuxt-link>

      <nuxt-link v-if="!isAuthenticated" to="/me/signin" class="block px-4 py-2">
        Войти
      </nuxt-link>

      <nuxt-link v-else to="/me" class="block px-4 py-2">
        Мой ББТ
      </nuxt-link>

      <cart-button
        :open="isCartDropdownOpen"
        :items="myCartItems"
        @close="isCartDropdownOpen=false"
        @click="onMyBooksDropdownClick"
        @checkout="onCheckoutClicked"
        class="block px-4 py-2"
      />
    </nav>
  </header>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
import { CartItem } from '../lib/cart'
import CartButton from '~/components/CartButton.vue'
import { cartStore, userStore } from '~/store/index'

@Component({ components: { CartButton } })
class NavBar extends Vue {
  private isOpen: boolean = false;
  @Prop({ default: true }) readonly borders!: boolean;
  @Prop({ default: false }) readonly inverted!: boolean;

  private isCartDropdownOpen: boolean = false;

  get isAuthenticated(): boolean {
    return userStore.isAuthenticated
  }

  get logoUrl(): string {
    return this.inverted
      ? 'http://bbt-online.ru/wp-content/themes/bbt/img/main-page-logo.svg'
      : 'http://bbt-online.ru/wp-content/uploads/logo.svg'
  }

  get myCartItems(): CartItem[] {
    return cartStore.items
  }

  private onMyBooksDropdownClick() {
    this.isCartDropdownOpen = !this.isCartDropdownOpen
  }

  private onCheckoutClicked() {
    this.isCartDropdownOpen = false
    this.$router.push('/cart')
  }
}

export default NavBar
</script>
