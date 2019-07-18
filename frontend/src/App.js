import React, { Component } from 'react';

class App extends Component {
  state = {
    targets: []
  };

  async componentDidMount() {
    try {
      const res = await fetch('http://localhost:8000/incxosii_api/target/');
      const targets = await res.json();
      this.setState({
        targets
      });
    } catch (e) {
      console.log(e);
    }
  }

  render() {
    return (
      <div>
        {this.state.targets.map(item => (
          <div key={item.results.targetID}>
            <h1>{item.results.target_title}</h1>
            <span>{item.results.target_description}</span>
          </div>
        ))}
      </div>
    );
  }
}

export default App;