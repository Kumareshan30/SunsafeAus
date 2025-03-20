<template>
  <div class="uv-tracker">
    <h1>How is the UV doing mate?</h1>
    
    <div class="search-section">
      <input
        v-model="searchQuery"
        @input="handleSearchInput"
        placeholder="Enter suburb or postcode"
        class="search-input"
      />
      <div v-if="isSearching" class="loading">Searching...</div>
    </div>

    <div v-if="searchResults.length > 0" class="results">
      <select 
        v-model="selectedResult" 
        @change="handleSelection" 
        class="result-select"
      >
        <option disabled value="">Please select one</option>
        <option 
          v-for="result in searchResults" 
          :key="result.id" 
          :value="result"
        >
          {{ result.name }}
        </option>
      </select>
    </div>

    <div v-if="errorMessage && searchQuery.trim()" class="error">
      {{ errorMessage }}
    </div>

    <div class="uv-gauge">
      <UvGauge :uv-value="uvIndex" :size="300" />
    </div>
    
    <div class="info-container">
      <div class="info-box">
        <img src="@/assets/weather.png" alt="Weather Icon" class="info-icon" />
        <p class="info-label">Weather</p>
        <p class="info-value">{{ weather }}°C</p>
      </div>
      
      <div class="info-box">
        <img src="@/assets/AQ.png" alt="humidity Icon" class="info-icon" />
        <p class="info-label">humidity</p>
        <p class="info-value">{{ humidity }}</p>
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
import axios from 'axios';

const debounce = (fn, delay = 500) => {
  let timeoutId;
  return (...args) => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => fn(...args), delay);
  };
};

export default {
  name: "UVTracker",
  components: {
    UvGauge,
  },
  setup() {
    const uvIndex = ref(0);
    const weather = ref(0);
    const humidity = ref(0);
    const windSpeed = ref(0);

    const uvRisk = computed(() => {
      if (uvIndex.value < 3) return "Low UV exposure";
      if (uvIndex.value < 6) return "Moderate UV exposure";
      if (uvIndex.value < 8) return "High UV exposure";
      return "Very High UV exposure";
    });

    return { uvIndex, weather, humidity, windSpeed, uvRisk };
  },
  data() {
    return {
      searchQuery: '',
      searchResults: [],
      selectedResult: null,
      errorMessage: '',
      isSearching: false
    };
  },
  created() {
    this.searchDebounce = debounce(this.searchSuburbs);
  },
  methods: {
    handleSearchInput() {
      this.clearState();
      if (this.searchQuery.trim().length >= 2) {
        this.isSearching = true;
        this.searchDebounce();
      }
    },

    async searchSuburbs() {
      try {
        const { data } = await axios.get(
          `https://aussafebackend.onrender.com/locations`,
          {
            params: {
              search_param: this.searchQuery.trim()
            }
          }
        );

        this.searchResults = data.map(loc => ({
          location_id: `${loc.id}`,
          name: `${loc.locality}, ${loc.state} ${loc.postcode}`
        }));

        this.errorMessage = data.length ? '' : 'Cannot find Suburb/Postcode';
      } catch (error) {
        this.errorMessage = 'Search service unavailable';
        console.error('Search error:', error);
      } finally {
        this.isSearching = false;
      }
    },

    async handleSelection() {
      if (!this.selectedResult) return;

      try {
        const  response  = await axios.get(
          `https://aussafebackend.onrender.com/weather`,  
          {
            params: {
              location_id: this.selectedResult.location_id
            }
          }
        );
        const weatherData = response.data.data;
        const fToC = (f) => ((f - 32) * 5/9).toFixed(1);
        this.uvIndex = weatherData.uvIndex;
        this.weather = fToC(weatherData.temperature);
        this.windSpeed = (weatherData.windSpeed * 1.60934).toFixed(1);
        this.humidity = weatherData.humidity;

      } catch (error) {
        console.error('Weather data error:', error.response || error);
        this.errorMessage = error.response?.data?.detail 
          || 'Failed to load weather data';
        
        this.uvIndex = 0;
        this.weather = 0;
        this.humidity = 0;
        this.windSpeed = 0;
      }
    },

    clearState() {
      this.searchResults = [];
      this.selectedResult = null;
      this.errorMessage = '';
    }
  }
};
</script>

<style scoped>
/* Container */
.uv-tracker {
  text-align: center;
  padding: 20px;
  background: transparent;
  max-width: 800px;
  margin: 0 auto;
}

/* Search Bar */
.search-section {
  margin: 20px 0;
}

.search-input {
  padding: 12px 15px;
  width: 100%;  /* Make it responsive */
  max-width: 400px;
  border: 2px solid #ddd;
  border-radius: 6px;
  text-align: center;
  font-size: 16px;
  transition: border 0.3s ease-in-out;
}

.search-input:focus {
  border: 2px solid #ffd700;
  outline: none;
}

.loading {
  color: #666;
  margin-top: 5px;
}

/* Error Message */
.error {
  color: #e74c3c;
  margin: 10px 0;
  font-size: 14px;
}

/* Dropdown Results */
.results {
  margin: 15px 0;
}

.result-select {
  padding: 8px 12px;
  width: 100%;
  max-width: 325px;
  border-radius: 4px;
}

/* UV Gauge Section */
.uv-gauge {
  background: transparent;
  border-radius: 10px;
  padding: 20px;
  box-shadow: none;
  display: flex;
  justify-content: center;
  align-items: center;
}

.uv-gauge svg {
  max-width: 100%;
  height: auto;
}

/* UV Risk Indicator */
.uv-value {
  font-size: 24px;
  font-weight: bold;
}

.uv-risk {
  font-size: 1.2rem;
  font-weight: bold;
  color: #e74c3c;
}

/* Info Section */
.info-container {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap; 
  gap: 20px;
  margin-top: 20px;
}

/* Individual Info Box */
.info-box {
  padding: 15px;
  width: 120px; /* Adjust for mobile */
  background: #ffffff;
  border-radius: 10px;
  text-align: center;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.info-icon {
  width: 50px;
  height: 50px;
}

.info-label {
  font-weight: 600;
  margin: 8px 0;
}

.info-value {
  font-size: 0.9em;
  color: #666;
}

/* Mobile Responsiveness */
@media screen and (max-width: 768px) {
  .search-input {
    width: 90%;
  }

  .uv-gauge {
    padding: 10px;
  }

  .info-container {
    flex-direction: column;
    align-items: center;
  }

  .info-box {
    width: 80%;
    margin-bottom: 10px;
  }
}
</style>