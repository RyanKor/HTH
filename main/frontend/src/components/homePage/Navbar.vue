<template>
  <div class="nav">
    <div class="navhead">
      <div class="navhead-brand">
        <router-link :to="{ name: 'home' }">
          <img class="navhead-brand-logo" src="../../assets/logo4.png" />
        </router-link>
      </div>
      <!-- <p class="navhead-txt">청각장애인을 위한 진료도우미</p> -->
      <div class="navhead-icon" @click="expanded = !expanded">
        <i class="fas fa-bars fa-lg"></i>
      </div>
    </div>
    <transition-expand>
      <div class="navexpand" v-if="expanded">
        <a class="nav-menu">로그인</a>
        <br />
        <a class="nav-menu">회원가입</a>
        <br />
        <a class="nav-menu">About 60dB</a>
      </div>
    </transition-expand>
  </div>
</template>

<script>
import TransitionExpand from "./NavEffect.vue";
export default {
  name: `Nav`,
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

<style scope>
/* nav bar */

.navhead {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid rgba(192, 192, 192, 0.562);
  padding: 0 0.8rem;
  height: 8.5vh;
}
.navhead-brand-logo {
  width: 16.5rem;
  height: 3rem;
  vertical-align: middle;
}
.navhead-txt {
  color: gray;
  font-family: "KoreanDREAM3R";
  letter-spacing: 80%;
  font-size: 0.6rem;
  margin-left: 5%;
  margin-right: 10%;
}
.navhead-icon {
  display: flex;
  justify-content: center;
  background-color: white;
  border: 1px solid rgba(128, 128, 128, 0.24);
  border-radius: 3px;
  width: 44px;
  height: 34px;
  padding: 0.1rem;
}
.navhead-icon:hover {
  background-color: rgb(233, 232, 232);
  transition: 0.4s;
}
.navhead-icon:focus {
  background-color: rgb(233, 232, 232);
}
.fa-bars {
  color: gray;
  margin: 0.25rem auto;
  font-size: 1.5rem;
}
.navexpand {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  border-bottom: 1px solid rgba(192, 192, 192, 0.63);
  color: rgb(77, 77, 77);
  line-height: 1px;
  font-weight: 500;
}
.nav-menu {
  font-size: 0.9rem;
  width: 100%;
  padding: 20px 20px;
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