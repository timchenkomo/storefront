<template functional>
  <div
    v-if="props.visible"
    @click="listeners.close"
    class="fixed flex inset-0 w-full h-screen items-center justify-center"
  >
    <!-- Modal dialog -->
    <div class="w-full max-w-xl bg-white shadow-lg rounded-lg p-4">
      <!-- Title -->
      <h3 class="text-xl">
        {{ props.title }}
        <span @click="listeners.close" class="float-right cursor-pointer">
          <close-icon class="w-4 h-4" />
        </span>
      </h3>
      <hr>

      <!-- List of formats -->
      <ul class="mt-4">
        <a
          v-for="(opt, idx) in props.options"
          :href="opt.url"
          :key="idx"
          class="cursor-pointer"
        >
          <li class="hover:bg-blue-500 rounded px-4 py-1 my-1 hover:text-white">
            Скачать
            <span class="uppercase">{{ opt.ext }}</span>
            <span class="text-xs text-gray-500">{{ opt.size }}</span>
          </li>
        </a>
      </ul>
    </div>
  </div>
</template>
