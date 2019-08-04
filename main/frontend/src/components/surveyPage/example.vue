<template>
  <div class="scroll">
    <scrollactive
      class="scrollnav"
      v-on:itemchanged="onItemChanged"
      :offset="30"
      :duration="600"
      :modifyUrl="false"
      bezier-easing-value=".5,0,.35,1"
    >
      <a href="#port1" class="scrollactive-item">Section1</a>
      <a href="#port2" class="scrollactive-item">Section2</a>
      <a href="#port3" class="scrollactive-item">Section3</a>
      <a href="#port4" class="scrollactive-item">Section4</a>
    </scrollactive>
    <div id="port1">
      <span class="span">Section1</span>
    </div>
    <div id="port2">
      <span class="span">Section2</span>
    </div>
    <div id="port3">
      <span class="span">Section3</span>
    </div>
    <div id="port4">
      <span class="span">Section4</span>
    </div>
  </div>
</template>

<script>
export default {
  name: "scroll",
  data() {
    return {};
  },
  methods: {
    onItemChanged() {}
  }
};
</script>

<style scoped>
.span {
  font-size: 3rem;
  color: white;
  font-family: "raleway";
  font-weight: 200;
}
.scrollnav {
  position: fixed;
  display: flex;
  justify-content: space-around;
  align-items: center;
  background-color: white;
  width: 100%;
  height: 6%;
  font-family: raleway;
}
.scrollactive-item {
  color: black;
  font-weight: 500;
}

#port1 {
  padding-top: 15%;
  padding-right: 50%;
  width: 100%;
  height: 100vh;
  background-color: orange;
}
#port2 {
  padding-top: 15%;
  padding-right: 50%;
  width: 100%;
  height: 100vh;
  background-color: green;
}
#port3 {
  padding-top: 15%;
  padding-right: 50%;
  width: 100%;
  height: 100vh;
  background-color: cadetblue;
}
#port4 {
  padding-top: 15%;
  padding-right: 50%;
  width: 100%;
  height: 100vh;
  background-color: darkolivegreen;
}
</style>
