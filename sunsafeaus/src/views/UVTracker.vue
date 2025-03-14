<template>
    <div class="uv-tracker">
      <h1>How is the UV doing mate?</h1>
      
      <!-- UV Gauge -->
      <div class="uv-gauge">
        <UvGauge :uv-value="uvIndex" :size="300" />
        <p class="uv-value">{{ uvIndex }}</p>
        <p class="uv-risk">{{ uvRisk }}</p>
      </div>
  
      <!-- Weather, Air Quality, Wind Information -->
      <div class="info-container">
        <div class="info-box">
          <img src="@/assets/weather.png" alt="Weather Icon" class="info-icon" />
          <p class="info-label">Weather</p>
          <p class="info-value">{{ weather }}°C</p>
        </div>
        
        <div class="info-box">
          <img src="@/assets/AQ.png" alt="Air Quality Icon" class="info-icon" />
          <p class="info-label">Air Quality</p>
          <p class="info-value">{{ airQuality }}</p>
        </div>
  
        <div class="info-box">
          <img src="@/assets/wind.png" alt="Wind Icon" class="info-icon" />
          <p class="info-label">Wind</p>
          <p class="info-value">{{ windSpeed }} kmph</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { ref, computed } from 'vue';
  import UvGauge from '@/components/UVGauge.vue';
  
  export default {
    name: "UVTracker",
    components: {
      UvGauge,
    },
    setup() {
      // Simulated data
      const uvIndex = ref(13.1);
      const weather = ref(23); // in °C
      const airQuality = ref(101);
      const windSpeed = ref(7); // in kmph
  
      // Compute UV risk level based on the index
      const uvRisk = computed(() => {
        if (uvIndex.value < 3) return "Low UV exposure";
        if (uvIndex.value < 6) return "Moderate UV exposure";
        if (uvIndex.value < 8) return "High UV exposure";
        return "Very High UV exposure";
      });
  
      return { uvIndex, weather, airQuality, windSpeed, uvRisk };
    }
  };
  </script>
  
  <style scoped>
  .uv-tracker {
    text-align: center;
    padding: 20px;
  }
  
  .uv-gauge {
    margin: 20px auto;
  }
  
  .uv-value {
    font-size: 24px;
    font-weight: bold;
  }
  
  .uv-risk {
    font-size: 18px;
    color: brown;
    text-decoration: underline;
  }
  
  .info-container {
    display: flex;
    justify-content: center;
    gap: 50px;
    margin-top: 20px;
  }
  
  .info-box {
    text-align: center;
  }
  
  .info-icon {
    width: 50px;
    height: 50px;
  }
  
  .info-label {
    font-size: 16px;
    font-weight: bold;
  }
  
  .info-value {
    font-size: 14px;
  }
  </style>  