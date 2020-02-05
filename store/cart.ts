import { Module, VuexModule, Mutation } from 'vuex-module-decorators'
import { CartItem } from '~/lib/cart'

@Module({
  name: 'cart',
  stateFactory: true,
  namespaced: true
})
export default class CartModule extends VuexModule {
  items: CartItem[] = []

  @Mutation
  public add(item: CartItem) {
    this.items.push(item)
  }

  @Mutation
  public remove(id: string) {
    this.items = this.items.filter(x => x.id !== id)
  }
}
