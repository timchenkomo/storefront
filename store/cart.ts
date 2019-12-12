import { Module, VuexModule, Mutation } from 'vuex-module-decorators'
import { CartItem } from '~/lib/cart'
import { Book } from '~/lib/book'

@Module({
  name: 'cart',
  stateFactory: true,
  namespaced: true
})
export default class CartModule extends VuexModule {
  items: CartItem[] = []

  @Mutation
  public add(item: Book) {
    this.items.push({
      product: item,
      quantity: 1
    })
  }
}
