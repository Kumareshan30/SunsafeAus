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
  padding: 20px; 
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
  width: 110%;
  height: auto;
  object-fit: cover;
  display: block;
  margin-left: 5%;
}

.overlay {
  position: absolute;
  top: 65%;
  left: 5%; 
  transform: translateY(-50%);
  color: black;
  text-align: left;
  max-width: 380px;
}

.overlay h2 {
  font-size: 2rem;
  font-weight: bold;
  line-height: 1.2;
}

.overlay p {
  font-size: 1rem;
  margin: 15px 0;
}

.read-more {
  background-color: #fff4bc;
  padding: 10px 16px;
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

@media screen and (max-width: 768px) {
  .image-container {
    flex-direction: column;
    text-align: center;
  }

  .background-image {
    width: 100%;
    margin-left: 0;
  }

  .overlay {
    position: absolute;
    top: 35%;
    left: 10%;
    transform: translateY(-50%);
    max-width: 80%;
  }

  .overlay h2 {
    font-size: 1.8rem;
  }

  .overlay p {
    font-size: 0.9rem;
  }

  .read-more {
    font-size: 0.9rem;
    padding: 8px 14px;
  }
}
</style>