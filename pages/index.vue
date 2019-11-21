<template>
  <section class="section">
    {{ hello }}
  </section>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator'

@Component
class IndexPage extends Vue {
  hello: string = 'This is a message';
}

export default IndexPage
</script>
