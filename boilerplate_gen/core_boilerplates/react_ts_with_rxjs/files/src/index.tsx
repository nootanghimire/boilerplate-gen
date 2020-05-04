import * as React from 'react';
import * as ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { HashRouter, Route } from 'react-router-dom';


// const store = configureStore();

/*
const Root = () => (
  <Provider store={store}>
    <HashRouter>
      <Route path="/:somePath?" render={(props) => (<div id="something">Welcome</div>)} />
    </HashRouter>
  </Provider>
);

ReactDOM.render(<Root />, document.getElementById('render'));
*/

const Root = () => (
  <div>This is a simple thing</div>
);

ReactDOM.render(<Root />, document.getElementById('somewhere'));

