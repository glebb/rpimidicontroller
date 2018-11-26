import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import IconButton from '@material-ui/core/IconButton';
import CancelOutlined from '@material-ui/icons/CancelOutlined';

const styles = theme => ({
  button: {
    position: 'absolute',
    top: 36,
    right: 5,
    left: 'auto',
    bottom: 'auto',
    margin: 0,
    padding: 0,


  },
  input: {
    display: 'none',
  },
  bContainer: {
  },
});

function QuitButton(props) {
  const { classes } = props;

  function handleQuitClick() {
    fetch('/quit') 
  }

  return (
    <div className={classes.bContainer} >
      <IconButton className={classes.button} aria-label="Quit" onClick={handleQuitClick}>
        <CancelOutlined />
      </IconButton>
    </div>
  );
}

QuitButton.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(QuitButton);