<template>
  <v-carousel
    class="v-carousel"
    height="63vh"
    :show-arrows="false"
    :hide-delimiters="hideDelimiters"
    :cycle="cycle"
    :continuous="true"
  >
    <v-carousel-item v-for="(item,i) in items" :key="i" :src="item.src">
      <div class="carousel-txt" v-if="i===0">
        <p class="carousel-txt-head">
          당신의
          <br />
          <span class="carousel-bold">60데시벨</span>을 채워드립니다.
        </p>
        <br />
        <p class="carousel-txt-main">진료 전 문진표 작성을 통해</p>
        <p class="carousel-txt-main">불편함 없고 정확한 진료를 경험해보세요.</p>
      </div>
      <div class="carousel-txt" v-if="i===1">
        <p class="carousel-txt-head">
          간편한
          <br />모바일
          <span class="carousel-bold">설문조사</span>
        </p>
        <br />
        <p class="carousel-txt-main">협업 의료팀의 자문으로 구성된 설문조사,</p>
        <p class="carousel-txt-main">대기시간을 이용하여 간편하게 작성하세요.</p>
      </div>
      <div class="carousel-txt-3" v-if="i===2">
        <p class="carousel-txt-head">
          <span class="carousel-bold">프로필</span>페이지 관리
        </p>
        <br />
        <p class="carousel-txt-main">나만을 위한 프로필 페이지에서</p>
        <p class="carousel-txt-main">건강기록과 지난 설문이력을 관리하세요.</p>
      </div>
    </v-carousel-item>
  </v-carousel>
</template>
<script>
export default {
  data() {
    return {
      items: [
        {
          src: require("../../assets/pic3.jpg")
        },
        {
          src: require("../../assets/pic5.jpg")
        },
        {
          src: require("../../assets/pic6.jpg")
        }
      ],
      hideDelimiters: true,
      cycle: true,
      showArowsOnHover: true
    };
  }
};
</script>
<style scoped>
* {
  color: rgb(94, 94, 94);
}
.v-carousel {
  height: 65vh;
}
.v-responsive__content {
  height: 100%;
}
.carousel-txt {
  display: flex;
  flex-direction: column;
  padding: 3rem 2.5rem;
  padding-top: 3rem;
}
.carousel-txt-3 {
  display: flex;
  flex-direction: column;
  padding: 3rem 2.5rem;
  padding-top: 3.3rem;
  text-align: center;
}
.carousel-txt-head {
  font-size: 1.6rem;
}
.carousel-bold {
  font-weight: bolder;
  color: rgb(87, 87, 87);
  font-weight: 800;
}
</style>
