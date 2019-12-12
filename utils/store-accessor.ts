import { Store } from 'vuex'
import { getModule } from 'vuex-module-decorators'
import CartModule from '~/store/cart'

let cartStore: CartModule

function initialiseStores(store: Store<any>): void {
  cartStore = getModule(CartModule, store)
}

export {
  initialiseStores,
  cartStore
}
