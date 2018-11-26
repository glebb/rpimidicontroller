import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import Slider from '@material-ui/lab/Slider';

const styles = {
  root: {
    position: 'relative',
    marginTop: 20,
    touchAction: "none"    
  },
  slider: {
    padding: '12px 0px',
  },
};

class PCSlider extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      value: null,
      rep: ""
    }
  }
  handleChange = (event, value) => {
    this.setState({value: value, rep: "("+value+")"});
    //this.props.globalStateHandler(value)
  };

  handleDragEnd = () => {
    this.props.globalStateHandler(this.state.value);
    const url = "/pcset/"+this.state.value;
    fetch(url);
    this.setState({value: null, rep: ""});
  };  

  render() {
    const { classes } = this.props;

    return (
      <div className={classes.root}>
      
        <Slider
          classes={{ container: classes.slider }}
          value={this.props.globalState}
          aria-labelledby="label"
          max={126}
          min={1}
          step={1}
          onChange={this.handleChange}
          onDragEnd={this.handleDragEnd}
        /> 
        <Typography id="label"> {this.props.globalState} {this.state.rep}</Typography>

      </div>
    );
  }
}

PCSlider.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(PCSlider);