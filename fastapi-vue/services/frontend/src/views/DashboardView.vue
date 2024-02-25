<template>
  <div>
    <section>
      <h1>Add new message</h1>
      <hr/><br/>

      <form @submit.prevent="submitForm1">
        <div class="mb-3">
          <label for="title" class="form-label">Title:</label>
          <input type="text" name="title" v-model="form.title" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="content" class="form-label">Content:</label>
          <textarea name="content" v-model="form.content" class="form-control"></textarea>
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </section>

    <br/><br/>

    <section>
      <h1>Messages</h1>
      <hr/><br/>

      <div v-if="messages">
        <div v-if="messages.length">
          <div v-for="message in messages" :key="message.id" class="messages">
            <div class="card" style="width: 18rem;">
              <div class="card-body">
                <ul>
                  <li><strong>Message Title:</strong> {{ message.title }}</li>
                  <li><strong>Author:</strong> {{ message.author.username }}</li>
                  <li><router-link :to="{name: 'Message', params:{id: message.id}}">View</router-link></li>
                </ul>
              </div>
            </div>
            <br/>
          </div>
        </div>
      </div>

      <div v-else>
        <p>Nothing to see. Check back later.</p>
      </div>
    </section>

    <section>
      <h1>Count Most Frequent Words In All Messages</h1>
      <hr/><br/>

      <form @submit.prevent="submitForm2">
        <div class="mb-3">
          <label for="numWords" class="form-label">Number of Words:</label>
          <textarea name="numWords" v-model="form2.numWords" class="form-control"></textarea>
        </div>
        <div class="mb-3">
          <label for="outputArea" class="form-label">Most Common Words and their Associated Frequencies:</label>
          <span readonly name="outputArea" class="textarea form-control" role="textbox" style="white-space: pre-wrap;">{{ words }}</span>
        </div>
        <button type="submit" class="btn btn-primary">Run Query</button>
      </form>
    </section>
  </div>
</template>

<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
  name: 'DashboardView',
  data() {
    return {
      form: {
        title: '',
        content: '',
      },
      form2: {
        numWords: '999',
      },
    };
  },
  created: function() {
    return this.$store.dispatch('getMessages');
  },
  computed: {
    ...mapGetters({ messages: 'stateMessages'}),
    ...mapGetters({ words: 'stateWords'}),
  },
  methods: {
    ...mapActions(['createMessage']),
    async submitForm1() {
      await this.createMessage(this.form);
    },
    ...mapActions(['getFreqWords']),
    async submitForm2() {
      await this.getFreqWords(this.form2.numWords);
    },
  },
});
</script>