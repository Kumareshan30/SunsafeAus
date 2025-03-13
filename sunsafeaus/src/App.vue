<template>
  <div id="app">
    <NavBar />
    <div class="content">
      <router-view />
    </div>
  </div>
</template>

<style>
#app {
  font-family: 'Raleway', sans-serif;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.content {
  margin-top: 80px;
  padding: 20px;
}
</style>