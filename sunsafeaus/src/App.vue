<template>
  <div id="app" class="container">
    <LandingPage />
  </div>
</template>

<script>
import LandingPage from "./components/LandingPage.vue";

export default {
  components: {
    LandingPage,
  },
};
</script>

<style>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  padding: 20px;
}
</style>