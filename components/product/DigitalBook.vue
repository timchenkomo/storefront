<template functional>
  <!-- Download sample -->
  <div
    class="bg-blue-500 rounded text-white text-center px-4 py-2 my-1 md:mr-2 text-sm"
  >
    Образец

    <a
      v-for="url in props.data.urls"
      :key="url.ext"
      :href="'/download/' + props.group.slug + '/sample_' + url.url"
      class="hover:text-blue-200"
      download
    >
      {{ url.ext.toUpperCase() }}
    </a>
  </div>
</template>
