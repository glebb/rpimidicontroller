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
    padding: '22px 0px',
  },
};

class SimpleSlider extends React.Component {
  state = {
    value: this.props.position,
  };

  cc = "0";

  handleChange = (event, value) => {
    this.setState({ value });
    const url = "/ccset/"+this.cc+"/"+value;
    fetch(url);
  };

  render() {
    const { classes } = this.props;
    const { value } = this.state;
    this.cc = this.props.cc;

    return (
      <div className={classes.root}>
        <Typography id="label">{this.props.name}</Typography>
        <Slider
          classes={{ container: classes.slider }}
          value={value}
          aria-labelledby="label"
          max={127}
          min={0}
          step={9}
          onChange={this.handleChange}
        />
      </div>
    );
  }
}

SimpleSlider.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(SimpleSlider);