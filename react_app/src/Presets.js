import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';
import PCSlider from './PCSlider'

const styles = theme => ({
  button: {
    margin: theme.spacing.unit,

  },
  input: {
    display: 'none',
  },
});

function PresetButtons(props) {
  const { classes } = props;
  let selected = props.globalState;

  function handleClick(value) {
    let temp = value;
    if (value === 200) {
      temp = selected -= 1;

    }
    else if (value === 300) {
      temp = selected += 1;

    }

    if (temp < 0) temp = 125;
    if (temp > 125) temp = 0;


    fetch('/pcset/'+temp);
    selected = temp;
    props.globalStateHandler(temp)
  }

  return (
    <div>
        <p>
      {/*<Button variant="contained" color="secondary" size="medium" className={classes.button} onClick={() => handleClick(1)}>
        1
      </Button>
      <Button variant="contained" color="secondary"   size="medium" className={classes.button} onClick={() => handleClick(2)}>
        2
      </Button>
      <Button variant="contained" color="secondary"  size="medium"  className={classes.button} onClick={() => handleClick(3)}>
        3
      </Button>
      <Button variant="contained" color="secondary" size="medium" className={classes.button} onClick={() => handleClick(4)}>
        4
      </Button>
      <Button variant="contained" color="secondary"   size="medium" className={classes.button} onClick={() => handleClick(5)}>
        5
      </Button>
      <Button variant="contained" color="secondary"  size="medium"  className={classes.button} onClick={() => handleClick(6)}>
        6
      </Button>
  <br/> */}
      <Button variant="contained" color="default"  size="medium"  className={classes.button} onClick={() => handleClick(200)}>
        Previous
      </Button>
      <Button variant="contained" color="default"  size="medium"  className={classes.button} onClick={() => handleClick(300)}>
        Next
      </Button>

      </p>
        <PCSlider globalStateHandler={props.globalStateHandler} globalState={props.globalState}/>
    </div>
  );
}

PresetButtons.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(PresetButtons);