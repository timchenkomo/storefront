<template>
  <div class="font-montserrat">
    <nav-bar />
    <div class="mx-4 lg:mx-32">
      <div class="mx-auto mt-6">
        <!-- Flash messages -->
        <msg
          v-for="(msg, idx) in messages"
          @click="onMsgClicked(idx)"
          :key="idx"
          :msg="msg.msg"
          :color="msg.color || 'red'"
          class="my-2"
        />
        <nuxt />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'
import { msgStore } from '@/store/index'
import { Message } from '@/lib/msg'

@Component()
class DefaultLayout extends Vue {
  private msgCleanInterval

  private created() {
    this.msgCleanInterval = setInterval(() => msgStore.clean(), 1000)
  }

  private destroyed() {
    clearInterval(this.msgCleanInterval)
  }

  get messages(): Message[] {
    return msgStore.messages
  }

  private onMsgClicked(idx: number) {
    msgStore.removeByIdx(idx)
  }
}

export default DefaultLayout
</script>
