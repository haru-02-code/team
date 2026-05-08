//jQuery設定ファイル

//グローバル変数として設定
  let selectedColor = '#3B82F6' ;
// $(function () {}は$(document).ready(function () {}の省略形で
// 意味はHTMLが全部読み込まれた後に実行する
$(function () {
  // 初期色設定
  $('.color-btn').each(function () {
    // const color = ...取得した色を変数に保存。
    const color = $(this).data('color');
    $(this).css('background-color', color);
  });

  $('.color-btn').on('click', function () {

    $('.color-btn').removeClass('active');
    
    $(this).addClass('active');
    selectedColor = $(this).data('color');

    // // task-nameに文字がある時だけ色変更
    if ($('#task-name').val() !== '') {
      $('.add-btn').css('background-color', selectedColor);
    }
  });
});

// 開始・終了日時取得

// 追加ボタン
$(function () {
  // .on('input', function () {
  // テキストボックスやテキストエリアなどの入力フォーム要素の値が
  // 1文字入力・削除されるたびに、即座に処理を実行する
  $('#task-name').on('input', function () {
    // valはvalue(中身)の意味　task-nameの中身を取得
    const taskName = $(this).val();
    
    // 文字が空であれば
    if (taskName === '') {
      $('.add-btn')
      // .propはhtmlの属性(property)を変更するメソッド
      .prop('disabled', true)
      .css('background-color', '#9CA3AF'); }
    // 文字が入っていれば
    else{
      $('.add-btn')
        .prop('disabled', false) //falseで解除
        .css('background-color', selectedColor);
    }
  });
});