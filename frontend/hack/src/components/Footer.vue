<template>
  <footer>
    <p>2020 TORYS-HIGH</p>
  </footer>
</template>

<script>
export default {
  name: "Footer",
};
</script>

<style scoped>
footer {
  width: 100%;
  height: 70px;
  background: #aaa;
  position: absolute;
  bottom: 0;
}

p {
  margin: 0;
  height: 100%;
  font-size: 12px;
  line-height: 70px;
  color: white;
  font-weight: bold;
}

@media screen and (min-width: 600px) {
  p {
    font-size: 15px;
  }
}

@media screen and (min-width: 900px) {
  p {
    font-size: 18px;
  }
}
</style>
