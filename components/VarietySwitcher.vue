<template>
  <div class="my-8 flex flex-col md:flex-row">
    <!-- digital -->
    <icon-button
      v-if="varieties.includes('digital')"
      :active="active == 'digital'"
      @click="onVarietyChanged('digital')"
      class="mr-6 cursor-pointer"
    >
      <template v-slot:icon>
        <svg
          class="h-5 mr-2 inline-block fill-current"
          viewBox="0 0 14 18"
        >
          <path d="M8.2 15A1.2 1.2 0 117 13.8 1.2 1.2 0 018.2 15zM14 3v12a3 3 0 01-3 3H3a3 3 0 01-3-3V3a3 3 0 013-3h8a3 3 0 013 3zm-1 0a2 2 0 00-2-2H3a2 2 0 00-2 2v12a2 2 0 002 2h8a2 2 0 002-2zm-2.5 1h-7a.5.5 0 000 1h7a.5.5 0 000-1zm0 2h-7a.5.5 0 000 1h7a.5.5 0 000-1zm0 2h-7a.5.5 0 000 1h7a.5.5 0 000-1zm0 2h-7a.5.5 0 000 1h7a.5.5 0 000-1z" />
        </svg>
      </template>
      Эл.книга
    </icon-button>

    <!-- Audio -->
    <icon-button
      v-if="varieties.includes('audio')"
      :active="active == 'audio'"
      @click="onVarietyChanged('audio')"
      class="mr-6 cursor-pointer"
    >
      <template v-slot:icon>
        <svg
          class="h-5 mr-2 inline-block fill-current"
          viewBox="0 0 16 18"
        >
          <path d="M8 0a8 8 0 00-8 8v8a2 2 0 004 0v-3a2 2 0 00-2-2 2 2 0 00-1 .28V8a7 7 0 0114 0v3.28a2 2 0 00-1-.28 2 2 0 00-2 2v3a2 2 0 004 0V8a8 8 0 00-8-8zM2 12a1 1 0 011 1v3a1 1 0 01-2 0v-3a1 1 0 011-1zm13 4a1 1 0 01-2 0v-3a1 1 0 012 0v3z" />
        </svg>
      </template>

      Аудио книга
    </icon-button>

    <!-- Press -->
    <icon-button
      v-if="varieties.includes('press')"
      :active="active == 'press'"
      @click="onVarietyChanged('press')"
      class="mr-6 cursor-pointer"
    >
      <template v-slot:icon>
        <svg
          class="h-5 mr-2 inline-block fill-current"
          viewBox="0 0 19 18"
        >
          <path d="M18.5 0a23.71 23.71 0 00-9 1.84A23.71 23.71 0 00.5 0a.5.5 0 00-.5.5v15.11a.5.5 0 00.5.5A22.84 22.84 0 019.29 18a.5.5 0 00.43 0 22.84 22.84 0 018.79-1.84.5.5 0 00.5-.5V.5a.5.5 0 00-.51-.5zM1 1a23.17 23.17 0 018 1.72v14a24 24 0 00-8-1.63zm17 14.12a24 24 0 00-8 1.63v-14A23.17 23.17 0 0118 1zM2 5.15a.5.5 0 01.55-.44A18.83 18.83 0 017.7 5.95a.5.5 0 01-.39.92A18.46 18.46 0 002.45 5.7.5.5 0 012 5.15zM8 9.6a.5.5 0 01-.66.27A18.46 18.46 0 002.45 8.7a.5.5 0 11.11-1A18.83 18.83 0 017.7 8.95a.5.5 0 01.3.65zm0 3a.5.5 0 01-.66.27 18.46 18.46 0 00-4.89-1.17.5.5 0 01.11-1 18.83 18.83 0 015.14 1.25.5.5 0 01.3.65zm3-6a.5.5 0 01.26-.66 18.79 18.79 0 015.19-1.24.5.5 0 11.11 1 18.47 18.47 0 00-4.86 1.17.5.5 0 01-.7-.27zm0 3a.5.5 0 01.26-.66 18.79 18.79 0 015.19-1.24.5.5 0 11.11 1 18.47 18.47 0 00-4.86 1.17.5.5 0 01-.7-.27zm6 1.54a.5.5 0 01-.44.55 18.47 18.47 0 00-4.86 1.17.5.5 0 01-.39-.92 18.79 18.79 0 015.14-1.25.5.5 0 01.55.46z" />
        </svg>
      </template>

      Печатный вариант
    </icon-button>
  </div>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'
import IconButton from '~/components/IconButton.vue'

@Component({ components: { IconButton } })
class VarietySwitcher extends Vue {
  @Prop() readonly varieties!: string[];
  @Prop({ default: 'digital' }) readonly active!: string;

  private onVarietyChanged(variety: string) {
    this.$emit('change', variety)
  }
}

export default VarietySwitcher
</script>
