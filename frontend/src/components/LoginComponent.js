import TextField from "@material-ui/core/TextField";
import React from "react";
import Paper from "@material-ui/core/Paper";
import Button from "@material-ui/core/Button";

class LoginComponent extends React.Component {
  render() {
    return (
      <Paper
        style={{
          position: "absolute",
          left: "50%",
          top: "50%",
          transform: "translate(-50%, -50%)",
          width: "344px",
          padding: "32px"
        }}
      >
        <form noValidate autoComplete="off">
          <div>
            <h1>login</h1>
          </div>
          <div>
            <TextField label="Username" fullWidth="true" />
          </div>
          <div>
            <TextField label="Password" fullWidth="true" />
          </div>
          <div>
            <Button
              style={{
                marginTop: "24px"
              }}
              variant="outlined"
            >
              submit
            </Button>
          </div>
        </form>
      </Paper>
    );
  }
}

export default LoginComponent;
