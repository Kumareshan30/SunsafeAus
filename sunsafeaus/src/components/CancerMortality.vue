<template>
    <div class="cancer-mortality">
      <!-- Filters -->
      <div class="filters">
        <label for="cancerType">Cancer Type:</label>
        <select id="cancerType" v-model="selectedCancerType">
          <option v-for="type in cancerTypes" :key="type" :value="type">{{ type }}</option>
        </select>
  
        <label for="sex">Sex:</label>
        <select id="sex" v-model="selectedSex">
          <option v-for="sex in sexes" :key="sex" :value="sex">{{ sex }}</option>
        </select>
  
        <label for="startYear">Start Year:</label>
        <select id="startYear" v-model="selectedStartYear">
          <option v-for="year in years" :key="year" :value="year">{{ year }}</option>
        </select>
  
        <label for="endYear">End Year:</label>
        <select id="endYear" v-model="selectedEndYear">
          <option v-for="year in years" :key="year" :value="year">{{ year }}</option>
        </select>
      </div>
  
  
      <!-- Bar Chart -->
      <div class="chart-container">
        <canvas ref="barChart"></canvas>
      </div>
    </div>
  </template>
  
  <script>
  import { ref, computed, watch, onMounted } from 'vue';
  import { Chart, registerables } from 'chart.js';
  
  Chart.register(...registerables);
  
  export default {
    name: 'CancerMortality',
    setup() {
      const selectedCancerType = ref('Melanoma of the skin');
      const selectedSex = ref('Persons');
      const selectedStartYear = ref(2000);
      const selectedEndYear = ref(2020);
  
      const cancerData = ref([]);
  
      const loadData = async () => {
        try {
          const response = await fetch('/cancer_mortality.csv');
          const text = await response.text();
          const rows = text.split('\n').slice(1); 
          cancerData.value = rows
          .filter(row => row.trim() !== '') 
          .map(row => {
            const [Year, CancerType, Sex, Count, AgeSpecificRate] = row.split(',');
            return {
              Year: parseInt(Year),
              'Cancer Type': CancerType.trim(), 
              Sex: Sex.trim(), 
              Count: parseInt(Count),
              'Age-specific Rate (per 100,000)': parseFloat(AgeSpecificRate),
            };
          });
        } catch (error) {
          console.error('Error loading data:', error);
        }
      };
  
      onMounted(loadData);

      const cancerTypes = computed(() => [...new Set(cancerData.value.map(row => row['Cancer Type']))]);
      const sexes = computed(() => [...new Set(cancerData.value.map(row => row.Sex))]);
      const years = computed(() => [...new Set(cancerData.value.map(row => row.Year))].sort());
  
      const filteredData = computed(() => {
        return cancerData.value.filter(row => 
          row['Cancer Type'] === selectedCancerType.value &&
          row.Sex === selectedSex.value &&
          row.Year >= selectedStartYear.value &&
          row.Year <= selectedEndYear.value
        );
      });
  
      const barChart = ref(null);
      let chartInstance = null;
  
      const updateChart = () => {
        if (chartInstance) {
          chartInstance.destroy();
        }
  
        const labels = years.value.filter(year => year >= selectedStartYear.value && year <= selectedEndYear.value);
        const counts = labels.map(year => {
          const rows = filteredData.value.filter(row => row.Year === year);
          return rows.reduce((sum, row) => sum + row.Count, 0);
        });
  
        chartInstance = new Chart(barChart.value, {
          type: 'bar',
          data: {
            labels,
            datasets: [{
              label: 'Total Death Count',
              data: counts,
              backgroundColor: 'rgba(75, 192, 192, 0.2)',
              borderColor: 'rgba(75, 192, 192, 1)',
              borderWidth: 1,
            }],
          },
          options: {
            scales: {
              y: {
                beginAtZero: true,
              },
            },
          },
        });
      };
  
      watch([selectedCancerType, selectedSex, selectedStartYear, selectedEndYear], updateChart);
      watch(cancerData, updateChart);
  
      return {
        selectedCancerType,
        selectedSex,
        selectedStartYear,
        selectedEndYear,
        cancerTypes,
        sexes,
        years,
        filteredData,
        barChart,
      };
    },
  };
  </script>
  
  <style scoped>
  .cancer-mortality {
    font-family: Arial, sans-serif;
  }
  
  .filters {
    margin-bottom: 20px;
  }
  
  .filters label {
    margin-right: 10px;
  }
  
  table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 20px;
  }
  
  th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
  }
  
  th {
    background-color: #f4f4f4;
  }
  
  .chart-container {
    width: 80%;
    margin: 0 auto;
  }
  </style>