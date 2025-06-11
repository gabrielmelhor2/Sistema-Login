$(document).ready(function () {
  $(document).mousemove(function (e) {
    const offsetX = parseInt(e.pageX / 8);
    $('body').css('background-position', `${offsetX}px 0`);
  });
});
