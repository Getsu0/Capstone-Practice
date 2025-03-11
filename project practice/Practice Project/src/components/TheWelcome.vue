<template>
  <div class="container">
    <div class="content">
      <aside class="sidebar">
        <ul>
          <li @click="showComponent('home')">Home</li>
          <li @click="showComponent('justMade')">Input</li>
        </ul>
      </aside>
      <main class="home" v-if="currentComponent === 'home'">
        <h1>Welcome to Minuti Coffee</h1>
        <p>This is the home page.</p>
        <Graphs />
      </main>
      <main class="justMade" v-if="currentComponent === 'justMade'">
        <justMade />
      </main>
    </div>
    <footer class="footer">
      <p>&copy; Code Catalyst </p>
    </footer>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import Graphs from './Graphs.vue';
import justMade from './justMade.vue';

const currentComponent = ref('home');

const showComponent = (component) => {
  currentComponent.value = component;
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&family=Open+Sans:wght@400;600&display=swap');

.container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  font-family: 'Roboto', sans-serif;
}

.content {
  display: flex;
  flex: 1;
  background-color: #F4EBD0;
}

.sidebar {
  background-color: #AF9164;
  padding: 20px;
  width: 200px;
  flex-shrink: 0;
  font-family: 'Open Sans', sans-serif;
}

.sidebar ul {
  list-style-type: none;
  padding: 0;
  font-weight: bold;
}

.sidebar li {
  margin: 20px 0;
  background-color: #F7F3E3;
  border: 1px solid #fff;
  padding: 10px;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s, transform 0.3s;
}

.sidebar li:hover {
  background-color: #ffeb3b;
  transform: translateY(-2px);
}

.home, .justMade {
  flex: 1;
  text-align: center;
  padding: 20px;
}

.footer {
  background-color: #6F1A07;
  text-align: center;
  padding: 10px;
  color: #fff;
}
</style>

