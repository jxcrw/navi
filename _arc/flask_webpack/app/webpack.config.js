// TODO: Get hot module reloading working: https://medium.com/@rajaraodv/webpack-hot-module-replacement-hmr-e756a726a07

const glob = require("glob-all");
const path = require('path');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const WebpackMd5Hash = require('webpack-md5-hash');
const PurifyCSSPlugin = require('purifycss-webpack');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const ManifestRevisionPlugin = require('manifest-revision-webpack-plugin');

module.exports = {
  entry: { main: './assets/scripts/index.js' },
  output: {
    path: path.resolve(__dirname, 'static'),
    filename: '[name].[hash:3].js',
    publicPath: 'http://localhost:8080/assets/',
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      },
      {
        test: /\.scss$/,
        use: ['style-loader', MiniCssExtractPlugin.loader, 'css-loader', 'sass-loader']
      },
      {
        test: /.(ttf|otf|eot|svg|woff(2)?)(\?[a-z0-9]+)?$/,
        use: [{
          loader: 'file-loader',
          options: {
            name: '[name].[ext]',
            outputPath: 'fonts/',
          }
        }]
      }
    ]
  },
  plugins: [
    // new CleanWebpackPlugin('static', {} ),
    new WebpackMd5Hash(),
    new PurifyCSSPlugin({
      paths: glob.sync([
        path.join(__dirname, './assets/scripts/*.js'),
        path.join(__dirname, './templates/*.html')
      ]),
      // minimize: true,
    }),
    new MiniCssExtractPlugin({filename: '[name].[contenthash:3].css'}),
    new ManifestRevisionPlugin(path.join('', 'manifest.json'), {
        rootAssetPath: './assets',
        ignorePaths: ['/styles', '/scripts',]
    }),
  ],
  devServer: {
    contentBase: path.resolve(__dirname, './templates'),
    watchContentBase: true,
    compress: true,
    port: 8080,
    headers: {
      'Access-Control-Allow-Origin': '*'
    },
  },
};