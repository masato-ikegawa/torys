<template>
  <div class="container">
    <Header />
    <main>
      <div class="imagepost-wrapper disp">
        <ImagePost @passImageStatus="serveImageStatus" />
      </div>
      <Button @click="dImage()" label="この画像で決定" class="btn disp" />
      <div class="omikuji-wrapper nodisp">
        <Omikuji />
      </div>
      <Button @click="dResult()" label="おみくじを回す" class="btn nodisp" id="act-btn" />
    </main>
    <Footer />
  </div>
</template>

<script>
import axios from "axios";

import Header from "./components/Header.vue";
import Footer from "./components/Footer.vue";
import ImagePost from "./components/ImagePost.vue";
import Omikuji from "./components/Omikuji.vue";
import Button from "./components/Button.vue";

export default {
  name: "App",
  components: {
    Header,
    Footer,
    ImagePost,
    Omikuji,
    Button,
  },
  data() {
    return {
      resultText: "",
      imgData: "",
      result: Number,
      activate: { type: Boolean, default: false },
    };
  },
  methods: {
    serveImageStatus() {
      const btn1 = this.$el.children[1].children[1];
      btn1.id = "act-btn";
    },
    shuffle() {
      var random = Math.floor(Math.random() * 5);
      this.result = random;
      return random;
    },
    dImage() {
      if (this.$el.children[1].children[0].children[0].children[2]) {
        this.imgData = this.$el.children[1].children[0].children[0].children[2].src;
        console.log(this.imgData);
        this.$el.children[1].children[0].classList.remove("disp");
        this.$el.children[1].children[0].classList.add("nodisp");
        const btn1 = this.$el.children[1].children[1];
        btn1.classList.remove("disp");
        btn1.classList.add("nodisp");
        const omikujiwrapper = this.$el.children[1].children[2];
        omikujiwrapper.classList.remove("nodisp");
        omikujiwrapper.classList.add("disp");
        const btn2 = this.$el.children[1].children[3];
        btn2.classList.remove("nodisp");
        btn2.classList.add("disp");
      } else {
        console.log("ないよ");
      }
    },
    dResult() {
      const resValue = this.shuffle();
      if (resValue === 0) {
        this.resultText = "凶";
      } else if (resValue === 1) {
        this.resultText = "末吉";
      } else if (resValue === 2) {
        this.resultText = "小吉";
      } else if (resValue === 3) {
        this.resultText = "中吉";
      } else if (resValue === 4) {
        this.resultText = "大吉";
      }
      this.result = resValue;
      axios.post(
        "http://localhost:5000/upload",
        { result: this.result, img: this.imgData },
        { headers: { "Content-Type": "application/json" } }
      );
    },
  },
};
</script>

<style>
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  background: rgb(253, 234, 126);
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.container {
  width: 100%;
  min-height: 100vh;
  height: 500px;
  position: relative;
  box-sizing: border-box;
}
</style>

<style scoped>
.btn {
  margin: 0 auto;
}

.nodisp {
  display: none;
}

.disp {
  display: block;
}

@media screen and (min-width: 600px) {
  h1 {
    font-size: 18px;
  }
}

@media screen and (min-width: 900px) {
  h1 {
    font-size: 21px;
  }
}

@media screen and (min-width: 1200px) {
  h1 {
    font-size: 24px;
  }
}
</style>
