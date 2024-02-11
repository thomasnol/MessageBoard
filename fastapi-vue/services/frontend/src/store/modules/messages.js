import axios from 'axios';

const state = {
  messages: null,
  message: null
};

const getters = {
  stateMessages: state => state.messages,
  stateMessage: state => state.message,
};

const actions = {
  async createMessage({dispatch}, message) {
    await axios.post('messages', message);
    await dispatch('getMessages');
  },
  async getMessages({commit}) {
    let {data} = await axios.get('messages');
    commit('setMessages', data);
  },
  async viewMessage({commit}, id) {
    let {data} = await axios.get(`message/${id}`);
    commit('setMessage', data);
  },
  // eslint-disable-next-line no-empty-pattern
  async updateMessage({}, message) {
    await axios.patch(`message/${message.id}`, message.form);
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteMessage({}, id) {
    await axios.delete(`message/${id}`);
  }
};

const mutations = {
  setMessages(state, messages){
    state.messages = messages;
  },
  setMessage(state, message){
    state.message = message;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};