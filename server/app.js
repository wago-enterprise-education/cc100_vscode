var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');

var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');

var app = express();

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', indexRouter);
app.use('/users', usersRouter);
/**********************************************************************************************/


/*** endpoints for digital out 1-4 ***/
app.use('/api/v1/do/1', indexRouter);
app.use('/api/v1/do/2', indexRouter);
app.use('/api/v1/do/3', indexRouter);
app.use('/api/v1/do/4', indexRouter);

/*** endpoint for reloading the Homepage (after working with Programming-Site) ***/
app.use('/api/v1/do/reload', indexRouter);

/*** endpoint for returning the current digital-in-data value ***/
app.use('/api/v1/di/value', indexRouter);

/*** endpoints for analog out 1-2 ***/
app.use('/api/v1/ao/1', indexRouter);
app.use('/api/v1/ao/2', indexRouter);

/*** endpoint for the server to use the given javascript-files ***/
app.use("/media/sd/public/javascripts", express.static('/media/sd/public/javascripts'));

module.exports = app;
