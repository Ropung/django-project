// - 글쓰기와 수정에서 쓸 수 있는 함수
// 제목이 비어있거나 또는 5글자 이하라면 경고창 표시하고 진행멈춤
// 글 내용이 비어있거나 10글자 이하라면 경고창 표시하고 진행멈춤
// 제목이나 글 내용에 바보, 멍청이, 한조 들어있으면 경고창 표시하고 진행멈춤
$(document).ready(function () {
  // alert("제이쿼리 연결");

  $("#formValidate").on("click", function () {
    alert("주문하기 클릭");
    formValidate();
  });
});

function formValidate() {
  order_text = $("#order_text").val();
  price = $("#price").val();
  address = $("#address").val();
  console.log(order_text);

  if (order_text.include("바보", "멍청이", "한조")) {
    alert("욕설 사용금지");
    return false;
  }
  if (order_text == "" && order_text.length <= 10) {
    alert("글 내용이 비어있거나 10글자이하");
    return false;
  }
  if (price == 0 && price < 3000) {
    alert("최소금액은 3000원이상");
    return false;
  }
  if (addres == "" && addres == null) {
    alert("주소공백금지");
    return false;
  }
  return true;
}
