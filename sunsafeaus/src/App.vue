<template>
  <div id="app">
    <NavBar />
    <div class="content">
      <router-view />
    </div>
  </div>
</template>

<script>
import NavBar from "./components/NavBar.vue";

export default {
  components: {
    NavBar,
  },
};
</script>

<style>
#app {
  font-family: 'Raleway', sans-serif;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.content {
  margin-top: 20px;
  padding: 20px;
}
</style>