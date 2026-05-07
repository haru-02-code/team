//jQuery設定ファイル
$(function () {
  // 初期色設定
  $('.color-btn').each(function () {
    const color = $(this).data('color');
    $(this).css('background-color', color);
  });

  $('.color-btn').on('click', function () {

    $('.color-btn').removeClass('active');
    
    $(this).addClass('active');
  });
});