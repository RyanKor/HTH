<template>
  <div class="home">
    <Navbar />
    <Slider />
    <HelloWorld msg="Welcome to Your Vue.js App" />
    <Company />
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";
import Navbar from '../components/Navbar.vue';
import Slider from '../components/Carousel.vue';
import Company from '../components/Company.vue';
export default {
  name: "home",
    data () {
    return {
      title: 'Main'
    }
      },
  components: {
    Navbar,
    HelloWorld,
    Slider,
    Company
  }
};
</script>
