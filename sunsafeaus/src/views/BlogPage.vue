<template>
    <div class="blog-page">
      <h1>Impacts of UV</h1>
      <p class="description">Data analysis and visualisation</p>
  
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


    <!-- 图片展示 -->
    <div class="image-grid">
  <div v-for="(image, index) in images" :key="index" class="image-card">
    <img :src="image.src" :alt="image.title" class="blog-image" />
  </div>
</div>

    <!-- 关键见解展示 -->
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

      <!-- 其他关键见解 -->
    </div>
  </div>
</div>
  </template>
  
  <script>
import blog1 from '@/assets/blog2.png'
import blog2 from '@/assets/blog2.png'
import blog3 from '@/assets/blog3.png'
import blog4 from '@/assets/blog4.png'
import blog5 from '@/assets/blog5.png'
import blog6 from '@/assets/blog6.png'
import blog7 from '@/assets/blog7.png'
import blog8 from '@/assets/blog8.png'

const images = [
{ src: blog1, title: 'Understanding UV Radiation', description: 'Explore the impact of UV radiation on skin health.' },
  { src: blog2, title: 'Understanding UV Radiation', description: 'Explore the impact of UV radiation on skin health.' },
  { src: blog2, title: 'Stay Safe Under the Sun', description: 'Learn about sun protection measures.' },
  { src: blog3, title: 'UV Index and Weather', description: 'Understand the science behind UV index.' },
  { src: blog4, title: 'Cancer Incidence Trends', description: 'See the rise in skin cancer cases.' },
  { src: blog5, title: 'Gender Differences', description: 'Explore differences in cancer rates by gender.' },
  { src: blog6, title: 'Impact of Cancer Type', description: 'Understand the impact of melanoma vs non-melanoma.' },
  { src: blog7, title: 'Recent Trends', description: 'See the sharp rise in cases since 2000.' },
  { src: blog8, title: 'Preventive Measures', description: 'Learn about early screening and sun protection.' },
]

  export default {
    name: "BlogPage",
    data() {
      return {
      images, // ✅ 正确暴露 images 变量
    };
      
  
    // setup() {
      // Simulated blog post data
    //   const blogPosts = ref([
    //     {
    //       id: 1,
    //       title: "Understanding UV Radiation and Its Effects",
    //       excerpt: "Explore the impact of UV radiation on skin health and why sun protection is crucial.",
    //       image: "/assets/blog1.jpg",
    //     },
    //     {
    //       id: 2,
    //       title: "How to Stay Safe Under the Australian Sun",
    //       excerpt: "Learn about the best sunscreen practices and protective measures for sun safety.",
    //       image: "/assets/blog2.jpg",
    //     },
    //     {
    //       id: 3,
    //       title: "The Science Behind UV Index and Weather",
    //       excerpt: "A detailed explanation of the UV index, how it's measured, and what it means for daily life.",
    //       image: "/assets/blog3.jpg",
    //     },
    //   ]);
  
    //   return { blogPosts };
    },
  };
  </script>
  
  <style scoped>
  .blog-page {
    text-align: center;
    padding: 20px;
  }
  
  .description {
    font-size: 16px;
    margin-bottom: 20px;
  }
  
  .blog-container {
    display: flex;
    justify-content: center;
    gap: 20px;
    flex-wrap: wrap;
    margin-top: 20px;
  }
  
  .blog-card {
    background: #fff;
    border-radius: 8px;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    width: 300px;
    overflow: hidden;
    text-align: left;
  }
  
  .blog-image {
    width: 100%;
    height: 180px;
    object-fit: cover;
  }
  
  .blog-content {
    padding: 15px;
  }
  
  .blog-content h2 {
    font-size: 18px;
    margin-bottom: 10px;
  }
  
  .blog-content p {
    font-size: 14px;
    color: #555;
  }
  
  .read-more {
    display: inline-block;
    margin-top: 10px;
    font-size: 14px;
    font-weight: bold;
    color: #007bff;
    text-decoration: none;
  }
  
  .read-more:hover {
    text-decoration: underline;
  }
  .key-insights {
  text-align: left;
  margin: 40px auto;
  max-width: 900px;
  line-height: 1.8;
  color: #333;
}
  </style>  