<template>
  <div class="resources">
    <h1>Get Your Personalized Recommendation For Sun Safety</h1>
    <div class="container">
      <div class="left-section">
        <div class="recommendation-container">
          <form @submit.prevent="submitForm">
            <!-- skin_type -->
            <div class="form-group">
              <label for="skin-type">Skin Type:</label>
              <select id="skin-type" v-model="form.skin_type" required>
                <option value="" disabled>Please choose</option>
                <option v-for="type in skinTypes" :key="type.value" :value="type.value">
                  {{ type.label }}
                </option>
              </select>
            </div>

            <!-- skin_tone -->
            <div class="form-group">
              <label for="skin-color">Skin Color:</label>
              <select id="skin-color" v-model="form.skin_tone" required>
                <option value="" disabled>Please choose</option>
                <option v-for="color in skinColors" :key="color.value" :value="color.value">
                  {{ color.label }}
                </option>
              </select>
            </div>

            <!-- activity_level -->
            <div class="form-group">
              <label for="activity-level">Activity Level:</label>
              <select id="activity-level" v-model="form.activity_level" required>
                <option value="" disabled>Please choose</option>
                <option v-for="level in activityLevels" :key="level.value" :value="level.value">
                  {{ level.label }}
                </option>
              </select>
            </div>

            <!-- location search -->
            <div class="form-group">
              <label for="location">Location:</label>
              <input
                id="location"
                type="text"
                v-model="locationQuery"
                @input="searchLocations"
                placeholder="Please enter Postcode/Suburb"
                required
              />
              <ul v-if="locationOptions.length" class="location-options">
                <li
                  v-for="item in locationOptions"
                  :key="item"
                  @click="selectLocation(item)"
                >
                  {{ item.locality }} ({{ item.postcode }})
                </li>
              </ul>
            </div>

            <button type="submit">Get Recommendation</button>
          </form>

          <!-- Recommendation -->
          <div class="result-box">
            <h3>Recommendation</h3>
            <ul class="recommendation-list">
              <li v-for="(value, key) in recommendation" :key="key" class="recommendation-item">
                <span class="key">{{ key.replace(/_/g, ' ') }}:</span>
                <span class="value">{{ value }}</span>
              </li>
            </ul>
          </div>

          <div v-if="error" class="error-message">
            {{ error }}
          </div>
        </div>
      </div>

      <div class="right-section">
        <h3>Reminders:</h3>
        <div class="reminder-instructions">
          <p>Don't forget to reapply Sun Screen</p>
        </div>
        <ul class="reminder-list">
          <li v-for="(time, index) in reminders" :key="index" class="reminder-item">
            <span class="time">{{ time.format('HH:mm') }}</span>
            <span class="countdown">{{ timeUntil(time) }}</span>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue';
import axios from 'axios';
import dayjs from 'dayjs';

const form = ref({
  skin_type: '',
  skin_tone: '',
  activity_level: '',
  location: null
});

const skinTypes = [
  { value: 'oily', label: 'Oily' },
  { value: 'dry', label: 'Dry' },
  { value: 'sensitive', label: 'Sensitive' },
  { value: 'combination', label: 'Combination' }
];

const skinColors = [
  { value: 'dark', label: 'Dark' },
  { value: 'fair', label: 'Fair' },
  { value: 'olive', label: 'Olive' },
  { value: 'medium', label: 'Medium' }
];

const activityLevels = [
  { value: 'low', label: 'Low (0-2 hours)' },
  { value: 'medium', label: 'Medium (2-4 hours)' },
  { value: 'high', label: 'High (4+ hours)' }
];

const locationQuery = ref('');
const locationOptions = ref([]);
const recommendation = ref({});
const error = ref('');
const reminders = ref([]);
const now = ref(dayjs());

const searchLocations = async () => {
  if (locationQuery.value) {
    try {
      const response = await axios.get('https://aussafebackend.onrender.com/locations', {
        params: { search_param: locationQuery.value }
      });
      locationOptions.value = response.data;
    } catch (err) {
      console.error('Failed to find location:', err);
    }
  } else {
    locationOptions.value = [];
  }
};

const selectLocation = (item) => {
  form.value.location = item;
  locationQuery.value = `${item.locality} (${item.postcode})`;
  locationOptions.value = [];
  console.log('Selected location:', form.value.location);
};

const validateForm = () => {
  return (
    form.value.skin_type &&
    form.value.skin_tone &&
    form.value.activity_level &&
    form.value.location
  );
};

const submitForm = async () => {
  error.value = '';
  recommendation.value = {};

  if (!validateForm()) {
    error.value = 'Please fill in the entire form';
    return;
  }

  try {
    const payload = {
      skin_type: form.value.skin_type,
      skin_tone: form.value.skin_tone,
      activity_level: form.value.activity_level,
      location: form.value.location
    };

    const response = await axios.post('https://aussafebackend.onrender.com/sun_protection', payload);
    recommendation.value = response.data;
  } catch (err) {
    console.error(err);
    error.value = err.response?.data?.detail || 'Failed to request, try again later';
  }
};

let timer = null;
onMounted(() => {
  timer = setInterval(() => {
    now.value = dayjs();
  }, 60 * 1000);
});

onUnmounted(() => {
  clearInterval(timer);
});

watch(recommendation, () => {
  generateReminders();
});

const generateReminders = () => {
  reminders.value = [];

  if (!recommendation.value.reapply_frequency) return;

  const freqMatch = recommendation.value.reapply_frequency.match(/(\d+)/);
  if (!freqMatch) return;

  const hoursInterval = parseInt(freqMatch[1]);
  const startTime = dayjs
::contentReference[oaicite:0]{index=0}
 
