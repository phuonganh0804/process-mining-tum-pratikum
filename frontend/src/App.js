import "./App.css";
import result from "./result.png";

import React, { Component } from "react";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      uploadedFile: null,
      algorithm: "",
      dependency: "",
      and: "",
      observation: "",
      relative: "",
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleUpload = this.handleUpload.bind(this);
    this.handleOption = this.handleOption.bind(this);
    this.handleDependency = this.handleDependency.bind(this);
    this.handleAnd = this.handleAnd.bind(this);
    this.handlePositiveObservation = this.handlePositiveObservation.bind(this);
    this.handleRelativeToBest = this.handleRelativeToBest.bind(this);
  }

  handleRelativeToBest(event) {
    this.setState({
      relative: event.target.value,
    });
  }

  handlePositiveObservation(event) {
    this.setState({
      observation: event.target.value,
    });
  }

  handleDependency(event) {
    this.setState({
      dependency: event.target.value,
    });
  }

  handleAnd(event) {
    this.setState({
      and: event.target.value,
    });
  }

  handleChange(event) {
    this.setState({
      uploadedFile: event.target.files[0],
    });
  }

  handleOption(event) {
    this.setState({
      algorithm: event.target.value,
    });
  }

  handleUpload = async (e) => {
    e.preventDefault();
    if (!this.state.uploadedFile) {
      alert("Please first select a file");
      return;
    }
    const data = new FormData();
    data.append("file", this.state.uploadedFile);
    data.append("algorithm", this.state.algorithm);
    data.append("dependency", this.state.dependency);
    data.append("and", this.state.and);
    data.append("observation", this.state.observation);
    data.append("relative", this.state.relative);
    const response = await fetch("/api/upload", {
      method: "post",
      body: data,
    });

    try {
      if (response.ok) {
        alert("File uploaded successfully");
      } else {
        alert("Failed to upload the file due to errors");
      }
    } catch (error) {
      console.error("Error while uploading the file:", error);
      alert("Error occurred while uploading the file");
    }
  };

  render() {
    return (
      <body>
        <h1>Process Mining Tool</h1>
        <div class="parent">
          <div class="input">
            <form>
              <label for="file">
                Select your XES file:
                <input
                  id="file"
                  type="file"
                  accept=".xes"
                  onChange={this.handleChange}
                />
              </label>
              <label for="algorithm">
                Algorithm:
                <select
                  id="algorithm"
                  name="algorithm"
                  onChange={this.handleOption}
                  value={this.state.algorithm}
                >
                  <option value="">--Please choose an option--</option>
                  <option value="Alpha Algorithm">Alpha Algorithm</option>
                  <option value="Heuristic Miner">Heuristic Miner</option>
                </select>
              </label>
              <label for="dependency">
                Dependency threshold:
                <input
                  type="text"
                  placeholder="0.9"
                  value={this.state.dependency}
                  onChange={this.handleDependency}
                />
              </label>
              <label for="and">
                AND-threshold:
                <input
                  type="text"
                  placeholder="0.1"
                  value={this.state.and}
                  onChange={this.handleAnd}
                />
              </label>
              <label for="observation">
                Positive observations threshold:
                <input
                  type="text"
                  placeholder="3"
                  value={this.state.observation}
                  onChange={this.handlePositiveObservation}
                />
              </label>
              <label for="relative">
                Relative to best threshold:
                <input
                  type="text"
                  placeholder="0.05"
                  value={this.state.relative}
                  onChange={this.handleRelativeToBest}
                />
              </label>
              <label for="submit">
                <button id="submit" onClick={this.handleUpload}>
                  Start Mining
                </button>
              </label>
            </form>
          </div>
          <div class="output">
            <img src={result} alt="result" />
          </div>
          <footer>
            <p></p>
          </footer>
        </div>
      </body>
    );
  }
}

export default App;
