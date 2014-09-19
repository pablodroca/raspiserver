function HomeViewModel(){
  var self = this;
  
  self.init = function(options){
    self.options = options;

    self.hide = function (itemId) {
      $('#'+itemId).addClass('hide');
    };

    self.show = function (itemId) {
      $('#'+itemId).removeClass('hide');
    };

    $('#led-mode-on').click(function (){
      self.hide('led-mode-on');
      self.show('led-mode-off');
      self.show('led-on');
      self.show('led-off');
      $.get(self.options.ledModeOnUrl).fail(function() {alert('Error');});
    });
    $('#led-mode-off').click(function (){
      self.show('led-mode-on');
      self.hide('led-mode-off');
      self.hide('led-on');
      self.hide('led-off');
      $.get(self.options.ledModeOffUrl).fail(function() {alert('Error');});
    });
    $('#led-on').click(function (){
      $.get(self.options.ledOnUrl).fail(function() {alert('Error');});
    });
    $('#led-off').click(function (){
      $.get(self.options.ledOffUrl).fail(function() {alert('Error');});
    });
    $('#shutdown').click(function (){
      $('#confirm-shutdown').modal('show');
    });
    $('#shutdown-ok').click(function (){
      $.get(self.options.shutdownUrl, null, function(result){
        alert(result);
      });
      $('#confirm-shutdown').modal('close');
    });
  };
}
