const {config} = require('../config');
const mongoose = require('mongoose');

mongoose.Promise=global.Promise;

mongoose.connect(config.mongoUri);
console.log('conectado a mongodb');