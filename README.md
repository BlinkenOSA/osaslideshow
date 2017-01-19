# osaslideshow
Micro app to present a configurable slideshow at CEU Library on a FullHD screen.

## Configuration

+ Slide photos should be uploaded to `static/photos` directory.
+ `config/slides.json` file contains the configuration script:

 - `photo:` Filename of the uploaded photo.
 - `text:` Caption, which should be displayed on the bottom of the page.

## Third party application

This micro app uses the amazing library called `better-simple-slideshow` available here: https://github.com/leemark/better-simple-slideshow
