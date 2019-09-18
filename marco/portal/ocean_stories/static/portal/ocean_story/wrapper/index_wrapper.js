// var _ = require('lodash')
    // curtain = require('./curtain')
    // hackyMarineCadastreLayerConversion = require('./hacky_marine_cadastre_layer_conversion')
    // scrollSpy = require('./scroll_spy')
//     // ol3MapEngine = require('./ol3_map_engine')
//     oceanStoryMap = require('./map')
    // polyfills = require('./polyfills');

function mount(mapElement, story, animate) {
//
  // var map;
//   var mapEngine = ol3MapEngine(mapElement[0], animate);

  app.wrapper.map.setMouseWheelZoom(false);

  function bindScrollAnimationToLinks(selector) {
    if (animate) {
      // copied with modification from
      // http://www.paulund.co.uk/smooth-scroll-to-internal-links-with-jquery
      $(document).ready(function(){
        // only animate intra-page links inside .content
        $(selector).on('click',function (e) {
          e.preventDefault();

          var target = this.hash;
          $target = $(target);

          $('html, body').stop().animate({
            'scrollTop': $target.offset().top
          }, 900, 'swing', function () {
            window.location.hash = target;
          });
        });
      });
    }
  }

  bindScrollAnimationToLinks('a[href^="#"].animate');

  // returns a setter that calls the passed function whenever the value changes
  // this could be useful as part of a utility library
  function callIfChanged(f) {
    var state;
    return function(newState) {
      if (typeof(state) == "undefined" || newState !== state) {
        state = newState;
        f(state);
      }
    }
  }

  curtain($('.curtain'), callIfChanged(function(collapsed){
    console.info('set collapse: '+collapsed);
    mapElement.toggleClass('half', collapsed);
    mapElement.toggleClass('full', !collapsed);
    mapEngine.updateSize();
  }));

  /* recursive function to pull out all layer, sublayer, and companion layer objects */
  function getAllLayers(current_layers, layers_list) {
    if (typeof(current_layers) != "object") {
      current_layers = {};
    }
    for (var i = 0; i < layers_list.length; i++) {
      if (Object.keys(current_layers).indexOf(layers_list[i].id) < 0) {
        current_layers[layers_list[i].id] = layers_list[i];
        if (layers_list[i].hasOwnProperty('subLayers') && layers_list[i].subLayers.length > 0) {
          current_layers = getAllLayers(current_layers, layers_list[i].subLayers);
        }
        if (layers_list[i].hasOwnProperty('companion_layers') && layers_list[i].companion_layers.length > 0) {
          current_layers = getAllLayers(current_layers, layers_list[i].companion_layers);
        }
      }
    }
    return current_layers;
  }

  // $.getJSON("/data_manager/api/layers/", function(data) {
  $.getJSON("/data_manager/get_json", function(data) {  
    if (data.hasOwnProperty('layers')) {
      // data = data.layers;
      data = getAllLayers({}, data.layers);
    }

    var dataLayers = _.indexBy(data, 'id');
  //   _.each(dataLayers, function(d) {
  //     if (d.layer_type == 'ArcRest' && d.url.indexOf('http://coast.noaa.gov/arcgis/rest/services/MarineCadastre') > -1) {
  //       hackyMarineCadastreLayerConversion(d);
  //     }
  //   })
    // os_map = oceanStoryMap(mapEngine, story, dataLayers);
    os_map = mapEngine.updateMap(story, dataLayers);
    scrollSpy('.content', 'a.anchor[id^=\'section-\']', function(sectionIndex){
      // return os_map.goToSection(story, sectionIndex);
      return os_map.goToSection(sectionIndex);
    })
  });
}
//
// module.exports = mount;
//
// window.oceanStory = module.exports;
window.oceanStory = mount;
app.init();
