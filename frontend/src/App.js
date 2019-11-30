import React from "react";
import "./App.css";
import LoginComponent from "./components/LoginComponent";

class App extends React.Component {
  render() {
    return (
      <div className="App">
        <LoginComponent />
      </div>
    );
  }
}

export default App;
