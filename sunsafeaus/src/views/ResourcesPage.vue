<template>
  <div class="resources">
    <h1>Get Your Personalized Recommendations for Sun Safety</h1>

      
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
            <button type="submit" class="read-more">Get Recommendations</button>
          </form>

          <!-- Recommendation Box -->
          <div class="result-box">
            <h3>Your Recommendations-</h3>
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

      <!-- Right Section (Reminders) -->
      <div class="right-section">
        <h3>Sunscreen Reminders</h3>
        <div class="reminder-instructions">
          <p>The sun is strongest between 9 AM - 6 PM, making sun protection essential. Let us help you to set sunscreen reminders during these hours, based on your personalised recommendations. Download a reminder for your Google/Apple Calendar so you never forget!</p>
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
.resources {
  max-width: 700px;
  margin: 0 auto;
  padding: 32px 20px;
  text-align: center;
}

h1 {
  font-size: 26px;
  font-weight: bold;
  text-align: center;
  margin-bottom: 24px;
}

.content-container {
  display: flex;
  flex-direction: column;
  align-items: center; 
  gap: 20px;
  width: 100%;
}

.recommendation-container {
  width: 100%;
  max-width: 600px;
  min-height: 500px;
  background-color: #ffffff;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  padding: 24px;
  box-sizing: border-box;
  min-height: 420px;
  margin-bottom: 24px;
  align-items: center;
  margin: 0 auto;
}

.form-group {
  margin-bottom: 16px;
  text-align: left;
}

.form-group label {
  display: block;
  font-size: 15px;
  margin-bottom: 6px;
}

.form-group select,
.form-group input {
  width: 100%;
  padding: 12px 14px;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  font-size: 12px;
  color: #2d3748;
  background-color: #f8fafc;
  transition: 0.2s ease;
  box-sizing: border-box;
}

.form-group select:focus,
.form-group input:focus {
  outline: none;
  border-color: #ffcf40;
  box-shadow: 0 0 5px rgba(255, 207, 64, 0.5);
}

.read-more {
  background-color: #fff4bc;
  padding: 12px 16px;
  border: none;
  font-size: 1rem;
  font-weight: bold;
  cursor: pointer;
  border-radius: 5px;
  box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s ease-in-out;
  width: 100%;
  margin-top: 10px;
}

.read-more:hover {
  background-color: #f6e8b3;
}

.result-box {
  width: 100%;
  background: #f8fafc;
  border-radius: 8px;
  padding: 18px;
  box-sizing: border-box;
  margin-top: 16px;
  text-align: left;
}

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
  align-items: center;
}

.key {
  font-weight: 600;
  color: #4a5568;
  flex: 1;
  text-align: left;
}

.value {
  flex: 2;
  text-align: left;
  color: #2d3748;
}

.result-box:last-child {
  margin-bottom: 0;
}

.error-message {
  margin-top: 12px;
  padding: 12px;
  background-color: #ffe6e6;
  color: #c53030;
  font-weight: 500;
  text-align: center;
  border-radius: 8px;
}

.right-section {
  max-width: 600px;
  background-color: #ffffff;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  padding: 24px;
  box-sizing: border-box;
}

.right-section,
.result-box {
  margin-left: auto;
  margin-right: auto;
}

/* **Fix: Adjusts Reminders Section Spacing** */
.reminder-instructions {
  font-size: 14px;
  font-weight: 500;
  color: grey;
  margin-bottom: 8px;
}


.right-section h3 {
  margin-bottom: 10px;
}

.right-section {
  text-align: center;
  margin-top: 10px;
}

.right-section:last-child {
  margin-bottom: 0;
}

.download-button {
  width: 100%;
  padding: 12px;
  background-color: #ffefb3;
  border: none;
  border-radius: 8px;
  font-size: 14px;
  font-weight: 600;
  color: #2d3748;
  cursor: pointer;
  transition: background-color 0.2s ease;
  margin-top: 16px;
}

@media (max-width: 768px) {
  .resources {
    max-width: 90%;
  }

  .container {
    flex-direction: column;
    align-items: center;
    width: 100%;
  }
}
</style>