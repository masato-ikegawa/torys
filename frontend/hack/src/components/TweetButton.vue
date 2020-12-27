<template>
  <a id="tweetbutton" target="_blank" rel="noopener" :href="href()">Tweet</a>
</template>

<script>
export default {
  name: "TweetButton",
  props: {
    after: { type: Boolean, default: false },
  },
  data() {
    return {
      result: "",
    };
  },
  methods: {
    href: function () {
      const url = "http://54.150.148.100";

      if (this.after && this.result != "") {
        const result = this.result;
        const link =
          "http://twitter.com/share?url=" +
          url +
          "&text=ニコニコおみくじで" +
          result +
          "が出ました";
        return link;
      } else {
        const link = "http://twitter.com/share?url=" + url + "&text=ニコニコおみくじ";
        return link;
      }
    },
    resultChange(resultText) {
      this.result = resultText;
    },
  },
};
</script>

<style scoped>
a {
  display: block;
  width: 60px;
  height: 24px;
  font-family: "Helvetica Neue", Arial, sans-serif;
  text-align: center;
  font-size: 15px;
  color: white;
  border: 1px solid #ccc;
  border-radius: 5px;
  background: #1b95e0;
  line-height: 23px;
  text-decoration: none;
  font-weight: bold;
  user-select: none;
}

a:hover {
  background-color: #0c7abf;
}
</style>
