{"filter":false,"title":"picture.js","tooltip":"/user_profile/static/js/picture.js","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":35,"column":0},"action":"insert","lines":["$(function () {","","  var jcrop_api,","      boundx,","      boundy,","      xsize = 200,","      ysize = 200;","  ","  $(\"#crop-picture\").Jcrop({","    aspectRatio: xsize / ysize,","    onSelect: updateCoords,","    setSelect: [0, 0, 200, 200]","  },function(){","    var bounds = this.getBounds();","    boundx = bounds[0];","    boundy = bounds[1];","    jcrop_api = this;","  });","","  function updateCoords(c) {","    $(\"#x\").val(c.x);","    $(\"#y\").val(c.y);","    $(\"#w\").val(c.w);","    $(\"#h\").val(c.h);","  };","","  $(\"#btn-upload-picture\").click(function () {","    $(\"#picture-upload-form input[name='picture']\").click();","  });","","  $(\"#picture-upload-form input[name='picture']\").change(function () {","    $(\"#picture-upload-form\").submit();","  });","","});",""],"id":1}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":27,"column":60},"end":{"row":27,"column":60},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":66,"mode":"ace/mode/javascript"}},"timestamp":1456858953593,"hash":"19f1e40339011b6572b42573e5694c04d1f669fb"}