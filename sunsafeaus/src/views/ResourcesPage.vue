<template>
    <div class="resources-page">
      <h1>Your Sun Safety Guide</h1>
      <p class="description">
        Stay protected under the sun with personalized recommendations tailored to your skin type and environment.
        Use this guide to find the right sunscreen for your needs.
      </p>
  
      <!-- Sunscreen Matching Section -->
      <div class="sunscreen-section">
        <h3>A. Find your perfect sunscreen match</h3>
        <div class="field-group">
          <label>Skin Tone <input type="text" placeholder="Dark" /></label>
          <label>UV Index <input type="text" placeholder="13.1" /></label>
          <label>Estimated duration of exposure <input type="text" placeholder="5 hours" /></label>
          <button class="calculate-btn">Calculate</button>
        </div>
        <p>→ Your recommended sunscreen is SPF 50+. Apply 2 teaspoons of sunscreen while reapplying every 2 hours.</p>
      </div>
  
      <!-- Dressing Smart Section -->
      <div class="dressing-smart">
        <h3>B. Dressing Smart for the Sun</h3>
        <label>Enter your UV Index: <input type="text" placeholder="13.1" /></label>
        <button class="go-btn">Go</button>
        <p>*Output*</p>
      </div>
  
      <!-- Sunscreen Reminder -->
      <div class="reminder-section">
        <div class="reminder-box">
          <p>Set Sunscreen Reminders</p>
          <button class="add-reminder">+</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "ResourcesPage",
  };
  </script>
  
  <style scoped>
  .resources-page {
    text-align: left;
    padding: 20px;
    max-width: 900px;
    margin: auto;
  }
  
  .description {
    font-size: 16px;
    margin-bottom: 20px;
  }
  
  .field-group {
    display: flex;
    flex-direction: column;
    max-width: 400px;
  }
  
  .field-group label {
    margin: 8px 0;
  }
  
  input {
    width: 100%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  .calculate-btn, .go-btn {
    margin-top: 10px;
    padding: 8px 12px;
    background-color: #f7e49b;
    border: 1px solid #999;
    cursor: pointer;
  }
  
  .calculate-btn:hover, .go-btn:hover {
    background-color: #ffd966;
  }
  
  .reminder-section {
    display: flex;
    justify-content: flex-end;
    margin-top: 20px;
  }
  
  .reminder-box {
    background: #f7e49b;
    border: 1px solid #999;
    padding: 10px;
    width: 200px;
    text-align: center;
  }
  
  .add-reminder {
    display: block;
    margin-top: 10px;
    font-size: 18px;
    font-weight: bold;
    background: white;
    border: 1px solid #999;
    cursor: pointer;
  }
  </style>  