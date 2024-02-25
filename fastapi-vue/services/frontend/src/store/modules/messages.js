import axios from 'axios';

const state = {
  messages: null,
  message: null,
  words: null,
};

const getters = {
  stateMessages: state => state.messages,
  stateMessage: state => state.message,
  stateWords: state => state.words,
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
  async getFreqWords({commit}, numWords) {
    let {data: resData} = await axios.get('messages');
    // const WordList = "A paragraph is a series of sentences that are organized and coherent, and are all related to a single topic. Almost every piece of writing you do that is longer than a few sentences should be organized into paragraphs. This is because paragraphs show a reader where the subdivisions of an essay begin and end, and thus help the reader see the organization of the essay and grasp its main points."
    let WordList = resData.map(message => message.content).join(' ');
    
    const url = 'https://8z7tjvl9r0.execute-api.us-east-1.amazonaws.com/default/CalculateFreq'
    let {data: responseData} = await axios.get(url, {
      params: {
        WordList: WordList,
        numWords: numWords,
      },
      withCredentials: false,
    });
    console.log(responseData);
    // let finalRes = responseData.map(words => words[0]+" ("+words[1]+" times)");
    // finalRes = finalRes.join(', ');
    let frequencies = {};
    for (let i = 0; i < responseData.length; i++) {
      let word = responseData[i][0];
      let frequency = responseData[i][1];
      // frequency already exists in frequencies
      if (frequency in frequencies) {
        frequencies[frequency].push(word);
      }
      // new frequency
      else {
        frequencies[frequency] = [word];
      }
    }
    let topFrequencies = Object.keys(frequencies).sort((a, b) => b - a);
    let finalRes = "";
    for (let i = 0; i < topFrequencies.length; i++) {
      let frequency = topFrequencies[i];
      // console.log(frequency + ": " + frequencies[frequency].join(", "));
      finalRes += frequency + ": " + frequencies[frequency].join(", ") + "\n";
    }
    console.log(finalRes);

    commit('setWords', finalRes);
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
  setWords(state, words){
    state.words = words;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};