<template>
  <div class="practice">
    <navbar />
    <scroll />
  </div>
</template>

<script>
import scroll from "../components/surveyPage/example.vue";
import navbar from "../components/homePage/Navbar.vue";
export default {
  name: "practice",

  components: {
    scroll,
    navbar
  }
};
</script>
<style>
</style>
