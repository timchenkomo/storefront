<template>
  <div :class="{'border-b-2': borders}" class="w-auto py-6">
    <div class="container mx-auto flex items-center justify-between px-4 text-sm font-light">
      <nuxt-link to="/">
        <img :src="logoUrl">
      </nuxt-link>

      <nav :class="{'text-white': inverted }">
        <nuxt-link to="/about" class="px-4">
          Об издательстве
        </nuxt-link>
        <nuxt-link to="/books" class="px-4">
          Библиотека
        </nuxt-link>
        <nuxt-link to="/login" class="px-4">
          Войти
        </nuxt-link>
        <cart-button
          :open="isCartDropdownOpen"
          :items="myCartItems"
          @close="isCartDropdownOpen=false"
          @click="onMyBooksDropdownClick"
          @checkout="onCheckoutClicked"
        />
      </nav>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
import { CartItem } from '../lib/cart'
import CartButton from '~/components/CartButton.vue'
import { cartStore } from '~/store/index'

@Component({ components: { CartButton } })
class NavBar extends Vue {
  @Prop({ default: true }) readonly borders!: boolean;
  @Prop({ default: false }) readonly inverted!: boolean;

  private isCartDropdownOpen: boolean = false;

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
