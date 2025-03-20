<template>
  <div class="landing-page">
    <div class="image-container">
      <div class="overlay">
        <h2>About <span class="highlight">SunSafeAus</span></h2>
        <p>
          We are a bunch of tech enthusiasts who wish to contribute to the growing concerns
          about Australia’s sun protection habits and its UV exposure dangers.
        </p>
        <button class="read-more" @click="goToResources">Plan Your Safety</button>
      </div>
            <img src="@/assets/home.png" alt="Sun Safe Illustration" class="background-image" />
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
/* Parent Container */
.landing-page {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: calc(100vh - 80px);
  padding: 20px;
}

/* Image Container */
.image-container {
  position: relative;
  width: 100%;
  max-width: 1200px;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Background Image */
.background-image {
  width: 100%;
  height: auto;
  object-fit: cover;
  display: block;
  margin-bottom: 20px;
}

.overlay {
  position: absolute;
  top: 60%;
  left: 2%;
  transform: translateY(-50%);
  color: black;
  text-align: left;
  max-width: 350px;
}

.overlay h2 {
  font-size: 2rem;
  font-weight: bold;
  line-height: 1.2;
  margin-bottom: 15px;
}

.highlight{
  border-radius: 1em 0 1em 0;
  background-image: linear-gradient(
    -75deg,
    rgba(255, 224, 0, 0.2),
    rgba(255, 224, 0, 0.7) 95%,
    rgba(255, 224, 0, 0.1)
  );
}

.overlay p {
  font-size: 1rem;
  margin-bottom: 20px;
}

.read-more {
  background-color: #fff4bc;
  padding: 12px 18px;
  border: none;
  font-size: 1rem;
  font-weight: normal;
  cursor: pointer;
  border-radius: 8px;
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s ease-in-out;
  margin-top: 5px;
}

.read-more:hover {
  background-color: #f6e8b3;
}

@media screen and (max-width: 768px) {
  .image-container {
    display: flex;
    flex-direction: column-reverse;
    align-items: start;
  }

  .overlay {
    position: relative;
    top: 15%;
    left: 0;
    transform: translateY(-20%);
    max-width: 90%;
    text-align: left;
  }

  .highlight {
    background-image: linear-gradient(
      -100deg,
      rgba(255, 224, 0, 0.1),
      rgba(255, 224, 0, 0.5) 80%,
      rgba(255, 224, 0, 0.05)
    );
  }

  .highlight {
    background-image: linear-gradient(
      -100deg,
      rgba(255, 224, 0, 0.1),
      rgba(255, 224, 0, 0.5) 80%,
      rgba(255, 224, 0, 0.05)
    );
  }
  .overlay h2 {
    font-size: 1.8rem;
    margin-left: -30px;
  }

  .overlay p {
    font-size: 0.9rem;
    margin-bottom: 5px;
    max-width: 70%;
    margin-left: -30px;
  }

  .read-more {
    font-size: 0.9rem;
    margin-top: 5px;
    margin-left: -35px;
  }

  .background-image {
  width: 100vw;
  height: 125%;
  object-fit: cover;
  position: absolute;
  top: -26%;
  left: -10%;
  z-index: -1;
}
}
</style>

