<template>
  <div class="landing-page">
    <div class="logo-bar">
      <img src="@/assets/logo.png" alt="Logo" class="logo" />
    </div>
    
    <div class="header">
      <img src="@/assets/sun.png" alt="Sun Icon" class="sun-icon" />
      <h1 class="heading">The Hidden Cost of Sunshine: Australia’s Growing UV Threat</h1>
    </div>
    
    <p class="description">Add data analysis and visualisation of Impacts of UV</p>
    
    <section class="uv-exposure">
      <h2>Know the UV exposure around you</h2>
      <label>Search your location: <input type="text" placeholder="....." /></label>
      <p>Tracker output</p>
    </section>
    
    <section class="sun-safety-guide">
      <h2>Your Sun Safety Guide</h2>
      <p>Stay protected under the sun with personalized recommendations tailored to your skin type and environment. Use this guide to find the right sunscreen for your needs.</p>
      
      <h3>A. Find your perfect sunscreen match</h3>
        <div class="field-group">
          <label>Skin Tone <input type="text" placeholder="Dark" /></label>
          <label>UV Index <input type="text" placeholder="13.1" /></label>
          <label>Estimated duration of exposure <input type="text" placeholder="5 hours" /></label>
          <button class="calculate-btn">Calculate</button>
        </div>
      
      <p>→ Your recommended sunscreen is SPF 50+. Apply 2 teaspoons of sunscreen while reapplying every 2 hours.</p>
      
      <h3>B. Dressing Smart for the Sun</h3>
      <div class="field-group">
        <label>Enter your UV index: <input type="text" placeholder="13.1" /></label>
        <button class="go-btn">Go</button>
      </div>
      <p>→ Output</p>
    </section>
  </div>
</template>

<script>
export default {
  name: "LandingPage",
};
</script>

<style>
.logo-bar {
  width: 100%;
  max-width: 100%;
  margin: 0;
  padding: 5px 0;
  background-color: #fff4bc;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
}

.logo {
  width: 80px;
  height: auto;
}

.header {
  display: flex;
  align-items: baseline;
  justify-content: center;
  gap: 1px;
}

.heading {
  font-size: 2rem;
  font-weight: bold;
}

.sun-icon {
  width: 75px;
  height: auto;
  align-self: center;
}

.main-heading, .description {
  text-align: justify;
}

.sun-safety-guide {
  text-align: left;
}

.sun-safety-guide label {
  margin-left: 1rem;
}

.sun-safety-guide label, 
.sun-safety-guide input, 
.sun-safety-guide select, 
.sun-safety-guide textarea {
  display: block;
  text-align: left;
  margin: 0.25em 0;
}

.sun-safety-guide .field-group {
  margin-left: 1rem;
}

.sun-safety-guide .calculate-btn, 
.sun-safety-guide .go-btn {
  padding: 8px 12px; 
  font-size: 14px; 
  font-weight: bold;
  border: 1px solid #999;
  cursor: pointer;
  transition: background-color 0.3s ease-in-out;
}

.sun-safety-guide .calculate-btn:hover, 
.sun-safety-guide .go-btn:hover {
  background-color: #ffd966;
}

.landing-page {
  max-width: 1000px;
  width: 100%;
  margin: 0 auto;
  text-align: center;
}

.uv-exposure {
  background-color: #fff4bc;
  padding: 20px;
  border-radius: 8px;
  margin-top: 5px;
}

.uv-exposure p {
  margin-bottom: 5px;
}
</style>