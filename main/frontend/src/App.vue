<template>
  <div>
    <!-- <Navbar /> -->
    <router-view />
  </div>
</template>

<script>
// import Navbar from "./components/homePage/Navbar.vue";
export default {
  name: "App",
  components: {
    // Navbar
  }
};
</script>
<style>
@import url(https://cdn.jsdelivr.net/gh/moonspam/NanumSquare@1.0/nanumsquare.css);

* {
  font-family: "NanumSquare", sans-serif;
}
</style>

