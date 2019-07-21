<template>
  <div class="home">
    <Navbar />
    <Slider />
    <Buttons msg="편의 기능 함 눌러봐" />
    <Footer />
  </div>
</template>

<script>
// @ is an alias to /src
import Buttons from "../components/Buttons.vue";
import Navbar from '../components/Navbar.vue';
import Slider from '../components/Carousel.vue';
import Footer from '../components/Footer.vue';
export default {
  name: "home",
    data () {
    return {
      title: 'Main'
    }
      },
  components: {
    Navbar,
    Slider,
    Buttons,
    Footer
  }
};
</script>
<style>
</style>
