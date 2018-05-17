var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    context: __dirname,

    entry: './assets/js/index',

    mode: 'none',

    output: {
        path: path.resolve('./dist'),
        filename: '[name]-[hash].js',
    },

    plugins: [
        new BundleTracker({ filename: './webpack-stats.json' }),
    ],

    module: {
        
    },
}