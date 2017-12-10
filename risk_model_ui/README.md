# Risk Model UI

## Overview

This is a single page web application developed with [Vue.js](https://vuejs.org) and [Webapack](https://webpack.js.org/).

The app retrieves risk types (more precisely their definitions, i.e., name description, field types) from the back-end service and builds a form with inputs corrresponding to each the risk type's field types.

The UI consists of a main page that simply list all of the available risk types and of a detail page each risk type. On clicking on an specific risk type, the user navigates to a detail page that shows the riks type corresponding form.

## Developer's Guide

For my own future reference, I'm going to document the entire process of creating a UI with Vue.js/Webpack.

### Setting Up Vue CLI

Install [nodejs](https://nodejs.org/en/) (at least version 6 is required):

    curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
    sudo apt-get install nodejs

Install [vue-cli](https://github.com/vuejs/vue-cli):

    sudo npm install -g vue-cli

### Creating a Project

Run the following command to create a project skeleton using the simple [webpack](https://webpack.js.org/) template:

    vue init webpack-simple risk_model_ui

### Running the App

Install dependencies:

    npm install

Serve with hot reload at localhost:8080:

    npm run dev

### Building the App

Build for production with minification:

    run build


### Bootstrap

Install:

     npm i bootstrap-vue bootstrap@4.0.0-beta.2

Add the following imports to `main.js`:

    import BootstrapVue from 'bootstrap-vue'
    import 'bootstrap/dist/css/bootstrap.css'
    import 'bootstrap-vue/dist/bootstrap-vue.css'
     
    Vue.use(BootstrapVue);


### jQuery

The easiest way is to use [unpkg](https://unpkg.com/#/). Just add the following to your index.html:

    <script src="https://unpkg.com/jquery@3.1.1"></script>