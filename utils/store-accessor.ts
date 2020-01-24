import { Store } from 'vuex'
import { getModule } from 'vuex-module-decorators'
import CartModule from '~/store/cart'
import MsgModule from '~/store/msg'

let cartStore: CartModule
let msgStore: MsgModule

function initialiseStores(store: Store<any>): void {
  cartStore = getModule(CartModule, store)
  msgStore = getModule(MsgModule, store)
}

export {
  initialiseStores,
  cartStore,
  msgStore,
}
