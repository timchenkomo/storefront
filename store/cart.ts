import { Module, VuexModule, Mutation, Action } from 'vuex-module-decorators'
import { CartItem } from '~/lib/cart'
import { $axios } from '~/utils/api'

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

  /** Remove all items from cart */
  @Mutation public empty() {
    this.items = []
  }

  /** Create invoice **/
  @Action({ rawError: true }) async createInvoice(): Promise<number> {
    const itemsId = this.items.map(x => x.id)
    const { data } = await $axios.post('/payment/create', itemsId)
    return data.invoice_id
  }
}
