import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';

const styles = theme => ({
  button: {
    margin: theme.spacing.unit,
    
  },
  extendedIcon: {
    marginRight: theme.spacing.unit,
  },
});

const tempoStyle = {
    margin: 0,
    top: 'auto',
    right: 20,
    bottom: 20,
    left: 'auto',
    position: 'fixed',
};

const tunerStyle = {
  margin: 0,
  top: 'auto',
  left: 20,
  bottom: 20,
  right: 'auto',
  position: 'fixed',
};

const modeStyle = {
  margin: 0,
  top: 'auto',
  left: 100,
  bottom: 20,
  right: 'auto',
  position: 'fixed',
};

function FloatingActionButtons(props) {
  const { classes } = props;
  function handleTapClick(value) {
    fetch('/ccset/64/127') 
  }
  function handleTunerClick(value) {
    fetch('/cctoggle/68') 
  }
  function handleNextModeClick(value) {
    fetch('/ccset/71/4') 
  }


  return (
    <div>
      <Button variant="fab" style={tempoStyle} color="primary" className={classes.button} onClick={handleTapClick}>
        TAP
      </Button>
      <Button variant="fab" style={tunerStyle} color="primary" className={classes.button} onClick={handleTunerClick}>
        Tuner
      </Button>
      <Button variant="fab" style={modeStyle} color="primary" className={classes.button} onClick={() => handleNextModeClick(1)}>
        Mode
      </Button>

    </div>
  );
}

FloatingActionButtons.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(FloatingActionButtons);