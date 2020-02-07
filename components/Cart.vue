<template>
  <div>
    <!-- Cart is empty -->
    <div
      v-if="isEmpty"
      class="text-center text-xl"
    >
      Ваша корзина пуста
    </div>

    <!-- Cart -->
    <div
      v-if="!isEmpty"
    >
      <!-- List of items in cart -->
      <div
        v-for="item in items"
        :key="item.id"
        class="flex sm:mx-4 my-2 hover:bg-gray-200 px-1 py-1 rounded items-baseline"
      >
        <!-- Delete item button -->
        <span
          @click.stop="onDeleteItemClicked(item)"
          class="mr-1 px-2 font rounded text-red-500 bg-red-200 opacity-25 hover:opacity-100 cursor-pointer"
        >✕</span>

        <!-- Title and type -->
        <nuxt-link
          :to="'/books/' + item.url"
          class="truncate"
        >
          {{ item.title }}
        </nuxt-link>

        <span v-if="item.type" class="truncate px-2 mx-2 text-gray-100 text-xs bg-gray-400 rounded-full">
          {{ item.type }}
        </span>

        <!-- Price -->
        <span class="flex-grow" />
        <span>{{ item.price }}&nbsp;₽</span>
      </div>

      <!-- Total price -->
      <div class="mx-4 flex items-baseline">
        <span class="w-full" />
        <span class="text-3xl font-bold">{{ totalPrice }}</span>&nbsp;₽
      </div>

      <!-- Put an order -->
      <hr class="mt-2 mb-4">
      <input
        @click="save"
        class="px-4 py-2 text-white bg-blue-500 hover:bg-blue-600 rounded float-right"
        type="submit"
        value="Оплатить"
      >
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
import md5 from 'md5'
import { CartItem } from '../lib/cart'
import { cartStore } from '~/store/index'

@Component
class Cart extends Vue {
  @Prop({ default: [] }) readonly items!: CartItem[];

  private async save() {
    // save invoice at server and get invoice ID
    const itemsId = this.items.map(x => x.id)
    const { data } = await this.$axios.post('/payment/create', itemsId)
    const invoiceId = data.invoice_id

    // calculate signature
    const signature = md5('bbt-online:' + this.totalPrice + ':' + invoiceId + ':BJYhRoXsT454wP7aEz5y')

    // redirect to robocassa
    const url = 'https://auth.robokassa.ru/Merchant/Index.aspx' +
                '?IsTest=1' +
                '&MerchantLogin=bbt-online' +
                '&OutSum=' + this.totalPrice +
                '&InvId=' + invoiceId +
                '&SignatureValue=' + signature
    window.location = url
  }

  private get count(): number {
    return this.items.length
  }

  private get isEmpty(): boolean {
    return this.count === 0
  }

  private get totalPrice(): number {
    return this.items.map(x => x.price).reduce((a, b) => a + b, 0)
  }

  private onDeleteItemClicked(item: CartItem) {
    cartStore.remove(item.id)
  }
}

export default Cart
</script>
