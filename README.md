# ceph-performance-grapher

WebApp to plot performance data on the CEPH object store.
The app uses Vue.js in order to modularise all the tests.
Each type of test has its own subset of Vue.js components, making it extremely easy to modularise and
expand the app.

By turning the charts and tables into vue components they can easily be re-used.
At its current stage the app is only used by me and its being developed for my current needs.
If anyone wishes to use it, please email and I will be happy to help.

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report
```

For detailed explanation on how things work, checkout the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).
