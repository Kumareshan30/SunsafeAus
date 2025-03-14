<template>
    <div class="blog-page">
      <h1>Impacts of UV</h1>
      <p class="description">Data analysis and visualisation</p>
  
      <div class="blog-container">
        <div v-for="post in blogPosts" :key="post.id" class="blog-card">
          <img :src="post.image" alt="Blog Image" class="blog-image" />
          <div class="blog-content">
            <h2>{{ post.title }}</h2>
            <p>{{ post.excerpt }}</p>
            <router-link :to="'/blog/' + post.id" class="read-more">Read More</router-link>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { ref } from "vue";
  
  export default {
    name: "BlogPage",
    setup() {
      // Simulated blog post data
      const blogPosts = ref([
        {
          id: 1,
          title: "Understanding UV Radiation and Its Effects",
          excerpt: "Explore the impact of UV radiation on skin health and why sun protection is crucial.",
          image: "/assets/blog1.jpg",
        },
        {
          id: 2,
          title: "How to Stay Safe Under the Australian Sun",
          excerpt: "Learn about the best sunscreen practices and protective measures for sun safety.",
          image: "/assets/blog2.jpg",
        },
        {
          id: 3,
          title: "The Science Behind UV Index and Weather",
          excerpt: "A detailed explanation of the UV index, how it's measured, and what it means for daily life.",
          image: "/assets/blog3.jpg",
        },
      ]);
  
      return { blogPosts };
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
  </style>  