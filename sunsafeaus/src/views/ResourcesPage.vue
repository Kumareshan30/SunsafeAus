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
            :key="item.zipcode"
            @click="selectLocation(item)"
          >
            {{ item.location_name }} ({{ item.zipcode }})
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
      <h3>Reminders：</h3>
      <div class="reminder-instructions">
    <p>Don't forget to reapply Sun Scream</p>
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
import { ref } from 'vue'
import axios from 'axios'
import dayjs from 'dayjs' 
import { onUnmounted } from 'vue';
import { onMounted } from 'vue';
import { watch } from 'vue';



const form = ref({
  skin_type: '',
  skin_tone: '',
  activity_level: '',
  location: null
})


const skinTypes = [
  { value: 'oily', label: 'Oily' },
  { value: 'dry', label: 'Dry' },
  { value: 'sensitive', label: 'Sensitive' },
  { value: 'combination', label: 'Combination' }
]

const skinColors = [
  { value: 'dark', label: 'Dark', color: '#8D5524' },
  { value: 'fair', label: 'Fair', color: '#FFDBAC' },
  { value: 'olive', label: 'Olive', color: '#BAB86C' },
  { value: 'medium', label: 'Medium', color: '#C68642' }
]

const activityLevels = [
  { value: 'low', label: 'Low (0-2 hours)' },
  { value: 'median', label: 'Median (2-4 hours)' },
  { value: 'high', label: 'High (4+ hours)' }
]


const locationQuery = ref('')
const locationOptions = ref([])




const recommendation = ref({})
const error = ref('')

const reminders = ref([]) 


const now = ref(dayjs())


const searchLocations = async () => {
  if (locationQuery.value) {
    try {
      const response = await axios.get('http://localhost:8000/locations', {
        params: { searchParam: locationQuery.value }
      })
      locationOptions.value = response.data
    } catch (err) {
      console.error('fail to find location:', err)
    }
  } else {
    locationOptions.value = []
  }
}

const selectLocation = (item) => {
  form.value.location = item
  locationQuery.value = `${item.location_name} (${item.zipcode})`
  locationOptions.value = []
}

// validate
const validateForm = () => {
  return (
    form.value.skin_type &&
    form.value.skin_tone &&
    form.value.activity_level &&
    form.value.location
  )
}

// submit
const submitForm = async () => {
  error.value = ''
  recommendation.value = {}

  if (!validateForm()) {
    error.value = 'Please filled in the whole form'
    return
  }

  try {
    const payload = {
      skin_type: form.value.skin_type,
      skin_tone: form.value.skin_tone,
      activity_level: form.value.activity_level,
      location: form.value.location
    }

    const response = await axios.post('http://localhost:8000/sun_protection', payload)
    recommendation.value = response.data

  }catch (err) {
  console.error(err)
  error.value = err.response?.data?.detail || '请求失败，请稍后重试'
}
}

let timer = null
onMounted(() => {
  timer = setInterval(() => {
    now.value = dayjs()
  }, 60 * 1000) 
})

onUnmounted(() => {
  clearInterval(timer)
})

// get recommendation update
watch(recommendation, () => {
  generateReminders()
})

const generateReminders = () => {
  reminders.value = [] 

  if (!recommendation.value.reapply_frequency) return

  const freqMatch = recommendation.value.reapply_frequency.match(/(\d+)/)
  if (!freqMatch) return

  const hoursInterval = parseInt(freqMatch[1]) 
  const startTime = dayjs() 
  const endTime = dayjs().hour(18).minute(0).second(0) 

  let nextTime = startTime.add(hoursInterval, 'hour').startOf('hour')

  // get notice
  while (nextTime.isBefore(endTime)) {
    reminders.value.push(nextTime)
    nextTime = nextTime.add(hoursInterval, 'hour')
  }

}
//counter on time remain
const timeUntil = (reminderTime) => {
  const diff = reminderTime.diff(now.value, 'minute')
  if (diff <= 0) return '已过'
  if (diff < 60) return `in ${diff} minutes`
  const hours = Math.floor(diff / 60)
  const minutes = diff % 60
  return `in ${hours} hour${hours > 1 ? 's' : ''} ${minutes} minutes`
}

</script>

<style scoped>
.resources {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
  max-width: 1200px;
  margin: 0 auto;
  padding: 32px 20px;
  color: #1a202c;
}

h1 {
  font-size: 28px;
  font-weight: 700;
  margin-bottom: 32px;
  text-align: center;
  color: #2d3748;
  line-height: 1.2;
}


.container {
  display: flex;
  gap: 24px;
  justify-content: space-between;
  width: 100%; 
  max-width: 1200px; 
  margin: 0 auto; 
  padding: 20px; 
  box-sizing: border-box; 
}

.left-section, .right-section {
  background-color: #ffffff;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  overflow: hidden;
}

.left-section {
  flex: 1 1 calc(60% - 12px); 
}

.right-section {
  flex: 1 1 calc(40% - 12px); 
}

.right-section {
  flex: 1 1 35%; 
  display: flex;
  flex-direction: column;
}

.recommendation-container {
  padding: 28px;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  font-weight: 600;
  font-size: 14px;
  color: #4a5568;
}

.form-group select,
.form-group input {
  width: 100%;
  max-width: 350px;
  padding: 12px 16px;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  font-size: 15px;
  color: #2d3748;
  background-color: #f8fafc;
  transition: all 0.2s ease;
  box-sizing: border-box;
}

.form-group select:focus,
.form-group input:focus {
  outline: none;
  border-color: #cbd5e0;
  box-shadow: 0 0 0 3px rgba(203, 213, 224, 0.4);
  background-color: #ffffff;
}

.form-group select:hover,
.form-group input:hover {
  border-color: #cbd5e0;
}

.location-options {
  position: absolute;
  width: calc(100% - 56px);
  margin-top: 4px;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  background-color: #ffffff;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  max-height: 200px;
  overflow-y: auto;
  z-index: 10;
}

.location-options li {
  padding: 12px 16px;
  cursor: pointer;
  transition: background-color 0.15s ease;
  font-size: 14px;
}

.location-options li:hover {
  background-color: #f7fafc;
}

button[type="submit"] {
  width: 100%;
  padding: 14px;
  background-color: #fff4bc;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 600;
  color: #2d3748;
  cursor: pointer;
  transition: all 0.2s ease;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  margin-top: 8px;
}

button[type="submit"]:hover {
  background-color: #ffefb3;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
  transform: translateY(-1px);
}

button[type="submit"]:active {
  transform: translateY(0);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

.result-box {
  margin-top: 28px;
  padding: 24px;
  border-radius: 10px;
  background-color: #f8fafc;
  border: 1px solid #e2e8f0;
}

.result-box h3 {
  margin-top: 0;
  margin-bottom: 16px;
  font-size: 18px;
  font-weight: 600;
  color: #2d3748;
}

.recommendation-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.recommendation-item {
  display: flex;
  justify-content: space-between;
  padding: 12px 0;
  border-bottom: 1px solid #edf2f7;
  font-size: 14px;
  line-height: 1.5;
}

.recommendation-item:last-child {
  border-bottom: none;
}

.key {
  font-weight: 600;
  color: #4a5568;
  max-width: 50%;
}

.value {
  color: #2d3748;
  text-align: right;
  max-width: 50%;
}

.error-message {
  margin-top: 16px;
  padding: 12px;
  background-color: #fff5f5;
  color: #c53030;
  font-weight: 500;
  text-align: center;
  border-radius: 8px;
  border: 1px solid #fed7d7;
}

h3 {
  padding: 20px 28px;
  margin: 0;
  border-bottom: 1px solid #edf2f7;
  font-size: 18px;
  font-weight: 600;
  color: #2d3748;
  background-color: #f8fafc;
}

.reminder-content {
  padding: 20px;
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}

.reminder-container {
  flex-grow: 1;
}

.reminder-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.reminder-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 14px 10px;
  border-bottom: 1px solid #edf2f7;
  transition: background-color 0.15s ease;
}

.reminder-item:last-child {
  border-bottom: none;
}

.reminder-item:hover {
  background-color: #f7fafc;
}

.reminder-time {
  font-weight: 600;
  color: #4a5568;
  font-size: 16px;
}

.reminder-countdown {
  color: #718096;
  font-size: 14px;
}

.no-reminders {
  text-align: center;
  color: #718096;
  padding: 40px 20px;
  font-size: 14px;
}

.reminder-instructions p {
  margin: 0;
  line-height: 1.5;
  font-size: 12px;

}
</style>
