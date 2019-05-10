const {watch, src, dest} = require('gulp');

function copyPyToBuildDirectory(cb) {
    src('*.py').pipe(dest('build/CalculatorFunction'));
    cb();
}

exports.default = function() {
    watch('*.py', copyPyToBuildDirectory);
};