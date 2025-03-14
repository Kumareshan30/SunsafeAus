<template>
  <div class="landing-page">
    <div class="image-container">
      <img src="@/assets/home.png" alt="Sun Safe Illustration" class="background-image" />
      <div class="overlay">
        <h2>About Sun Safe Aus</h2>
        <p>
          We are a bunch of tech enthusiasts who wish to contribute to the growing concerns
          about Australia’s sun protection habits and its UV exposure dangers.
        </p>
        <button class="read-more" @click="goToResources">Plan Your Safety</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LandingPage",
  methods: {
    goToResources() {
      this.$router.push("/resources");
    },
  },
};
</script>

<style scoped>
.landing-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: calc(100vh - 80px);
  position: relative;
}

.image-container {
  position: relative;
  width: 100%;
  max-width: 1200px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.background-image {
  width: 120%;
  height: auto;
  object-fit: cover;
  display: block;
  margin-left: 10%;
}

.overlay {
  position: absolute;
  top: 60%;
  left: -3%;
  transform: translateY(-50%);
  color: black;
  text-align: left;
  max-width: 420px;
}

.overlay h2 {
  font-size: 2.4rem;
  font-weight: bold;
  line-height: 1.2;
}

.overlay p {
  font-size: 1.1rem;
  margin: 20px 0;
}

.read-more {
  background-color: #fff4bc;
  padding: 12px 18px;
  border: none;
  font-size: 1rem;
  font-weight: bold;
  cursor: pointer;
  border-radius: 5px;
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s ease-in-out;
}

.read-more:hover {
  background-color: #f6e8b3;
}
</style>