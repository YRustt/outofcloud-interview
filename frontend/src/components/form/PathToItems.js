import React, { Component } from 'react';


class PathToItems extends Component {
    render() {
        return (
            <div>
                <button className="btn btn-primary">Path to items</button>
                {this.props.path_to_items.map((tag, idx) => (
                  <div className="path_to_items">
                    <input
                        className="form-control"
                        type="text"
                        placeholder={`Tag #${idx + 1} name`}
                        value={tag}
                        onChange={this.props.handleChange(idx)}
                    />
                    <button
                        type="button"
                        onClick={this.props.handleRemove(idx)}
                        className="btn btn-primary"
                    >
                        -
                    </button>
                  </div>
                ))}
            </div>
        );
    }
}

export default PathToItems;
