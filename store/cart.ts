import { Module, VuexModule, Mutation } from 'vuex-module-decorators'
import { CartItem } from '~/lib/cart'

@Module({
  name: 'cart',
  stateFactory: true,
  namespaced: true
})
export default class CartModule extends VuexModule {
  items: CartItem[] = []

  /** Add new item to the cart. */
  @Mutation public add(item: CartItem) {
    this.items.push(item)
  }

  /** Remove item from cart using specified id. */
  @Mutation public remove(id: string) {
    this.items = this.items.filter(x => x.id !== id)
  }
}
