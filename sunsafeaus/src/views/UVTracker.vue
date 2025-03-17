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
          `http://localhost:8000/locations`,
          {
            params: {
              searchParam: this.searchQuery.trim()
            }
          }
        );

        this.searchResults = data.map(loc => ({
          location_id: `${loc.id}`,
          name: `${loc.location_name}, ${loc.state} ${loc.zipcode}`
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
          `http://localhost:8000/weather`,  
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
.uv-tracker {
  text-align: center;
  padding: 20px;
}

.search-section {
  margin: 20px 0;
}

.search-input {
  padding: 8px 12px;
  width: 300px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.loading {
  color: #666;
  margin-top: 5px;
}

.error {
  color: #e74c3c;
  margin: 10px 0;
}

.results {
  margin: 15px 0;
}

.result-select {
  padding: 8px 12px;
  width: 325px;
  border-radius: 4px;
}

.uv-gauge {
  margin: 30px auto;
}

.uv-value {
  font-size: 24px;
  font-weight: bold;
}

.uv-risk {
  color: #c0392b;
  margin-top: 10px;
}

.info-container {
  display: flex;
  justify-content: center;
  gap: 40px;
  margin-top: 30px;
}

.info-box {
  padding: 15px;
  min-width: 120px;
  background: #f8f9fa;
  border-radius: 8px;
}

.info-icon {
  width: 40px;
  height: 40px;
}

.info-label {
  font-weight: 600;
  margin: 8px 0;
}

.info-value {
  font-size: 0.9em;
  color: #666;
}
</style>