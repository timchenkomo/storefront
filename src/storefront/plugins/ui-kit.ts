import Vue from 'vue'
import BookCard from '~/components/BookCard.vue'
import SignInForm from '~/components/SignInForm.vue'
import SignUpForm from '~/components/SignUpForm.vue'
import Msg from '~/components/Msg.vue'
import NavMenu from '~/components/nav/NavMenu.vue'
import NavBar from '~/components/nav/NavBar.vue'
import InCartButton from '~/components/InCartButton.vue'

Vue.component('book-card', BookCard)
Vue.component('login-form', SignInForm)
Vue.component('signup-form', SignUpForm)
Vue.component('msg', Msg)
Vue.component('nav-bar', NavBar)
Vue.component('nav-menu', NavMenu)
Vue.component('in-cart-button', InCartButton)
