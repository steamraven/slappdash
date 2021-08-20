<template>
  <draggable
    :list="items"
    :group="{name: 'bookmarked', pull: 'clone', put: false}"
    item-key="name"
    class="list"
    animation=200
    :sort="false"
    >
    <template #item="{element}">
      <div class="element">{{element.name}}</div>
    </template>
  </draggable>
</template>

<script lang="py">
  draggable = require("vuedraggable")
  exports['default'] = {
    "name": "ResultList",
    "components": {
      "draggable": draggable
    },
    "props": {
      "items": Array

    }
  }
</script>