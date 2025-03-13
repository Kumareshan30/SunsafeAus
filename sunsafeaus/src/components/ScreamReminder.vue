<template>
    <div class="reminder-container">
      <button @click="showAddDialog" class="add-button">
        + Add Sunscreen Reminder
      </button>
  
      <div v-for="reminder in reminders" :key="reminder.id" class="reminder-item">
    <div class="reminder-content">
      <h4>{{ reminder.title }}</h4>
      <div class="time">{{ reminder.time }}</div>
      <div class="description">{{ reminder.description }}</div>
      <div class="countdown">{{ reminder.countdown }}</div>
      <a v-if="reminder.link" :href="reminder.link" class="zoom-link">{{ reminder.link }}</a>
    </div>
    <button @click="deleteReminder(reminder.id)" class="delete-btn">
      Delete
    </button>
  </div>
  
      <div v-if="isDialogVisible" class="dialog-overlay">
        <div class="dialog-content">
          <h3>Set Reminder Time</h3>
          <input 
            type="time" 
            v-model="newReminderTime"
            class="time-input"
          />
          <div class="dialog-buttons">
            <button @click="saveReminder" class="save-button">Save</button>
            <button @click="closeDialog" class="cancel-button">Cancel</button>
          </div>
        </div>
      </div>
  
      <div v-if="isNotificationVisible" class="notification-overlay">
        <div class="notification-content">
          <h3>⏰ Sunscreen Time!</h3>
          <p>Don't forget to reapply sunscreen!</p>
          <button @click="closeNotification" class="confirm-button">OK</button>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted, onUnmounted } from 'vue';
  
  const reminders = ref([]);
  const isDialogVisible = ref(false);
  const isNotificationVisible = ref(false);
  const newReminderTime = ref('');
  let checkInterval = null;
  
  const loadReminders = () => {
    const saved = localStorage.getItem('sunscreenReminders');
    if (saved) reminders.value = JSON.parse(saved);
  };
  
  const saveToLocalStorage = () => {
    localStorage.setItem('sunscreenReminders', JSON.stringify(reminders.value));
  };
  
  const showAddDialog = () => {
    isDialogVisible.value = true;
    newReminderTime.value = '';
  };
  
  const closeDialog = () => {
    isDialogVisible.value = false;
  };
  
  const saveReminder = () => {
    if (newReminderTime.value) {
      if (!reminders.value.some(r => r.time === newReminderTime.value)) {
        reminders.value.push({
          id: Date.now(),
          time: newReminderTime.value
        });
        saveToLocalStorage();
      }
      closeDialog();
    }
  };
  
  const checkReminders = () => {
    const now = new Date();
    const currentTime = `${now.getHours().toString().padStart(2, '0')}:${now.getMinutes().toString().padStart(2, '0')}`;
    
    if (reminders.value.some(r => r.time === currentTime)) {
      isNotificationVisible.value = true;
    }
  };
  
  const closeNotification = () => {
    isNotificationVisible.value = false;
  };

  const deleteReminder = (id) => {
  reminders.value = reminders.value.filter(r => r.id !== id)
  saveToLocalStorage()
}
  
  onMounted(() => {
    loadReminders();
    checkInterval = setInterval(checkReminders, 1000 * 60); 
  });
  
  onUnmounted(() => {
    clearInterval(checkInterval);
  });
  </script>
  
  <style scoped>
  .reminder-container {
    max-width: 400px;
    margin: 20px auto;
    padding: 20px;
  }
  
  .add-button {
    background: #4CAF50;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
    width: 100%;
    font-size: 16px;
  }
  
  .reminder-list {
    margin-top: 20px;
  }
  
  .reminder-item {
    background: #f5f5f5;
    padding: 10px;
    margin: 5px 0;
    border-radius: 4px;
  }
  
  .dialog-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0,0,0,0.5);
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .dialog-content {
    background: white;
    padding: 20px;
    border-radius: 8px;
    width: 300px;
  }
  
  .time-input {
    width: 100%;
    padding: 8px;
    margin: 10px 0;
    font-size: 16px;
  }
  
  .dialog-buttons {
    display: flex;
    gap: 10px;
    margin-top: 15px;
  }
  
  .save-button, .cancel-button {
    flex: 1;
    padding: 8px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .save-button {
    background: #4CAF50;
    color: white;
  }
  
  .cancel-button {
    background: #f44336;
    color: white;
  }
  
  .notification-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0,0,0,0.5);
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .notification-content {
    background: white;
    padding: 25px;
    border-radius: 8px;
    text-align: center;
    width: 300px;
  }
  
  .confirm-button {
    background: #2196F3;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 4px;
    margin-top: 15px;
    cursor: pointer;
  }
  </style>