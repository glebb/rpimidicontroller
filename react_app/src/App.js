import React, { Component } from 'react';
import './App.css';
import FullWidthTabs from './menu.js'
import CssBaseline from '@material-ui/core/CssBaseline';

import grey from '@material-ui/core/colors/grey';
import { MuiThemeProvider, createMuiTheme } from '@material-ui/core/styles';


const theme = createMuiTheme({
  palette: {
    primary: grey,
    type: 'dark',
  },
});

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      globalState: 1
    }
  }

  globalStateHandler = (data) => {
    this.setState({
      globalState: data,
    })
  }

  render() {
    return (
      <MuiThemeProvider theme={theme}>
      <React.Fragment>
        <CssBaseline />
        <div className="App">
        <FullWidthTabs globalStateHandler={this.globalStateHandler} globalState={this.state.globalState}/>
        </div>
      </React.Fragment>
      </MuiThemeProvider>     
    );
  }
}

export default App;
