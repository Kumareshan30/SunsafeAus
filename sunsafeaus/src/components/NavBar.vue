<template>
  <nav class="navbar">
    <div class="nav-container">
      <div class="logo">
        <img src="@/assets/logo.png" alt="Sun Safe Logo" />
      </div>
      <ul class="nav-links">
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/uv-tracker">UV Tracker</router-link></li>
        <li><router-link to="/resources">Resources</router-link></li>
        <li><router-link to="/blog">Blog</router-link></li>
      </ul>
    </div>
  </nav>
</template>

<style scoped>
.navbar {
  width: 100%; 
  background-color: #fff4bc;
  position: fixed;
  top: 0;
  left: 0;
  padding: 15px 0;
  z-index: 1000;
}

.nav-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.logo img {
  width: 100px;
}

.nav-links {
  display: flex;
  gap: 20px;
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav-links li {
  display: flex;
  align-items: center;
}

.nav-links a {
  text-decoration: none;
  font-weight: bold;
  color: black;
  transition: color 0.3s;
}

.nav-links a.router-link-exact-active {
  color: #d97706;
}

body {
  padding-top: 80px;
}
</style>
