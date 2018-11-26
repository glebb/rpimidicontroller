import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';

const styles = theme => ({
  button: {
    margin: theme.spacing.unit,
    marginBottom: 10
  },
  input: {
    display: 'none',
  },
});

const buttonStyle = {
    margin: 10
};

class Blocks extends Component {
    constructor(props) {
        super(props);
        this.classes = props;
      }

      handleClick = (value) => {
        fetch('/cctoggle/' + value)
    }
   
  render() {
      return (
    <div>
        <p>
      <Button variant="contained" color="default" size="large" style={buttonStyle} className={this.classes.button} onClick={(e) => this.handleClick(11)}>
        1
      </Button><br/>
      <Button variant="contained" color="default"   size="large" style={buttonStyle}  className={this.classes.button} onClick={(e) => this.handleClick(12)}>
        2
      </Button><br/>
      <Button variant="contained" color="default"  size="large" style={buttonStyle}   className={this.classes.button} onClick={(e) => this.handleClick(13)}>
        3
      </Button><br/>
      <Button variant="contained" color="default" size="large" style={buttonStyle}  className={this.classes.button} onClick={(e) => this.handleClick(14)}>
        4
      </Button><br/>
      <Button variant="contained" color="default"   size="large" style={buttonStyle}  className={this.classes.button} onClick={(e) => this.handleClick(15)}>
        5
      </Button><br/>
      <Button variant="contained" color="default"  size="large" style={buttonStyle}   className={this.classes.button} onClick={(e) => this.handleClick(16)}>
        6
      </Button><br/>
      </p>
    </div>)
  };
}

Blocks.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(Blocks);