<template>
  <div class="uv-gauge">
    <svg :width="size" :height="size * 0.8" viewBox="0 0 200 160">
      <path 
        v-for="(segment, index) in segmentsWithPaths"
        :key="index"
        :d="segment.path"
        :stroke="segment.color"
        stroke-width="8"
        fill="none"
        stroke-linecap="round"
      />

      <line
        x1="100"
        y1="80"
        x2="100"
        y2="35"
        stroke="#333"
        stroke-width="2"
        :transform="`rotate(${pointerAngle}, 100, 80)`"
        stroke-linecap="round"
      />

      <text
        x="100"
        y="90"
        text-anchor="middle"
        font-size="24"
        font-weight="bold"
        fill="#333"
      >
        {{ displayValue }}
      </text>

      <text
        x="100"
        y="140"
        text-anchor="middle"
        font-size="14"
        fill="#666"
      >
        {{ statusText }}
      </text>
    </svg>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue';

interface Segment {
  min: number;
  max: number;
  color: string;
  path: string;
}

const props = defineProps({
  uvValue: {
    type: Number,
    required: true,
    validator: (value: number) => value >= 0 && value <= 15
  },
  size: {
    type: Number,
    default: 200,
    validator: (value: number) => value > 0
  }
});

const START_ANGLE = -150;
const TOTAL_VISIBLE_ANGLE = 300;
const RADIUS = 70;
const CENTER = { x: 100, y: 80 };

const segments = [
  { min: 0,  max: 2.9,  color: '#A3D39C' },
  { min: 3,  max: 5.9,  color: '#FFD700' },
  { min: 6,  max: 7.9,  color: '#FFA500' },
  { min: 8,  max: 10.9, color: '#FF6347' },
  { min: 11, max: 12.9, color: '#CD5C5C' },
  { min: 13, max: 15,   color: '#8B0000' }
];

const segmentsWithPaths = computed(() => {
  let accumulatedAngle = START_ANGLE;
  
  return segments.map(segment => {
    const range = segment.max - segment.min;
    const angleSpan = (range / 15) * TOTAL_VISIBLE_ANGLE;
    
    const path = generateArcPath(
      accumulatedAngle,
      accumulatedAngle + angleSpan
    );

    accumulatedAngle += angleSpan;
    
    return {
      ...segment,
      path
    };
  });
});

const generateArcPath = (startDeg: number, endDeg: number): string => {
  const toRadians = (deg: number) => (deg - 90) * Math.PI / 180;
  
  const startRad = toRadians(startDeg);
  const endRad = toRadians(endDeg);
  const largeArcFlag = endDeg - startDeg > 180 ? 1 : 0;

  return `
    M ${CENTER.x + RADIUS * Math.cos(startRad)} 
    ${CENTER.y + RADIUS * Math.sin(startRad)}
    A ${RADIUS} ${RADIUS} 0 
    ${largeArcFlag} 1
    ${CENTER.x + RADIUS * Math.cos(endRad)} 
    ${CENTER.y + RADIUS * Math.sin(endRad)}
  `;
};

const pointerAngle = computed(() => {
  const normalizedValue = Math.min(Math.max(props.uvValue, 0), 15);
  return START_ANGLE + (normalizedValue / 15) * TOTAL_VISIBLE_ANGLE;
});

const displayValue = computed(() => props.uvValue.toFixed(1));

const statusText = computed(() => {
  const value = props.uvValue;
  if (value <= 2.9) return 'Low';
  if (value <= 5.9) return 'Moderate';
  if (value <= 7.9) return 'High';
  if (value <= 10.9) return 'Very High';
  if (value <= 12.9) return 'Extreme';
  return 'Dangerous';
});
</script>

<style scoped>
.uv-gauge {
  font-family: Arial, sans-serif;
  background: #f8f9fa;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}
</style>