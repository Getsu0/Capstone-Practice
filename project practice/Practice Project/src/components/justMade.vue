<script setup>
import { fetchWasteItems } from '@/api';
import { ref, onMounted } from 'vue';

const wasteItems = ref([]);

onMounted(async () => {
    wasteItems.value = await fetchWasteItems();
});
</script>

<template>
    <div class="just-made-container">
        <h2>Waste Items</h2>
        <ul>
            <li v-for="item in wasteItems" :key="item.id">
                {{ item.name }} - {{ item.category }} ({{ item.quantity }} {{ item.unit }})
            </li>
        </ul>
    </div>
</template>


<style scoped>
.just-made-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 20px;
  background-color: #f0f0f0;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin: 20px auto;
  max-width: 800px;
}

.just-made-container h2 {
  font-size: 24px;
  margin-bottom: 20px;
  color: #333;
  text-align: center;
}

.just-made-container ul {
  list-style-type: none;
  padding: 0;
  width: 100%;
}

.just-made-container li {
  background-color: #fff;
  margin-bottom: 10px;
  padding: 10px;
  border-radius: 5px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s, box-shadow 0.2s;
}

.just-made-container li:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
</style>