<template>
  <div class="resources">
    <h1>Get Your Personalized Recommendation for Sun Safety</h1>
    
    <div class="container">
      <!-- Left Section (Form) -->
      <div class="left-section">
        <div class="recommendation-container">
          <form @submit.prevent="submitForm">
            <!-- Skin Type -->
            <div class="form-group">
              <label for="skin-type">Skin Type:</label>
              <select id="skin-type" v-model="form.skin_type" required>
                <option value="" disabled>Please choose</option>
                <option v-for="type in skinTypes" :key="type.value" :value="type.value">
                  {{ type.label }}
                </option>
              </select>
            </div>

            <!-- Skin Tone -->
            <div class="form-group">
              <label for="skin-color">Skin Color:</label>
              <select id="skin-color" v-model="form.skin_tone" required>
                <option value="" disabled>Please choose</option>
                <option v-for="color in skinColors" :key="color.value" :value="color.value">
                  {{ color.label }}
                </option>
              </select>
            </div>

            <!-- Activity Level -->
            <div class="form-group">
              <label for="activity-level">Activity Level:</label>
              <select id="activity-level" v-model="form.activity_level" required>
                <option value="" disabled>Please choose</option>
                <option v-for="level in activityLevels" :key="level.value" :value="level.value">
                  {{ level.label }}
                </option>
              </select>
            </div>

            <!-- Location Search -->
            <div class="form-group">
              <label for="location">Location:</label>
              <input
                id="location"
                type="text"
                v-model="locationQuery"
                @input="searchLocations"
                placeholder="Enter Postcode/Suburb"
                required
              />
              <ul v-if="locationOptions.length" class="location-options">
                <li v-for="item in locationOptions" :key="item" @click="selectLocation(item)">
                  {{ item.locality }} ({{ item.postcode }})
                </li>
              </ul>
            </div>

            <!-- Submit Button -->
            <button type="submit" class="read-more">Get Recommendation</button>
          </form>

          <!-- Recommendation Box -->
          <div class="result-box">
            <h3>Your Recommendation</h3>
            <ul class="recommendation-list">
              <li v-for="(value, key) in recommendation" :key="key" class="recommendation-item">
                <span class="key">{{ key.replace(/_/g, ' ') }}:</span>
                <span class="value" v-if="key === 'reapply_frequency'">{{ formatReapplyFrequency(value) }}</span>
                <span class="value" v-else>{{ value }}</span>
              </li>
            </ul>
          </div>

          <!-- Error Message -->
          <div v-if="error" class="error-message">
            {{ error }}
          </div>
        </div>
      </div>

      <!-- Right Section (Reminders) -->
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
      <button v-if="reminders.length > 0" @click="downloadICSFile" class="download-button">
    Download Reminders (.ics)
  </button>
    </div>
  </div>
  <div v-if="showPopup" class="popup-overlay">
    <div class="popup-content">
      <p>It's time to reapply sunscreen!</p>
      <button @click="closePopup">Close</button>
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


const debounce = (fn, delay = 500) => {
  let timeoutId;
  return (...args) => {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => fn(...args), delay);
  };
};

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
  { value: 'medium', label: 'Medium (2-4 hours)' },
  { value: 'high', label: 'High (4+ hours)' }
]


const locationQuery = ref('')
const locationOptions = ref([])




const recommendation = ref({})
const error = ref('')

const reminders = ref([]) 


const now = ref(dayjs())
const showPopup = ref(false)


const searchLocations = debounce(async () => {
  if (locationQuery.value) {
    try {
      const response = await axios.get('https://aussafebackend.onrender.com/locations', {
        params: { search_param: locationQuery.value }
      });
      locationOptions.value = response.data;
    } catch (err) {
      console.error('fail to find location:', err);
    }
  } else {
    locationOptions.value = [];
  }
}, 300);

const selectLocation = (item) => {
  form.value.location = item
  locationQuery.value = `${item.locality} (${item.postcode})`
  locationOptions.value = []
  console.log('Selected location:', form.value.location)
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

    const response = await axios.post('https://aussafebackend.onrender.com/sun_protection', payload)
    recommendation.value = response.data

  }catch (err) {
  console.error(err)
  error.value = err.response?.data?.detail || 'Fail to request, Try again later'
}
}

let timer = null
onMounted(() => {
  timer = setInterval(() => {
    now.value = dayjs()
  }, 10 * 1000) 
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
  if (diff <= 0) return 'pass'
  if (diff < 60) return `in ${diff} minutes`
  const hours = Math.floor(diff / 60)
  const minutes = diff % 60
  return `in ${hours} hour${hours > 1 ? 's' : ''} ${minutes} minutes`
}

const checkReminders = () => {
  const currentTime = dayjs()
  const activeReminder = reminders.value.find(reminder => {
    return reminder.diff(currentTime, 'minute') <= 0
  })

  if (activeReminder) {
    showPopup.value = true
  }
}

const closePopup = () => {
  showPopup.value = false
}

watch(reminders, () => {
  checkReminders()
})

onMounted(() => {
  timer = setInterval(() => {
    now.value = dayjs()
    checkReminders() 
  }, 10 * 1000)
})

const formatReapplyFrequency = (frequency) => {
  if (frequency === 1) {
    return 'Every hour'
  } else {
    return `Every ${frequency} hours`
  }
}

const generateICSFile = () => {
  const events = reminders.value.map((reminder, index) => {
    const startTime = reminder.format('YYYYMMDDTHHmmss')
    const endTime = reminder.add(15, 'minute').format('YYYYMMDDTHHmmss') 
    return `
BEGIN:VEVENT
UID:${index}@aussafe
DTSTAMP:${dayjs().format('YYYYMMDDTHHmmss')}
DTSTART:${startTime}
DTEND:${endTime}
SUMMARY:Reapply Sunscreen
DESCRIPTION:It's time to reapply sunscreen!
END:VEVENT
    `.trim()
  }).join('\n')

  const icsContent = `
BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Aussafe//Sunscreen Reminder//EN
${events}
END:VCALENDAR
  `.trim()

  return icsContent
}

const downloadICSFile = () => {
  const icsContent = generateICSFile()
  const blob = new Blob([icsContent], { type: 'text/calendar;charset=utf-8' })
  const url = URL.createObjectURL(blob)

  const link = document.createElement('a')
  link.href = url
  link.setAttribute('download', 'sunscreen_reminders.ics')
  document.body.appendChild(link)
  link.click()

  document.body.removeChild(link)
  URL.revokeObjectURL(url)
}

</script>

<style scoped>
.read-more {
  background-color: #fff4bc;
  padding: 10px 16px;
  border: none;
  font-size: 1rem;
  font-weight: bold;
  cursor: pointer;
  border-radius: 5px;
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s ease-in-out;
}

.read-more:hover {
  background-color: #f6e8b3;
}

.resources {
  font-family: 'Inter', sans-serif;
  max-width: 1200px;
  margin: 0 auto;
  padding: 32px 20px;
  color: #1a202c;
}

/* Heading */
h1 {
  font-size: 30px;
  font-weight: 700;
  text-align: center;
  color: #2d3748;
  margin-bottom: 32px;
}

/* Layout Container */
.container {
  display: flex;
  gap: 24px;
  justify-content: space-between;
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
  box-sizing: border-box;
}

/* Left Section */
.left-section {
  flex: 1;
  background-color: #fff;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  padding: 28px;
}

/* Right Section */
.right-section {
  flex: 0.4;
  background-color: #fff;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  padding: 24px;
}

/* Form Styling */
.form-group {
  margin-bottom: 16px;
}

.form-group label {
  display: block;
  font-size: 15px;
  font-weight: 600;
  color: #4a5568;
  margin-bottom: 6px;
}

.form-group select,
.form-group input {
  width: 100%;
  padding: 12px 14px;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  font-size: 15px;
  color: #2d3748;
  background-color: #f8fafc;
  transition: 0.2s ease;
}

.form-group select:focus,
.form-group input:focus {
  outline: none;
  border-color: #ffcf40;
  box-shadow: 0 0 5px rgba(255, 207, 64, 0.5);
}

/* Submit Button */
.submit-btn {
  width: 100%;
  padding: 14px;
  background-color: #ffcf40;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 600;
  color: #2d3748;
  cursor: pointer;
  transition: 0.3s;
}

.submit-btn:hover {
  background-color: #ffbb33;
  transform: scale(1.02);
}

.result-box {
  margin-top: 20px;
  padding: 18px;
  background: #f8fafc;
  border-radius: 8px;
}

/* Recommendation List */
.recommendation-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.recommendation-item {
  display: flex;
  justify-content: space-between;
  padding: 10px 0;
  font-size: 14px;
  border-bottom: 1px solid #edf2f7;
}

.key {
  font-weight: 600;
  color: #4a5568;
}

.value {
  color: #2d3748;
}

/* Error Message */
.error-message {
  margin-top: 12px;
  padding: 12px;
  background-color: #ffe6e6;
  color: #c53030;
  font-weight: 500;
  text-align: center;
  border-radius: 8px;
}

/* Reminders */
.reminder-instructions {
  font-size: 14px;
  font-weight: 500;
  color: #ffbb33;
  margin-bottom: 8px;
}

.reminder-list {
  list-style: none;
  padding: 0;
}

.reminder-item {
  display: flex;
  justify-content: space-between;
  padding: 10px 0;
  font-size: 14px;
  border-bottom: 1px solid #edf2f7;
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

.popup-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.popup-content {
  background-color: #ffffff;
  padding: 24px;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
  text-align: center;
}

.popup-content p {
  margin-bottom: 16px;
  font-size: 16px;
  color: #2d3748;
}

.popup-content button {
  padding: 8px 16px;
  background-color: #fff4bc;
  border: none;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 600;
  color: #2d3748;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.popup-content button:hover {
  background-color: #ffefb3;
}
.download-button {
  width: 100%;
  padding: 12px;
  background-color:#ffefb3;
  border: none;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 600;
  color: #2d3748;
  cursor: pointer;
  transition: background-color 0.2s ease;
  margin-top: 16px;
}
</style>