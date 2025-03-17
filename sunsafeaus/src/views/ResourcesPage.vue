<template>
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
      <ul class="reminder-list">
        <li v-for="(time, index) in reminders" :key="index" class="reminder-item">
          <span class="time">{{ time.format('HH:mm') }}</span>
          <span class="countdown">{{ timeUntil(time) }}</span>
        </li>
      </ul>
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


// 表单数据
const form = ref({
  skin_type: '',
  skin_tone: '',
  activity_level: '',
  location: null
})

// 下拉选项数据
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

// 位置相关
const locationQuery = ref('')
const locationOptions = ref([])



// 推荐结果与错误
const recommendation = ref({})
const error = ref('')

const reminders = ref([]) // 存储提醒时间

// 更新时间
const now = ref(dayjs())

// 搜索位置
const searchLocations = async () => {
  if (locationQuery.value) {
    try {
      const response = await axios.get('http://localhost:8000/locations', {
        params: { searchParam: locationQuery.value }
      })
      locationOptions.value = response.data
    } catch (err) {
      console.error('位置搜索失败:', err)
    }
  } else {
    locationOptions.value = []
  }
}

// 选择位置
const selectLocation = (item) => {
  form.value.location = item
  locationQuery.value = `${item.location_name} (${item.zipcode})`
  locationOptions.value = []
}

// 表单验证
const validateForm = () => {
  return (
    form.value.skin_type &&
    form.value.skin_tone &&
    form.value.activity_level &&
    form.value.location
  )
}

// 提交表单
const submitForm = async () => {
  error.value = ''
  recommendation.value = {}

  if (!validateForm()) {
    error.value = '请填写所有必填字段'
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
  }, 60 * 1000) // 每分钟更新一次
})

onUnmounted(() => {
  clearInterval(timer)
})

// 监听 recommendation 更新提醒
watch(recommendation, () => {
  generateReminders()
})

const generateReminders = () => {
  reminders.value = [] // 清空上次的提醒

  if (!recommendation.value.reapply_frequency) return

  const freqMatch = recommendation.value.reapply_frequency.match(/(\d+)/)
  if (!freqMatch) return

  const hoursInterval = parseInt(freqMatch[1]) // 提取频率小时数
  const startTime = dayjs() // 当前时间
  const endTime = dayjs().hour(18).minute(0).second(0) // 设定晚上 18:00 截止

  let nextTime = startTime.add(hoursInterval, 'hour').startOf('hour')

  // 自动生成提醒
  while (nextTime.isBefore(endTime)) {
    reminders.value.push(nextTime)
    nextTime = nextTime.add(hoursInterval, 'hour')
  }

  console.log('生成的提醒:', reminders.value.map(t => t.format('HH:mm')))
}
// 倒计时计算器
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
.container {
  display: flex;
  justify-content: space-between; /* 将左右部分分开 */
}
.recommendation-container {
  max-width: 600px;
  margin: 20px auto;
  padding: 20px;
}

.result-box {
  margin-top: 20px;
  padding: 15px;
  border: 1px solid #e4e7ed;
  border-radius: 4px;
  background-color: #f8f9fa;
}

.error-message {
  color: #f56c6c;
  margin-top: 10px;
}

.location-options {
  border: 1px solid #ccc;
  max-height: 150px;
  overflow-y: auto;
  list-style: none;
  padding: 0;
  margin: 0;
}

.location-options li {
  padding: 8px;
  cursor: pointer;
}

.location-options li:hover {
  background-color: #f0f0f0;
}

.recommendation-list {
  list-style: none;
  padding: 0;
}

.recommendation-item {
  margin-bottom: 10px;
}

.key {
  font-weight: bold;
  text-transform: capitalize;
}

.value {
  margin-left: 10px;
}

.reminder-list {
  list-style: none;
  padding: 0;
}

.reminder-item {
  display: flex;
  justify-content: space-between;
  margin-bottom: 8px;
}

.time {
  font-weight: bold;
}

.countdown {
  color: gray;
  font-size: 0.9em;
}
</style>
