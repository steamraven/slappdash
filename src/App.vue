<template>
  <div class="text-center">
    <div class="hidden" >
      <span>{{bookmarkCount}}</span>
      <span>{{bookmarkNames}}</span>
      <span>{{trash.length}}</span>
    </div>
    <div class="pt-8">
      <draggable
        v-for="index in bookmarks.length"
        :key="index"
        v-model="bookmarks[index-1]"
        v-bind="options.bookmarks"
        @start="dragBookmark=true"
        @end="dragBookmark=false"
        @remove="cleanBookmarks"
      >
        <template #item="{element}">
          <AppButton :app-key="element" :apps="apps"></AppButton>
        </template>
      </draggable>
      <draggable
        v-model="newRow"
        v-bind="options.newRow"
        @add="addBookmark"
      >
        <template #item="{element}">
          <AppButton :app-key="element" :apps="apps"></AppButton>
        </template>
      </draggable>
      <draggable
        :class="{'dash-hidden':!showTrash}"
        v-bind="options.trash"
      >
        <template #item>
          <div class="dash-element"></div>
        </template>
      </draggable>
    </div>
    <div
      class="grid p-input-filled pt-1" 
    >
      <div class="col-8 col-offset-2 ">
        <span class="p-input-icon-left w-full" >
          <i class="pi pi-search" />
          <InputText 
            type="text" 
            autofocus 
            v-model="search" 
            class="w-full" 
            style="border-radius: 25px" 
            placeholder="Type to search; Drag app above to bookmark, or below to remove" 
          />
        </span>
      </div>
      <div class="col-8 col-offset-2 ">
        <draggable 
          v-model="results"
          v-bind="options.results"
          @start="dragResult=true"
          @end="dragResult=false"
        >
          <template #item="{element}">
            <AppButton :app-key="element" :apps="apps"></AppButton>
          </template>
        </draggable>
      </div>
    </div>

  </div>
</template>

<script src="./App.py">
</script>
<style lang="scss">
/*
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
*/

@import 'node_modules/primeflex/primeflex.scss';

body {
 background-image: url("assets/organs.jpeg");
}

.dash-hidden {
  visibility: hidden;
}

.dash-list {
  display: flex;
  flex-direction: row;
  justify-content: center;
  transition: all 5s;
}

.dash-element {
  border: solid 2px black;
  padding: 10px;
  margin: 10px;
  border-radius: 25px;
}

.dash-trash .dash-element {
  display: none;

}
.text-black {
  color: #000000 !important; 
}
.bg-black {
  background-color: #000000;
}

</style>
