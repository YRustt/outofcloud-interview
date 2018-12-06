import React, { Component } from 'react';
import './News.css';

import Detail from './Detail';
import OtherDetail from './OtherDetail';
import Loader from './Loader';


class News extends Component {
    constructor(props) {
        super(props);
        this.state = {
            news: []
        };
    }

    componentDidMount() {
        const queryString = require('query-string');
        var args = queryString.parse(this.props.location.search);

        if (args.name !== undefined) {
            const url = "/api/news" + this.props.location.search;
            fetch(url)
                .then(response => response.json())
                .then(data => this.setState({ news: data }));
        }

        this.setState({name: args.name});
    }

    render() {
        if (this.state.name !== undefined) {
            if (this.state.news.length === 0) {
                return (<div className="container"><Loader/></div>);
            }
            return (
                <div>
                    <div className="container">
                        <div className="h-600x h-sm-auto">
                            <div className="h-2-3 h-sm-auto oflow-hidden">
                                <Detail name={ this.state.name } curr_news={ this.state.news[0] } div_class="pb-5 pr-5 pr-sm-0 float-left float-sm-none w-2-3 w-sm-100 h-100 h-sm-300x" />

                                <div className="float-left float-sm-none w-1-3 w-sm-100 h-100 h-sm-600x">
                                    <Detail name={ this.state.name } curr_news={ this.state.news[1] } div_class="pl-5 pb-5 pl-sm-0 ptb-sm-5 pos-relative h-50" />
                                    <Detail name={ this.state.name } curr_news={ this.state.news[2] } div_class="pl-5 ptb-5 pl-sm-0 pos-relative h-50" />
                                </div>
                            </div>

                            <div className="h-1-3 oflow-hidden">
                                <Detail name={ this.state.name } curr_news={ this.state.news[3] } div_class="pr-5 pr-sm-0 pt-5 float-left float-sm-none pos-relative w-1-3 w-sm-100 h-100 h-sm-300x" />
                                <Detail name={ this.state.name } curr_news={ this.state.news[4] } div_class="plr-5 plr-sm-0 pt-5 pt-sm-10 float-left float-sm-none pos-relative w-1-3 w-sm-100 h-100 h-sm-300x" />
                                <Detail name={ this.state.name } curr_news={ this.state.news[5] } div_class="pl-5 pl-sm-0 pt-5 pt-sm-10 float-left float-sm-none pos-relative w-1-3 w-sm-100 h-100 h-sm-300x" />
                            </div>
                        </div>
                    </div>

                <section>
                    <div className="container">
                        <div className="row">

                            <div className="col-md-12 col-lg-8">

                                <h4 className="p-title mt-30"><b>ОСТАЛЬНЫЕ НОВОСТИ</b></h4>
                                <div className="row">
                                    {this.state.news.slice(6).map((curr_news, index) => {
                                        return <OtherDetail name={ this.state.name } curr_news={ curr_news } />
                                    })}
                                </div>

                            </div>

                            <div className="col-md-12 col-lg-4">

                                        <h4 className="p-title mt-30"><b>НОВОСТИ С ДРУГОГО СЕРВИСА</b></h4>
                                        <a className="oflow-hidden pos-relative mb-20 dplay-block" href="#">
                                            <div className="wh-100x abs-tlr"><img src="images/polular-1-100x100.jpg" alt=""/></div>
                                            <div className="ml-120 min-h-100x">
                                                <h5><b>Bitcoin Billionares Hidding in Plain Sight</b></h5>
                                                <h6 className="color-lite-black pt-10">by <span className="color-black"><b>Danile Palmer,</b></span> Jan 25, 2018</h6>
                                            </div>
                                        </a>

                                        <a className="oflow-hidden pos-relative mb-20 dplay-block" href="#">
                                            <div className="wh-100x abs-tlr"><img src="images/polular-2-100x100.jpg" alt=""/></div>
                                            <div className="ml-120 min-h-100x">
                                                <h5><b>Bitcoin Billionares Hidding in Plain Sight</b></h5>
                                                <h6 className="color-lite-black pt-10">by <span className="color-black"><b>Danile Palmer,</b></span> Jan 25, 2018</h6>
                                            </div>
                                        </a>

                                        <a className="oflow-hidden pos-relative mb-20 dplay-block" href="#">
                                            <div className="wh-100x abs-tlr"><img src="images/polular-3-100x100.jpg" alt=""/></div>
                                            <div className="ml-120 min-h-100x">
                                                <h5><b>Bitcoin Billionares Hidding in Plain Sight</b></h5>
                                                <h6 className="color-lite-black pt-10">by <span className="color-black"><b>Danile Palmer,</b></span> Jan 25, 2018</h6>
                                            </div>
                                        </a>

                                        <a className="oflow-hidden pos-relative mb-20 dplay-block" href="#">
                                            <div className="wh-100x abs-tlr"><img src="images/polular-4-100x100.jpg" alt=""/></div>
                                            <div className="ml-120 min-h-100x">
                                                <h5><b>Bitcoin Billionares Hidding in Plain Sight</b></h5>
                                                <h6 className="color-lite-black pt-10">by <span className="color-black"><b>Danile Palmer,</b></span> Jan 25, 2018</h6>
                                            </div>
                                        </a>


                            </div>

                        </div>
                    </div>
                </section>
            </div>

            );
        } else {
            return (
                <div>Не указан сервис</div>
            );
        }
    }
}

export default News;