import React, { Component } from 'react';

import PathToItems from './form/PathToItems';


class Registration extends Component {
    constructor(props) {
        super(props);
        this.state = {
            name: "",
            url: "",
            path_to_items: ["rss", "channel"],
            item_tag: "item",
            item_fields: {
                title: ["title"],
                link: ["link"],
                desc: ["desc"],
                published: ["pubDate"]
            }
        };
    }

    handleNameChange(evt) {

    }

    handleSubmit(evt) {
        const { name, shareholders } = this.state;
    }

    handlePathToItemsChange(idx) {
        return (evt) => {

        }
    }

    handleRemoveTagFromPathToItems(idx) {
        return (evt) => {

        }
    }

    render() {
        return (
            <div className="container">
                <form onSubmit={this.handleSubmit}>
                    <div className="form-group">
                        <input className="form-control" type="text" placeholder="Service name" value={this.state.name} onChange={this.handleNameChange} />
                    </div>
                    <div className="row">
                        <div className="col-md-12 col-lg-6">
                            <input className="form-control" type="text" placeholder="Url to rss" value={this.state.name} onChange={this.handleNameChange} />

                            <PathToItems
                                path_to_items={ this.state.path_to_items }
                                handleChange={ this.handlePathToItemsChange }
                                handleRemove={ this.handleRemoveTagFromPathToItems }
                            />

                            <input className="form-control" type="text" placeholder="Item tag" value={this.state.item_tag} onChange={this.handleNameChange} />

                            <button className="btn btn-primary">Fields</button>
                            <div className="item_fields">
                                {Object.entries(this.state.item_fields).map((field_info, idx) => (
                                    <div>
                                        <input className="form-control" type="text" placeholder={`Tag #${idx + 1} name`} value={field_info[0]} onChange={this.handlePathToItemsChange(idx)}/>
                                        <div>
                                            <input className="form-control" type="text" placeholder={`Tag #${idx + 1} name`} value={field_info[0]} onChange={this.handlePathToItemsChange(idx)}/>
                                        </div>
                                    </div>
                                ))}
                            </div>
                        </div>
                        <div className="col-md-12 col-lg-6">
                        </div>
                    </div>
                    <button type="submit" className="btn btn-primary">Submit</button>
                </form>
            </div>
        );
    }
}

export default Registration;
