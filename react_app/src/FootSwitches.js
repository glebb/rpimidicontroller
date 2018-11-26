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
      <Button variant="contained" color="default"   size="large" style={buttonStyle}  className={this.classes.button} onClick={(e) => this.handleClick(49)}>
      FS1
      </Button><br/>
      <Button variant="contained" color="default"  size="large" style={buttonStyle}   className={this.classes.button} onClick={(e) => this.handleClick(50)}>
      FS2
      </Button><br/>
      <Button variant="contained" color="default" size="large" style={buttonStyle}  className={this.classes.button} onClick={(e) => this.handleClick(51)}>
      FS3
      </Button><br/>
      <Button variant="contained" color="default"   size="large" style={buttonStyle}  className={this.classes.button} onClick={(e) => this.handleClick(52)}>
      FS4
      </Button><br/>
      <Button variant="contained" color="default"  size="large" style={buttonStyle}   className={this.classes.button} onClick={(e) => this.handleClick(53)}>
      FS5
      </Button><br/>
      </p>
    </div>)
  };
}

Blocks.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(Blocks);