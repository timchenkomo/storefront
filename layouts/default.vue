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
          class="my-2"
        />
        <nuxt />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'
import NavBar from '@/components/NavBar.vue'
import { msgStore } from '@/store/index'
import { Message } from '@/lib/msg'

@Component({
  components: { NavBar }
})
class DefaultLayout extends Vue {
  get messages(): Message[] {
    return msgStore.messages
  }

  private onMsgClicked(idx: number) {
    msgStore.removeByIdx(idx)
  }
}

export default DefaultLayout
</script>
