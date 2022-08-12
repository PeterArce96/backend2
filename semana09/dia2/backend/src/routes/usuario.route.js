const {Router} = require('express');
const router = Router();

const {getAll,create,update} = require('../controllers/usuario.controller');

router.route('/')
    .get(getAll)
    .post(create)
    
router.route('/:id')
    .put(update)

module.exports = router;