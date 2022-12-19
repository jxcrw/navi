const imagemin = require('imagemin');
const PNGImages = 'assets/images/*.png';
const JPEGImages = 'assets/images/*.jpg';
const output = 'static/img';

const imageminMozjpeg = require('imagemin-mozjpeg');

const optimiseJPEGImages = () =>
  imagemin([JPEGImages], output, {
    plugins: [
      imageminMozjpeg({
        quality: 70,
      }),
    ]
  });

optimiseJPEGImages()
  .catch(error => console.log(error));

const imageminPngquant = require('imagemin-pngquant');

const optimisePNGImages = () =>
  imagemin([PNGImages], output, {
    plugins: [
      imageminPngquant({ quality: '65-80' })
    ],
  });

optimiseJPEGImages()
  .then(() => optimisePNGImages())
  .catch(error => console.log(error));