<template>
  <div id="loading"></div>
</template>

<script>
export default {
  name: "Loading",
};
</script>

<style scoped>
#loading {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  margin-left: auto;
  margin-right: auto;
  margin-top: 200px;
  width: 7px;
  height: 7px;
  border-radius: 50%;
  box-shadow: 0 -30px 0 0 #bbb, 15px -26px 0 0 #aaa, 26px -15px 0 0 #999, 30px 0 0 0 #888,
    26px 15px 0 0 #777, 15px 26px 0 0 #666, 0 30px 0 0 #555, -15px 26px 0 0 #444,
    -26px 15px 0 0 #333, -30px 0 0 0 #222, -26px -15px 0 0 #111, -15px -26px 0 0 #000;
  animation: loading 1s infinite steps(12, start);
}

@keyframes loading {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}
</style>
