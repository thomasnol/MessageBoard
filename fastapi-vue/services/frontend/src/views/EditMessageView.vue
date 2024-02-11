<template>
  <section>
    <h1>Edit message</h1>
    <hr/><br/>

    <form @submit.prevent="submit">
      <div class="mb-3">
        <label for="title" class="form-label">Title:</label>
        <input type="text" name="title" v-model="form.title" class="form-control" />
      </div>
      <div class="mb-3">
        <label for="content" class="form-label">Content:</label>
        <textarea
          name="content"
          v-model="form.content"
          class="form-control"
        ></textarea>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </section>
</template>

<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
  name: 'EditMessage',
  props: ['id'],
  data() {
    return {
      form: {
        title: '',
        content: '',
      },
    };
  },
  created: function() {
    this.GetMessage();
  },
  computed: {
    ...mapGetters({ message: 'stateMessage' }),
  },
  methods: {
    ...mapActions(['updateMessage', 'viewMessage']),
    async submit() {
    try {
      let message = {
        id: this.id,
        form: this.form,
      };
      await this.updateMessage(message);
      this.$router.push({name: 'Message', params:{id: this.message.id}});
    } catch (error) {
      console.log(error);
    }
    },
    async GetMessage() {
      try {
        await this.viewMessage(this.id);
        this.form.title = this.message.title;
        this.form.content = this.message.content;
      } catch (error) {
        console.error(error);
        this.$router.push('/dashboard');
      }
    }
  },
});
</script>