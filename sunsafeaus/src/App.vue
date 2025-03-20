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
  padding: 0; 
  margin: 0;
}

.content {
  margin-top: 20px;
  padding: 20px;
  padding-top: 80px;
}
</style>