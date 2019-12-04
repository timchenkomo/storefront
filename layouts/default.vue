<template>
  <div>
    <nav-bar />
    <div class="container mx-auto">
      <nuxt />
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'
import NavBar from '@/components/NavBar.vue'

@Component({
  components: { NavBar }
})
class DefaultLayout extends Vue {
}

export default DefaultLayout
</script>
