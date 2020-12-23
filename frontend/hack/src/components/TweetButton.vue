<template>
  <a
    href="http://twitter.com/share?url=http://localhost:8080/&text=ニコニコおみくじ"
    id="tweetbutton"
    target="_blank"
    rel="noopener"
    >Tweet</a
  >
</template>

<script>
export default {
  name: "TweetButton",
};
</script>

<style scoped>
a {
  display: block;
  width: 60px;
  height: 23px;
  font-family: "Helvetica Neue", Arial, sans-serif;
  font-size: 15px;
  color: white;
  border: 1px solid #ccc;
  border-radius: 5px;
  background: #1b95e0;
  line-height: 23px;
  text-decoration: none;
  font-weight: bold;
}

a:hover {
  background-color: #0c7abf;
}
</style>
