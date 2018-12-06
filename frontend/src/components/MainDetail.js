import React, { Component } from 'react';

import './MainDetail';


class MainDetail extends Component {
    constructor(props) {
        super(props);
        this.state = {};
    }

    componentDidMount() {
        const queryString = require('query-string');
        var args = queryString.parse(this.props.location.search);

        this.setState({
            name: args.name,
            url: args.url
        })

        var url = "/api/grub" + this.props.location.search;
        fetch(url)
            .then(response => response.json())
            .then(data => this.setState(data));
    }

    render() {
        if (this.state.title === undefined) {
            return (<div>Данные загружаются</div>);
        }

        console.log(this.state);
        var image = this.state.image !== undefined ? this.state.image[0] : undefined;
        var title = this.state.title;

        return (
            <div>
                <section className="ptb-0">
                    <div className="mb-30 brdr-ash-1 opacty-5"></div>
                    <div className="container">
                        <a className="mt-10"><i className="mr-5 ion-ios-home"></i>Home<i className="mlr-10 ion-chevron-right"></i></a>
                        <a className="mt-10 color-ash" href="single-page.html">Single Blog</a>
                    </div>
                </section>

                <section>
                    <div className="container">
                        <div className="row">

                            <div className="col-md-12 col-lg-8">
                                { image !== undefined && <img src={ image } alt=""/> }
                                <h3 className="mt-30"><b>{ title }</b></h3>
                                { this.state.content.map((item, idx) => {
                                    return (<p className="mtb-15">{ item }</p>);
                                }) }

                                <div className="float-left-right text-center mt-40 mt-sm-20">

                                    <ul className="mb-30 list-li-mt-10 list-li-mr-5 list-a-plr-15 list-a-ptb-7 list-a-bg-grey list-a-br-2 list-a-hvr-primary ">
                                        <li><a href="#">MULTIPURPOSE</a></li>
                                        <li><a href="#">FASHION</a></li>
                                        <li className="mr-0"><a href="#">BLOGS</a></li>
                                    </ul>
                                    <ul className="mb-30 list-a-bg-grey list-a-hw-radial-35 list-a-hvr-primary list-li-ml-5">
                                        <li className="mr-10 ml-0">Share</li>
                                        <li><a href="#"><i className="ion-social-facebook"></i></a></li>
                                        <li><a href="#"><i className="ion-social-twitter"></i></a></li>
                                        <li><a href="#"><i className="ion-social-google"></i></a></li>
                                        <li><a href="#"><i className="ion-social-instagram"></i></a></li>
                                    </ul>

                                </div>

                            </div>

                            <div className="d-none d-md-block d-lg-none col-md-3"></div>
                            <div className="col-md-6 col-lg-4">
                                <h4 className="p-title"><b>POPULAR POSTS</b></h4>
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
    }
}


export default MainDetail;
