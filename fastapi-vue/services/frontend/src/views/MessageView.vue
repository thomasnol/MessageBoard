<template>
  <div v-if="message">
    <p><strong>Title:</strong> {{ message.title }}</p>
    <p><strong>Content:</strong> {{ message.content }}</p>
    <p><strong>Author:</strong> {{ message.author.username }}</p>

    <div v-if="user.id === message.author.id">
      <p><router-link :to="{name: 'EditMessage', params:{id: message.id}}" class="btn btn-primary">Edit</router-link></p>
      <p><button @click="removeMessage()" class="btn btn-secondary">Delete</button></p>
    </div>
  </div>
</template>


<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
  name: 'MessageView',
  props: ['id'],
  async created() {
    try {
      await this.viewMessage(this.id);
    } catch (error) {
      console.error(error);
      this.$router.push('/dashboard');
    }
  },
  computed: {
    ...mapGetters({ message: 'stateMessage', user: 'stateUser'}),
  },
  methods: {
    ...mapActions(['viewMessage', 'deleteMessage']),
    async removeMessage() {
      try {
        await this.deleteMessage(this.id);
        this.$router.push('/dashboard');
      } catch (error) {
        console.error(error);
      }
    }
  },
});
</script>