<template>
  <div>
    <b-carousel
      id="carousel-1"
      v-model="slide"
      :interval="4000"
      controls
      indicators
      background="#ababab"
      img-width="1024"
      img-height="480"
      style="text-shadow: 1px 1px 2px #333;"
      @sliding-start="onSlideStart"
      @sliding-end="onSlideEnd">

      <!-- Text slides with image -->
      <a href="#"><b-carousel-slide
        caption="내가 바로 병원이다"
        text="아프면 나한테 와"
        img-src="https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/N69pMl5/4k-health-care-hospital-exterior-with-blue-sky-and-time-lapse-clouds_4jjjqarme__F0000.png">
      </b-carousel-slide></a>

      <!-- Slides with custom text -->
      <a href="#"><b-carousel-slide
        caption="친절한 의사들을 만나는 바로 그 곳!"
        text="시간을 되돌리는듯한 친절 상담 써~~비스"
        img-src="https://cdn2.highdefdigest.com/media/2018/11/27/660/Doctor_Strange_4K.jpg">
        <!-- <h1>이미지 설명 추가 기능</h1> -->
      </b-carousel-slide></a>

      <!-- Slides with image only -->
      <a href="#"><b-carousel-slide
        caption="멋쟁이 사자처럼 7기"
        text="김승태, 이인우, 박선영, 박지환, 최상하, 이채연"
       img-src="https://i.pinimg.com/originals/97/cf/d2/97cfd2d9c778895d522f9cfa9e049d05.jpg">
       <!-- https://picsum.photos/1024/480/?image=58 -->
       </b-carousel-slide></a>

      <!-- Slides with img slot -->
      <!-- Note the classes .d-block and .img-fluid to prevent browser default image alignment -->
      <a href="#"><b-carousel-slide
        caption="프론트 넘나 어려운 것"
        text="2주를 갈아 넣었어버렸다!">
        <img
          slot="img"
          class="d-block img-fluid w-100"
          width="1024"
          height="480"
          src="https://d2v9y0dukr6mq2.cloudfront.net/video/thumbnail/N69pMl5/generic-health-care-modern-hospital-exterior-building-at-night-4k-time-lapse_bgkh2ma0_thumbnail-full03.png"
          alt="image slot"
        >
      </b-carousel-slide></a>

    </b-carousel>
    <!-- 이미지 넘어갈 때 마다 설명 넣을 수 있는 블록 -->
    <!-- <p class="mt-4">
      Slide #: {{ slide }}<br>
      Sliding: {{ sliding }}
    </p> -->
  </div>
</template>

<script>
  export default {
    data() {
      return {
        slide: 0,
        sliding: null
      }
    },
    methods: {
      onSlideStart(slide) {
        this.sliding = true
      },
      onSlideEnd(slide) {
        this.sliding = false
      }
    }
  }
</script>