import React, { Component } from 'react';
import './RegisteredServicesMenu.css';


class Menu extends Component {
    render() {
        return (
            <ul className="drop-down-menu drop-down-inner open">
                <li><a href="#">PAGE 1</a></li>
                <li><a href="#">PAGE 2</a></li>
            </ul>
        );
    }
}

export default Menu;
