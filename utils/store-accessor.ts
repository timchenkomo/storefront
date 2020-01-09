import { Store } from 'vuex'
import { getModule } from 'vuex-module-decorators'
import CartModule from '~/store/cart'
import MsgModule from '~/store/msg'
import UserModule from '~/store/user'

let cartStore: CartModule
let msgStore: MsgModule
let userStore: UserModule

function initialiseStores(store: Store<any>): void {
  cartStore = getModule(CartModule, store)
  msgStore = getModule(MsgModule, store)
  userStore = getModule(UserModule, store)
}

export {
  initialiseStores,
  cartStore,
  msgStore,
  userStore
}
