<template>
    <div class="survey">
        <Navbar />
        <h1>설문조사 페이지</h1>
    </div>
</template>

<script>
import Navbar from '../components/Navbar.vue';
export default {
  name: "survey",
    data () {
    return {
      title: 'Survey'
    }
      },
  components: {
    Navbar
  }
};
</script>

<style>

</style>
