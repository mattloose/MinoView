<template>
<div id='stuff'>
    <p>The Current Time is: {{ currenttime }}
  </p>
  </div>
</template>

<style scoped>
  a {
    color: rgb(50, 174, 110);
    text-decoration: none;
  }

  a:hover {
    color: rgb(40, 56, 76);
  }

  ul {
    list-style-type: none;
    margin-top: 10px;
  }

  li { display: inline-block; }
</style>

<script>
  export default {
    data () {
      return {
      }
    },
    props: ['currenttime', 'minIONdict']
  }
</script>
