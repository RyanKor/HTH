<template>
  <div class="nav">
    <transition-expand>
      <div class="navbar">
        <div class="nav-brand">
          <img class="logo" src="../../assets/logo_tp.png" />
        </div>
        <div class="nav-icon">
          <span class="icon" @click="expanded = !expanded">
            <i class="fas fa-bars"></i>
          </span>
        </div>
      </div>
      <div class="navexpand" v-if="expanded">
        <div v-if="expanded">
          Magna aliquyam erat, sed diam voluptua. At vero eos et
          accusam et justo duo dolores et ea rebum. Stet clita kasd
          gubergren, no sea takimata sanctus est Lorem ipsum dolor
          sit amet. Lorem ipsum dolor sit amet, consetetur
          sadipscing elitr, sed diam nonumy eirmod tempor invidunt
          ut labore et dolore magna aliquyam erat, sed diam
          voluptua. At vero eos et accusam et justo duo dolores et
          ea rebum. Stet clita kasd gubergren, no sea takimata
          sanctus est Lorem ipsum dolor sit amet.
        </div>
      </div>
    </transition-expand>
  </div>
</template>

<script>
import TransitionExpand from "./NavEffect.vue";
export default {
  name: `App`,
  components: {
    TransitionExpand
  },
  data() {
    return {
      expanded: false
    };
  }
};
</script>

<style>
/* nav bar */
.logo {
  width: 4rem;
  height: 2rem;
}
.expand-enter-active,
.expand-leave-active {
  transition-property: opacity, height;
}
.expand-enter,
.expand-leave-to {
  opacity: 0;
}
</style>