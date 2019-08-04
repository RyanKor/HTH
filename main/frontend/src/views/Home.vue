<template>
  <div class="home">
    <Navbar />
    <Container1 />
    <Container2 />
    <Container3 />
    <Container4 />
  </div>
</template>

<script>
// @ is an alias to /src
import Container1 from "../components/homePage/Container1.vue";
import Container2 from "../components/homePage/Container2.vue";
import Container3 from "../components/homePage/Container3.vue";
import Container4 from "../components/homePage/Container4.vue";
import Navbar from "../components/homePage/Navbar.vue";

export default {
  name: "home",
  components: {
    Container1,
    Container2,
    Container3,
    Container4,
    Navbar
  }
};
</script>
<style>
</style>
