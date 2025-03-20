<template>
  <nav class="navbar">
    <div class="nav-container">
      <div class="logo">
        <router-link to="/" class="logo">
        <img src="@/assets/logo.png" alt="Sun Safe Logo" />
        </router-link>
      </div>
      <div class="hamburger" @click="toggleMenu" v-if="!isMenuActive">
        &#9776;
      </div>
      <ul class="nav-links" :class="{ 'nav-active': isMenuActive }">
        <li><router-link to="/" @click="closeMenu">Home</router-link></li>
        <li><router-link to="/uv-tracker" @click="closeMenu">UV Tracker</router-link></li>
        <li><router-link to="/resources" @click="closeMenu">Resources</router-link></li>
        <li><router-link to="/blog" @click="closeMenu">Cancer Awareness</router-link></li>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {
  data() {
    return {
      isMenuActive: false,
    };
  },
  methods: {
    toggleMenu() {
      this.isMenuActive = !this.isMenuActive;
    },
    closeMenu() {
      this.isMenuActive = false;
    },
  },
  watch: {
    // Watch for route changes to close menu and reset hamburger icon
    $route() {
      this.isMenuActive = false;
    }
  }
};
</script>

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

.hamburger {
  display: none; /* Hide hamburger by default (desktop view) */
  font-size: 24px;
  cursor: pointer;
}

.nav-links {
  display: flex;
  gap: 20px;
  list-style: none;
  margin: 0;
  padding: 5;
}

.nav-links li {
  display: flex;
  align-items: center;
}

.nav-links a {
  text-decoration: none;
  font-weight: normal;
  color: black;
  transition: color 0.3s;
}

.nav-links a.router-link-exact-active {
  color: black;
  text-decoration: underline;
  text-underline-offset: 4px;
}

/* Mobile Menu */
@media (max-width: 768px) {
  .hamburger {
    display: block;
  }
  .nav-links {
    position: absolute;
    top: 100%;
    left: 0;
    width: 100%;
    flex-direction: column;
    background-color: #fff4bc;
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.3s ease-in-out;
  }
  .nav-links.nav-active {
    max-height: 300px; /* Adjust based on the number of links */
  }
  .nav-links li {
    text-align: center;
    padding: 10px 0;
  }
}

body {
  padding-top: 80px;
}
</style>
