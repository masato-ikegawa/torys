<template>
  <footer>
    <TweetButton class="tweet" />
    <p>2020 TORYS-HIGH</p>
  </footer>
</template>

<script>
import TweetButton from "./TweetButton.vue";

export default {
  name: "Footer",
  components: {
    TweetButton,
  },
};
</script>

<style scoped>
footer {
  width: 100%;
  height: 100px;
  background: #aaa;
  position: absolute;
  bottom: 0;
}

.tweet {
  margin: 15px auto;
}

p {
  margin: 0;
  font-size: 12px;
  color: white;
  font-weight: bold;
}

@media screen and (min-width: 900px) {
  p{
    font-size: 15px;
  }
}
</style>
