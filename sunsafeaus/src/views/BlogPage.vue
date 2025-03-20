<template>
    <div class="blog-page">
      <h1>Impacts of UV</h1>  
      <!-- <div class="blog-container">
        <div v-for="post in blogPosts" :key="post.id" class="blog-card">
          <img :src="post.image" alt="Blog Image" class="blog-image" />
          <div class="blog-content">
            <h2>{{ post.title }}</h2>
            <p>{{ post.excerpt }}</p>
            <router-link :to="'/blog/' + post.id" class="read-more">Read More</router-link>
          </div>
        </div>
      </div> -->

  <div class="insights-page">

    <div class="image-grid">
      <div>
    <h1>Cancer Mortality Data</h1>
    <CancerMortality/>
    <h1>Cancer Incident Data</h1>
    <CancerIncident/>
  </div>
</div>

    <div class="key-insights">
      <h1>Key Insights</h1>
      <h2>Steady Increase in Cancer Incidence</h2>
      <p>Steady Increase in Cancer Incidence

Over the years, there has been a noticeable rise in reported cases of Melanoma of the skin and Non-melanoma skin cancer for both males and females.
The trend suggests increased exposure to UV radiation, changes in lifestyle, or improved early detection methods.
Gender-Based Differences

Males have a higher incidence of Melanoma of the skin compared to females, especially in recent years.
This may be due to differences in outdoor exposure, genetic factors, or protective behaviors (e.g., sunscreen use).
Impact of Cancer Type

Melanoma cases are significantly higher compared to Non-melanoma skin cancer, emphasizing the need for targeted prevention efforts.
Rare non-melanoma cancers show a much lower but increasing trend.
Recent Years Show a Sharp Rise

The number of cases has escalated sharply from 2000 onwards, particularly for Melanoma.
This aligns with increased UV exposure risks and environmental factors.
Preventive Measures Needed

The rise in cases highlights the importance of early screening, sun protection, and awareness campaigns to reduce long-term risks.
</p>

      <h2>CANCER- MORTALITY</h2>
        <p>1.⁠ ⁠Mortality Trends Over Time
Cancer-related deaths have steadily increased over the years for both Melanoma and Non-melanoma skin cancers.
The increase in deaths is more noticeable from the 1990s onwards, aligning with the rising incidence of skin cancer.</p>
<p>2.⁠ ⁠Gender-Based Mortality Differences
Males have a higher mortality rate compared to females for Melanoma of the skin, likely due to later-stage diagnosis and fewer protective measures.
Females show a gradual rise in mortality, but at a lower rate than males.</p>
<p>3.⁠ ⁠Peak Mortality Periods
The 2010-2020 period shows the highest number of cancer-related deaths, with some decline in recent years.
The mortality rate does not increase at the same pace as incidence rates, suggesting better treatment options may have improved survival.</p>
<p>4.⁠ ⁠Non-Melanoma Skin Cancer Mortality
Compared to Melanoma, non-melanoma skin cancer mortality rates are significantly lower, but they have been rising steadily.
Men experience a higher fatality rate from non-melanoma skin cancers than women.</p>
<p>5.⁠ ⁠Implications & Preventive Measures
Early detection and awareness campaigns can help reduce mortality rates for skin cancers.
Continued advancements in treatment have helped slow the rate of mortality increase, but further research is needed.
Regular skin screenings, sun protection habits, and early medical intervention remain key in reducing deaths from both melanoma and non-melanoma skin cancers.</p>

    </div>
  </div>
</div>
  </template>
  
  <script>

import CancerMortality from '@/components/CancerMortality.vue';
import CancerIncident from '@/components/CancerIncident.vue';



  export default {
    name: "BlogPage",
    components: {
    CancerMortality,
    CancerIncident
    },
    };
      

  </script>
  
<style scoped>
/* General Blog Page Styling */
.blog-page {
  text-align: center;
  padding: 20px;
}

/* Insights Page Grid */
.image-grid {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
}

/* Key Insights Section */
.key-insights {
  text-align: justify; /* Ensures all text is justified */
  margin: 40px auto;
  max-width: 900px;
  line-height: 1.8;
  color: #333;
}

/* Adjusting Text Elements */
.key-insights h1, 
.key-insights h2 {
  text-align: center; /* Keeps headings centered */
}

.key-insights p {
  text-align: justify; /* Justifies all paragraph text */
}

/* Ensuring Images and Charts are Responsive */
.chart-container {
  width: 90%;
  max-width: 1200px;
  height: 60vh;
  min-height: 400px;
  margin: 0 auto;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Responsive Adjustments */
@media (max-width: 768px) {
  .image-grid {
    width: 100%;
    padding: 10px;
  }

  .chart-container {
    height: 50vh;
    min-height: 300px;
  }

  .key-insights {
    padding: 10px;
  }

  .key-insights h1, .key-insights h2 {
    font-size: 20px;
  }

  .key-insights p {
    font-size: 14px;
  }
}
</style>
