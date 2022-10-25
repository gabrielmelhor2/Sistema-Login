$(document).ready(function() {
  $(document).mousemove(function(e){
    TweenLite.to$(body),
    .5,
    {css:
      {
        backgroundPosition: "" + parseInt(event.pageX/8)
      }
    }
  }
}