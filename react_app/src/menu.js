import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import Typography from '@material-ui/core/Typography';
import FloatingActionButtons from "./FloatingActionButtons"
import SnapshotButtons from './Snapshots'
import PresetButtons from './Presets'
import SimpleSlider from './ParamSliders'
import Blocks from './FootSwitches'

function TabContainer(props) {
  return (
    <Typography component="div" style={{ padding: 8 * 3 }}>
      {props.children}
    </Typography>
  );
}

TabContainer.propTypes = {
  children: PropTypes.node.isRequired,
};


const styles = theme => ({
  root: {
    flexGrow: 1,
    textColor: "white",
    width: "100%",
    backgroundColor: theme.palette.background.paper,
  },
  sliders: {
    marginTop: 20
  }
});

class FullWidthTabs extends React.Component {
  constructor(props) {
    super(props);
  }

  state = {
    value: 0,
  };

  handleChange = (event, value) => {
    this.setState({ value });
  };

  handleChangeIndex = index => {
    this.setState({ value: index });
  };

  render() {
    const { classes, theme } = this.props;
    const { value } = this.state;

    return (
      <div className={classes.root}>
        <AppBar position="static" color="default">
          <Tabs
            value={value}
            onChange={this.handleChange}
            fullWidth
          >
            <Tab label="Main" />
            <Tab label="FS" />
            <Tab label="Params" />
          </Tabs>
        </AppBar>
          {value === 0 && <TabContainer dir={theme.direction}>
          <AppBar position="static" color="default">
          Snapshots for current preset
          </AppBar>
          <SnapshotButtons/>

          <AppBar position="static" color="default">
          Preset Quick Dial
          </AppBar>
          <PresetButtons globalStateHandler={this.props.globalStateHandler} globalState={this.props.globalState}/><br/>
          <AppBar position="static" color="default">
          Expression Pedals
          </AppBar>
          <SimpleSlider name="EXP 1" cc="1" position="127"/>
          <SimpleSlider name="EXP 2" cc="2" position="0"/>

          </TabContainer>}
          {value === 1 && <TabContainer dir={theme.direction}><AppBar position="static" color="default">
          Footswitches
          </AppBar>
          <Blocks/>
          </TabContainer>}
          {value === 2 && <TabContainer dir={theme.direction}>
          <AppBar position="static" color="default">
          Parameters
          </AppBar>
          <div className={classes.sliders}>
            <SimpleSlider name="Param1" cc="80"/>
            <SimpleSlider name="Param2" cc="81"/>
            <SimpleSlider name="Param3" cc="82"/>
            <SimpleSlider name="Param4" cc="83"/>
            </div>
          </TabContainer>}
        <FloatingActionButtons />

      </div>

    );

  }
}

FullWidthTabs.propTypes = {
  classes: PropTypes.object.isRequired,
  theme: PropTypes.object.isRequired,
};

export default withStyles(styles, { withTheme: true })(FullWidthTabs);