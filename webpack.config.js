var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
var VueLoaderPlugin = require('vue-loader/lib/plugin');

module.exports = {
    context: __dirname,

    entry: './assets/js/index',

    mode: 'none',

    output: {
        path: path.resolve('./assets/bundles'),
        filename: '[name]-[hash].js',
    },

    plugins: [
        new BundleTracker({ filename: './webpack-stats.json' }),
        new VueLoaderPlugin(),
    ],

    module: {
        rules: [
            {
                test: /\.vue$/,
                loader: 'vue-loader'
            },
        ]
    },
}