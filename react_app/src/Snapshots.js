import React from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';


const buttonStyle = {
  margin: 10
};

const styles = theme => ({
  button: {
    margin: theme.spacing.unit,
    marginBottom: 10
  },
});

class SnapshotButtons extends React.Component {
  constructor(props) {
      super(props);
      this.classes = props;
 
    }

    handleClick = (value) => {
      fetch('/ccset/69/' + value)
  }
 
render() {
    return (
    <div>
        <p>
      <Button variant="contained" color="default" size="medium" style={buttonStyle} className={this.classes.button}onClick={(e) => this.handleClick(0)}>
        1
      </Button>
      <Button variant="contained" color="default"   size="medium" style={buttonStyle} className={this.classes.button}onClick={(e) => this.handleClick(1)}>
        2
      </Button>
      <Button variant="contained" color="default"  size="medium"  style={buttonStyle} className={this.classes.button}onClick={(e) => this.handleClick(2)}>
        3
      </Button>
      {/*<br/>
      <Button variant="outlined" color="default" style={buttonStyle} className={this.classes.button}onClick={(e) => this.handleClick(9)}>
        Previous
      </Button>
      <Button variant="outlined" color="default" style={buttonStyle} className={this.classes.button}onClick={(e) => this.handleClick(8)}>
        Next
      </Button> */}
      </p>
    </div>
  );
}
}

SnapshotButtons.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(SnapshotButtons);