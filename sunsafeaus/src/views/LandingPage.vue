<template>
  <div class="landing-page">
    <section class="about-section">
      <div class="about-text">
        <h2>About Sun Safe Aus</h2>
        <p>
          We are a bunch of tech enthusiasts who wish to contribute to the growing concerns
          about Australia’s sun protection habits and its UV exposure dangers.
        </p>
        <button class="read-more">Read more</button>
      </div>
      <div class="about-image">
        <img src="@/assets/home.png" alt="Sun Safe Illustration" />
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: "LandingPage",
};
</script>

<style>
.landing-page {
  padding: 100px 40px;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}

.about-section {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1000px;
  margin: auto;
}

.about-text {
  max-width: 500px;
  text-align: left;
}

.about-text h2 {
  font-size: 2rem;
  font-weight: bold;
}

.about-text p {
  font-size: 1.2rem;
  margin: 15px 0;
}

.read-more {
  background-color: #fff4bc;
  padding: 10px 15px;
  border: none;
  font-size: 1rem;
  cursor: pointer;
}

.about-image img {
  max-width: 350px;
}
</style>