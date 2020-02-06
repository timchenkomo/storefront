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
      <form action="https://auth.robokassa.ru/Merchant/Index.aspx" method="POST">
        <input type="hidden" name="IsTest" value="1">
        <input type="hidden" name="MerchantLogin" value="bbt-online">
        <input :value="totalPrice" type="hidden" name="OutSum">
        <input type="hidden" name="InvId" value="0">
        <input type="hidden" name="Description" value="Книжечек прикупил">
        <input :value="signature" type="hidden" name="SignatureValue">
        <input type="hidden" name="Culture" value="ru">
        <input type="hidden" name="Email" value="test@test.ru">
        <input type="hidden" name="ExpirationDate" value="2029-01-16T12:00">

        <hr class="my-4">

        <input class="px-4 py-2 text-white bg-blue-500 hover:bg-blue-600 rounded float-right" type="submit" value="Оплатить">
      </form>
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

  private get count(): number {
    return this.items.length
  }

  private get isEmpty(): boolean {
    return this.count === 0
  }

  private get totalPrice(): number {
    return this.items.map(x => x.price).reduce((a, b) => a + b, 0)
  }

  private get signature(): string {
    return md5('bbt-online:' + this.totalPrice + ':0:BJYhRoXsT454wP7aEz5y')
  }

  private onDeleteItemClicked(item: CartItem) {
    cartStore.remove(item.id)
  }
}

export default Cart
</script>
