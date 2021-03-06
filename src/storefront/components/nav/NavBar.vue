<template>
  <header
    :class="{'border-b-2': borders}"
    class="sm:flex sm:justify-between sm:items-center sm:px-4 sm:py-3 text-sm font-light"
  >
    <div class="flex items-center justify-between px-4 py-3 sm:p-0">
      <nuxt-link to="/">
        <logo
          :class="{'text-white': inverted}"
          class="fill-current"
        />
      </nuxt-link>

      <div class="sm:hidden">
        <button @click="isOpen = !isOpen" type="button" class="block focus:outline-none">
          <svg
            :class="{'text-white': inverted}"
            class="h-6 w-6 fill-current"
            viewBox="0 0 24 24"
          >
            <path v-if="isOpen" fill-rule="evenodd" d="M18.278 16.864a1 1 0 0 1-1.414 1.414l-4.829-4.828-4.828 4.828a1 1 0 0 1-1.414-1.414l4.828-4.829-4.828-4.828a1 1 0 0 1 1.414-1.414l4.829 4.828 4.828-4.828a1 1 0 1 1 1.414 1.414l-4.828 4.829 4.828 4.828z" />
            <path v-if="!isOpen" fill-rule="evenodd" d="M4 5h16a1 1 0 0 1 0 2H4a1 1 0 1 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2zm0 6h16a1 1 0 0 1 0 2H4a1 1 0 0 1 0-2z" />
          </svg>
        </button>
      </div>
    </div>

    <nav
      :class="{'text-white': inverted, 'block': isOpen, 'hidden': !isOpen }"
      class="px-2 pt-2 pb-4 sm:flex sm:p-0 items-center"
    >
      <!-- Static links -->
      <nuxt-link
        v-if="showMainComponents"
        to="/about"
        class="block px-4 py-2 whitespace-no-wrap"
      >
        Об издательстве
      </nuxt-link>

      <nuxt-link
        v-if="showMainComponents"
        to="/books"
        class="block px-4 py-2 whitespace-no-wrap"
      >
        Библиотека
      </nuxt-link>

      <!-- Account -->
      <nuxt-link
        v-if="!isAuthenticated && showMainComponents"
        to="/me/signin"
        class="block px-4 py-2 whitespace-no-wrap"
      >
        Войти
      </nuxt-link>
      <account-nav-menu
        ref="account"
        v-if="isAuthenticated && showMainComponents"
      />

      <!-- Additional components -->
      <div :is="components" />

      <!-- Cart button -->
      <cart-nav-menu
        ref="cart"
        v-if="showMainComponents"
        :items="myCartItems"
        @checkout="onCheckoutClicked"
        class="block px-4 py-2"
      />
    </nav>
  </header>
</template>

<script lang="ts">
import { Vue, Component, Prop, Watch } from 'vue-property-decorator'
import { CartItem } from '@/lib/cart'
import CartNavMenu from '~/components/nav/CartNavMenu.vue'
import AccountNavMenu from '~/components/nav/AccountNavMenu.vue'
import { cartStore } from '~/store/index'
import Logo from '~/assets/logo.svg'
import ReaderNavExtension from '~/components/nav/extensions/ReaderNavExtension.vue'

@Component({
  components: { AccountNavMenu, CartNavMenu, Logo, ReaderNavExtension }
})
class NavBar extends Vue {
  private isOpen: boolean = false

  @Prop({ default: true }) readonly borders!: boolean;
  @Prop({ default: false }) readonly inverted!: boolean;

  @Watch('$route.path')
  private onRouteChanged() {
    const account = (this.$refs.account as AccountNavMenu)
    const cart = (this.$refs.cart as CartNavMenu)

    if (account) {
      account.toggle(false)
    }
    if (cart) {
      cart.toggle(false)
    }
  }

  get isAuthenticated(): boolean {
    return this.$auth.loggedIn
  }

  get myCartItems(): CartItem[] {
    return cartStore.items
  }

  private onCheckoutClicked() {
    this.$router.push('/cart')
  }

  private get components(): string | undefined {
    if (this.$route.path.startsWith('/reader')) {
      return 'ReaderNavExtension'
    }
    return undefined
  }

  private get showMainComponents(): boolean {
    if (this.$route.path.startsWith('/reader')) {
      return false
    }
    return true
  }
}

export default NavBar
</script>
