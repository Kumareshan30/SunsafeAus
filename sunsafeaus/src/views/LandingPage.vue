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
}

/* Overlay (DESKTOP VIEW - Old Design) */
.overlay {
  position: absolute;
  top: 65%;
  left: 5%;
  transform: translateY(-50%);
  color: black;
  text-align: left;
  max-width: 380px;
}

/* Heading */
.overlay h2 {
  font-size: 2rem;
  font-weight: bold;
  line-height: 1.2;
  margin-bottom: 15px;
}

/* Highlighted Text */
.highlight {
  color: #ff9800; /* Makes "SunSafeAus" stand out */
}

/* Paragraph */
.overlay p {
  font-size: 1rem;
  margin-bottom: 20px; /* Added spacing */
}

/* Button */
.read-more {
  background-color: #fff4bc;
  padding: 12px 18px;
  border: none;
  font-size: 1rem;
  font-weight: bold;
  cursor: pointer;
  border-radius: 8px;
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s ease-in-out;
  margin-top: 20px; /* Extra space from text */
}

.read-more:hover {
  background-color: #f6e8b3;
}

/* ✅ Mobile View Adjustments */
@media screen and (max-width: 768px) {
  .image-container {
    flex-direction: column;
    text-align: center;
  }

  .background-image {
    width: 100%;
    margin-bottom: 20px; /* Added space between image and text */
  }

  .overlay {
    position: relative;
    top: auto;
    left: auto;
    transform: none;
    max-width: 90%;
    padding: 15px;
    text-align: center;
  }

  .overlay h2 {
    font-size: 1.8rem;
  }

  .overlay p {
    font-size: 0.9rem;
    margin-bottom: 20px;
  }

  .read-more {
    font-size: 0.9rem;
    padding: 10px 16px;
    margin-top: 20px; /* More spacing */
  }
}
</style>
