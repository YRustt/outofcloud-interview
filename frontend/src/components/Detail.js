import React, { Component } from 'react';
import buildUrl from 'build-url';
import './Detail.css';


class Detail extends Component {
    constructor(props) {
        super(props);
        this.state = {}
    }

    componentDidMount() {
        const name = this.props.name;
        const url = this.props.curr_news.link;

        const new_url = buildUrl({
            path: "/api/grub",
            queryParams: { name: name, url: url }
        });

        fetch(new_url)
            .then(response => response.json())
            .then(data => this.setState(data));
    }

    render() {
        if (this.state.title === undefined) {
            return (<div>Статья загружается</div>);
        }
        const image = (this.state.image !== undefined ? this.state.image[0] : "https://cmkt-image-prd.global.ssl.fastly.net/0.1.0/ps/2321248/580/386/m1/fpnw/wm1/cover-.jpg?1487898325&s=6c1df3e0f086a52e0dc4e0a39073a714");
        const title = this.props.curr_news.title;
        const category = this.props.curr_news.category;
        const published = this.props.curr_news.published;

        return (
            <div className={ this.props.div_class }>
                <a className="pos-relative h-100 dplay-block" href="#">
                    <div className="img-bg bg-grad-layer-6"><img src={ image }></img></div>
                    <div className="abs-blr color-white p-20 bg-sm-color-7">
                        <h4 className="mb-10 mb-sm-5"><b>{ title }</b></h4>
                        <ul className="list-li-mr-20">
                            <li><i className="color-primary mr-5 font-12 ion-ios-pricetag"></i><span className="color-primary"><b>{ category }</b></span></li>
                            <li><i className="color-primary mr-5 font-12 ion-ios-calendar"></i>{ published }</li>
                        </ul>
                    </div>
                </a>
            </div>
        );
    }
}

export default Detail;