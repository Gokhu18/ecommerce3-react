import React from 'react';
import { string, number } from 'prop-types';

export default class Sale extends React.Component {
    render() {
        const { color, size} = this.props;
        return (
            <svg width={size} height={size} viewBox="0 0 128 128" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlnsXlink="http://www.w3.org/1999/xlink">
                <title>Untitled</title>
                <desc>Created with Sketch.</desc>
                <g id="Page-1" stroke="none" stroke-width="1" fill={color} fill-rule="evenodd">
                    <image id="sale" x="0" y="0" width="128" height="128" xlinkHref="data:image/png;base64,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"/>
                </g>
            </svg>
        );
    }
}

Sale.propTypes = {
    color: string,
    size: number
};

Sale.defaultProps = {
    color: 'red',
    size: 40,
};