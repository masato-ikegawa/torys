<template>
  <div class="container">
    <ImageButton />
    <div class="omikuji-wrapper nodisp">
      <h1>ニコニコおみくじ</h1>
      <Button class="btn disp" label="おみくじを回す" @click="tappedBtn"></Button>
      <Button class="btn nodisp" label="もう1度回す" @click="tappedBtn"></Button>
      <Loading class="loading nodisp"></Loading>
      <TweetButton after="true" :result="resultValue" class="tweet nodisp"></TweetButton>
    </div>
    <Footer />
  </div>
</template>

<script lang="ts">
import Button from "./components/Button.vue";
import Loading from "./components/Loading.vue";
import Footer from "./components/Footer.vue";
import TweetButton from "./components/TweetButton.vue";
import ImageButton from "./components/ImageButton.vue";

function omikuji() {
  var random = Math.floor(Math.random() * 16);
  return random;
}

export default {
  name: "App",
  components: {
    Button,
    Loading,
    Footer,
    TweetButton,
    ImageButton,
  },
  data() {
    return {
      resultValue: "",
    };
  },
  methods: {
    tappedBtn() {
      this.$el.children[0].textContent = "Now Loading...";

      this.$el.children[1].classList.remove("disp");
      this.$el.children[1].classList.add("nodisp");

      this.$el.children[2].classList.remove("disp");
      this.$el.children[2].classList.add("nodisp");

      this.$el.children[3].classList.remove("nodisp");
      this.$el.children[3].classList.add("disp");

      this.$el.children[4].classList.remove("disp");
      this.$el.children[4].classList.add("nodisp");

      var result = omikuji();

      setTimeout(() => {
        if (result < 1) {
          this.$el.children[0].textContent = "大凶…";
          this.$data.resultValue = "大凶";
        } else if (result < 3) {
          this.$el.children[0].textContent = "凶…";
          this.$data.resultValue = "凶";
        } else if (result < 6) {
          this.$el.children[0].textContent = "末吉";
          this.$data.resultValue = "末吉";
        } else if (result < 10) {
          this.$el.children[0].textContent = "小吉";
          this.$data.resultValue = "小吉";
        } else if (result < 13) {
          this.$el.children[0].textContent = "中吉";
          this.$data.resultValue = "中吉";
        } else if (result < 15) {
          this.$el.children[0].textContent = "吉！";
          this.$data.resultValue = "吉";
        } else {
          this.$el.children[0].textContent = "大吉！";
          this.$data.resultValue = "大吉";
        }
        this.$el.children[2].classList.remove("nodisp");
        this.$el.children[2].classList.add("disp");

        this.$el.children[3].classList.remove("disp");
        this.$el.children[3].classList.add("nodisp");

        this.$el.children[4].classList.remove("nodisp");
        this.$el.children[4].classList.add("disp");
      }, 1000);
    },
  },
};
</script>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  margin: 0;
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
  padding-bottom: 70px;
  position: relative;
  box-sizing: border-box;
}

h1 {
  font-size: 18px;
  margin-top: 0;
  padding-top: 60px;
}

.btn {
  margin-top: 80px;
  margin-right: auto;
  margin-left: auto;
}

.loading {
  display: none;
}

.tweet {
  margin-top: 30px;
  margin-right: auto;
  margin-left: auto;
}

.disp {
  display: block !important;
}

.nodisp {
  display: none !important;
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
