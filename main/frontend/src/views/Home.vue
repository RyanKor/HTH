<template>
  <div class="home">
    <Navbar />
  </div>
</template>

<script>
// @ is an alias to /src
// import Buttons from "../components/Buttons.vue";
// import Navbar from "../components/Navbar.vue";
// import Slider from "../components/Carousel.vue";
// import Footer from "../components/Footer.vue";
import Navbar from "../components/homePage/Navbar.vue";
export default {
  name: "home",
  data() {
    return {
      title: "Main"
    };
  },
  components: {
    Navbar
  }
};
</script>
<style>
</style>
