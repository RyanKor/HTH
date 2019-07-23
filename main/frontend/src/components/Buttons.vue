<template>
  <mdb-container class="mt-5">
    <mdb-container>
      <mdb-row class="mdb-lightbox no-margin">
        <mdb-col md="4">
          <figure class = "figure">
            <img src="https://4.imimg.com/data4/AW/TX/MY-23197770/doctor-mask-500x500.jpg" class="img-fluid" alt="">
            <figcaption>의사소통</figcaption>
          </figure>
        </mdb-col>
        <mdb-col md="4" >
          <figure class = "figure">
            <img src="https://post-phinf.pstatic.net/MjAxNzA2MTVfMjMy/MDAxNDk3NDkwOTM0Mjkx.yj5bU8NC6_yXrr4dpUT6amqLnbwka5oC96B-D_uTikMg.K9Anxez7TaCPWnmGD9myFmIR1BeN7ud4wvuUJEPcKSUg.JPEG/GettyImages-488182081.jpg?type=w1200" class="img-fluid" alt="">
            <figcaption>복통</figcaption>
          </figure>
        </mdb-col>
        <mdb-col md="4">
          <figure class = "figure">
            <img src="https://images.pexels.com/photos/1928880/pexels-photo-1928880.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260" class="img-fluid" alt="">
            <figcaption>진찰</figcaption>
          </figure>
        </mdb-col>
        <mdb-col md="4">
          <figure class = "figure">
            <img src="http://www.emedicalnews.com/wp-content/uploads/2013/01/drug-allergies.jpg" class="img-fluid" alt="">
            <figcaption>처방</figcaption>
          </figure>
        </mdb-col>
        <mdb-col md="4">
          <figure class = "figure">
            <img src="https://thewallpaper.co//wp-content/uploads/2016/10/girl-sick-sadness-window-photo-car-mood-wallpaper-hd-wallpapers-4k-amazing-background-wallpapers-samsung-phone-wallpapers-1080p-display-digital-photos-4272x2848.jpg" class="img-fluid" alt="d">
            <figcaption>병 이름</figcaption>
          </figure>
        </mdb-col>
        <mdb-col md="4">
          <figure class = "figure">
            <img src="https://us.123rf.com/450wm/dizanna/dizanna1611/dizanna161100088/66162726-handschrift-alles-andere-mit-marker-konzept-hintergrund.jpg?ver=6" class="img-fluid" alt="">
            <figcaption>기타 문의</figcaption>
          </figure>
        </mdb-col>
      </mdb-row>
    </mdb-container>

  </mdb-container>
</template>
<script>
import { mdbContainer, mdbRow, mdbCol, mdbIcon, mdbBtn, mdbLightbox, mdbCarousel, mdbCarouselItem, mdbCarouselCaption, mdbCard, mdbModal, mdbModalHeader, mdbModalTitle, mdbModalBody, mdbModalFooter, mdbNavItem } from "mdbvue";
export default {
  name: "GalleryPage",
  data() {
    return {

      visible: false,
      index: 0
    };
  },
  methods: {

  },
  components: {
    mdbContainer,
    mdbRow,
    mdbCol,
    mdbIcon,
    mdbBtn,
    mdbLightbox,
    mdbCarousel,
    mdbCarouselItem,
    mdbCarouselCaption,
    mdbCard,
    mdbModal,
    mdbModalHeader,
    mdbModalTitle,
    mdbModalBody,
    mdbModalFooter,
    mdbNavItem
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  @media (min-width: 768px) {
    .carousel-multi-item-2 .col-md-3 {
      float: left;
      width: 25%;
      max-width: 100%; } }

    .carousel-multi-item-2 .card img {
      border-radius: 2px; }

    figure {
      cursor: pointer;
    }
</style>