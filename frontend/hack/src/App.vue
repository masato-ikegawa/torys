<template>
  <div class="container">
    <Header />
    <main>
      <div
        class="imagepost-wrapper"
        :class="{ disp: isImgWrapDisp, nodisp: isImgWrapNodisp }"
      >
        <ImagePost @passImageStatus="serveImageStatus" @catchImgData="thisIsImgData" />
      </div>
      <Button
        @click="dImage()"
        label="この画像で決定"
        class="btn"
        :class="{
          disp: isBtnDisp,
          nodisp: isBtnNodisp,
          actBtn: isBtn1Act,
          anactBtn: isBtn1anAct,
        }"
      />
      <p>{{ atension }}</p>
      <div
        class="omikuji-wrapper"
        :class="{ disp: isOmiWrapDisp, nodisp: isOmiWrapNodisp }"
      >
        <Omikuji ref="omikujiRef" />
      </div>
      <Button
        @click="dResult()"
        label="おみくじを回す"
        class="btn actBtn"
        :class="{ disp: isBtn2Disp, nodisp: isBtn2Nodisp }"
      />
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
      isBtnDisp: true,
      isBtnNodisp: false,
      isBtn1Act: false,
      isBtn1anAct: true,
      isBtn2Disp: false,
      isBtn2Nodisp: true,
      isImgWrapDisp: true,
      isImgWrapNodisp: false,
      isOmiWrapDisp: false,
      isOmiWrapNodisp: true,
      isDataImgReceive: false,
      atension: "",
    };
  },
  methods: {
    serveImageStatus() {
      this.isBtn1Act = true;
      this.isBtn1anAct = false;
      this.isDataImgReceive = true;
    },
    thisIsImgData(imgData) {
      this.imgData = imgData;
      if (this.imgData) {
        this.atension = "";
      }
    },
    shuffle() {
      var random = Math.floor(Math.random() * 5);
      this.result = random;
      return random;
    },
    dImage() {
      if (this.isDataImgReceive && this.imgData) {
        this.isImgWrapDisp = false;
        this.isImgWrapNodisp = true;
        this.isBtnDisp = false;
        this.isBtnNodisp = true;
        this.isOmiWrapDisp = true;
        this.isOmiWrapNodisp = false;
        this.isBtn2Nodisp = false;
        this.isBtn2Disp = true;
      } else {
        this.atension = "画像を選択してください";
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
      this.$refs.omikujiRef.loading();
      this.isBtn2Nodisp = true;
      this.isBtn2Disp = false;
      axios
        .post(
          "http://54.150.148.100/upload",
          { result: this.result, img: this.imgData },
          { headers: { "Content-Type": "application/json" } }
        )
        .then((res) => {
          console.log("登録完了");
          console.log("res:", res);
        })
        .catch((err) => {
          console.log(err);
          this.$refs.omikujiRef.err();
        });
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

p {
  text-align: center;
  font-size: 8px;
  color: rgb(250, 80, 60);
  font-weight: bold;
  margin-top: 4px;
  margin-bottom: 4px;
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
  p {
    font-size: 10px;
    margin-top: 6px;
    margin-bottom: 6px;
  }
}

@media screen and (min-width: 1200px) {
  h1 {
    font-size: 24px;
  }
}
</style>
