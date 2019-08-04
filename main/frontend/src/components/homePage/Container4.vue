<template>
  <div class="con4">
    <div class="con4-txt">60데시벨과 함께하는 사람들</div>
    <div class="row"></div>
    <div class="icons">
      <img class="icon1" src="../../assets/medi.png" />
      <img class="icon2" src="../../assets/60db.png" />
      <img class="icon3" src="../../assets/likelion.png" />
    </div>
  </div>
</template>
<script>
export default {};
</script>
<style scoped>
.con4 {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 70vh;
}
.row {
  width: 60%;
  height: 10px;
  border: 1px solid gray;
}
.icons {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.icon1 {
  width: 100px;
  height: 50px;
}
.icon2 {
  width: 100px;
  height: 50px;
}
.icon3 {
  width: 100px;
  height: 50px;
}
</style>

