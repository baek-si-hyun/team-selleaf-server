// 페이지가 열릴 때 체크된 박스가 없다면 삭제 버튼 disabled
const deleteBtn = document.querySelector(".delete-button");

// 현재 체크된 박스의 개수를 세는 함수
const countCheckBoxes = () => {
  // 각 체크박스의 상태가 변할 때마다 체크된 박스의 개수를 셈
  const checkedBoxes = document.querySelectorAll("input[type='checkbox']:checked")

  // 체크된 박스가 하나라도 있다고 가정하고 삭제 버튼의 disabled 해제
  deleteBtn.disabled = false;

  // 체크된 박스가 하나도 없다면 삭제 버튼 비활성화, 전체 선택 체크 해제
  if (checkedBoxes.length === 0) {
    deleteBtn.disabled = true;
  }
}

// 페이지가 열렸을 때 체크된 박스 개수를 셈
countCheckBoxes();

// 체크박스 이벤트 추가 기능 함수화
const addCheckBoxEvent = () => {
  // 체크박스 관련 js
  const allCheck = document.querySelector(".all-check");
  const checkboxes = document.querySelectorAll(".checkbox-input");

  // all-check 체크 여부에 따라 checkbox-input 체크 여부 조절
  allCheck.addEventListener("change", function () {
    checkboxes.forEach(function (checkbox) {
      checkbox.checked = allCheck.checked;

      // 현재 체크된 박스 개수를 세서 삭제 버튼의 활성화 여부 조정
      countCheckBoxes();
    });
  });

  // checkbox-input 중 하나라도 체크가 해제되면 all-check 체크 해제
  checkboxes.forEach(function (checkbox) {
    checkbox.addEventListener("change", function () {
      let allChecked = true;
      checkboxes.forEach(function (checkbox) {
        if (!checkbox.checked) {
          allChecked = false;
        }
      });
      allCheck.checked = allChecked;
    });
  });

  // checkbox-input 모두 체크되면 all-check 체크
  checkboxes.forEach(function (checkbox) {
    checkbox.addEventListener("change", function () {
      let allChecked = true;
      checkboxes.forEach(function (checkbox) {
        if (!checkbox.checked) {
          allChecked = false;
        }
      });
      allCheck.checked = allChecked;
    });
  });

  // 체크박스의 체크 상태가 변할 때마다 체크된 박스 개수를 셈
  checkboxes.forEach((checkbox) => {
    checkbox.addEventListener("change", countCheckBoxes);
  });
}
