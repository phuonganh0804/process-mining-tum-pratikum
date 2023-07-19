import "./App.css";

import React, { Component } from "react";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      uploadedFile: null,
      algorithm: "",
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleUpload = this.handleUpload.bind(this);
    this.handleOption = this.handleOption.bind(this);
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
        <div>
          <h1>Process Mining Tool</h1>
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
              Mining algorithm:
              <datalist id="algorithm" name="algorithm">
                <option value="">--Please choose an option--</option>
                <option value="Alpha Algorithm"></option>
                <option value="Heuristic Miner"></option>
              </datalist>
              <input
                name="algorithm"
                list="algorithm"
                onChange={this.handleOption}
              />
            </label>
            <label for="submit">
              <button id="submit" onClick={this.handleUpload}>
                Upload
              </button>
            </label>
          </form>
          <footer>
            <p>
              <a href="http://www.freepik.com">Designed by Freepik</a>
            </p>
          </footer>
        </div>
      </body>
    );
  }
}

export default App;
