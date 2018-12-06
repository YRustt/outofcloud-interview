import React, { Component } from 'react';
import { Switch, Route, Link } from 'react-router-dom';
import './App.css';

import News from './components/News';
import Detail from './components/Detail';
import Registration from './components/Registration';
import MainDetail from './components/MainDetail';


class App extends Component {
  render() {
    return (
      <div className="App">
          <header>
                <div className="bg-191">
                        <div className="container">
                                <div className="oflow-hidden color-ash font-9 text-sm-center ptb-sm-5">

                                        <ul className="float-left float-sm-none list-a-plr-10 list-a-plr-sm-5 list-a-ptb-15 list-a-ptb-sm-10">
                                                <li><a href="#">Контактная информация</a></li>
                                        </ul>
                                        <ul className="float-right float-sm-none list-a-plr-10 list-a-plr-sm-5 list-a-ptb-15 list-a-ptb-sm-5">
                                                <li><a className="pl-0 pl-sm-10" href="#"><i className="ion-social-facebook"></i></a></li>
                                                <li><a href="#"><i className="ion-social-twitter"></i></a></li>
                                                <li><a href="#"><i className="ion-social-google"></i></a></li>
                                                <li><a href="#"><i className="ion-social-instagram"></i></a></li>
                                        </ul>

                                </div>
                        </div>
                </div>

                <div className="container">
                        <a className="logo" href="index.html"><img src="images/news-logo.png" alt="Logo"/></a>

                        <a className="menu-nav-icon" data-menu="#main-menu" href="#"><i className="ion-navicon"></i></a>

                        <ul className="main-menu" id="main-menu">
                                <li className="drop-down"><a href="03_single-post.html">СЕРВИСЫ<i className="ion-arrow-down-b"></i></a></li>
                                <li><Link to="/register">ДОБАВИТЬ СЕРВИС</Link></li>
                        </ul>
                        <div className="clearfix"></div>
                </div>
        </header>
        <Switch>
          <Route path='/news' component={News}/>
          <Route path='/detail' component={MainDetail}/>
          <Route path='/register' component={Registration}/>
        </Switch>
      </div>
    );
  }
}

export default App;
