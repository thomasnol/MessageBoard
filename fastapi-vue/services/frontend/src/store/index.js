import { createStore } from "vuex";

import messages from './modules/messages';
import users from './modules/users';

export default createStore({
  modules: {
    messages,
    users,
  }
});