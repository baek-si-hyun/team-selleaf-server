// 페이지가 열릴 때 체크된 박스가 없다면 승인, 삭제 버튼 disabled
const editBtn = document.querySelector(".edit-button");
const deleteBtn = document.querySelector(".delete-button");

// 현재 체크된 박스의 개수를 세는 함수
const countCheckBoxes = () => {
  // 각 체크박스의 상태가 변할 때마다 체크된 박스의 개수를 셈
  const checkedBoxes = document.querySelectorAll("input[type='checkbox']:checked")

  // 체크된 박스가 하나라도 있다고 가정하고 승인, 삭제 버튼의 disabled 해제
  editBtn.disabled = false;
  deleteBtn.disabled = false;

  // 체크된 박스가 하나도 없다면 승인, 삭제 버튼 disabled
  if (checkedBoxes.length === 0) {
    editBtn.disabled = true;
    deleteBtn.disabled = true;
  }
}

// 페이지가 열렸을 때 체크된 박스 개수를 셈
countCheckBoxes();

// 화면에 강사의 정보를 뿌리기 위한 로직
// 페이지가 열렸을 때 강사 정보의 첫 페이지 표시
let page = 1;

// 리스트를 표시할 ul 태그
const ul = document.querySelector("ul.list-content");

// 신청자 정보의 첫 페이지를 화면에 띄워주는 함수
const callFirstEntryList = () => {
  teacherService.getEntryList(page, showTeachers).then((teachers) => {
    ul.innerHTML = teachers;

    // 체크박스 클릭 이벤트 추가
    addCheckBoxEvent();
  });
}

// 페이지가 열렸을 때 위 함수 사용
callFirstEntryList();

// 페이지네이션 이벤트 추가하기

// 승인, 삭제 모달창
document.addEventListener("DOMContentLoaded", function () {
  const deleteButtons = document.querySelectorAll(".delete-button");
  const deleteModalWrap = document.querySelector(".delete-modal-wrap");
  const approveModalWrap = document.querySelector(".approve-modal-wrap");

  // 삭제 모달
  deleteButtons.forEach(function (deleteButton) {
    deleteButton.addEventListener("click", () => {
      deleteModalWrap.style.display = "flex";
    });
  });

  const cancelButton = document.querySelector(".modal-cancel button");
  const confirmButton = document.querySelector(".modal-confirm button");

  // 삭제 모달 취소
  cancelButton.addEventListener("click", () => {
    deleteModalWrap.style.display = "none";
  });

  // 삭제 실행
  confirmButton.addEventListener("click", async () => {
    deleteModalWrap.style.display = "none";
  });

  // 승인 모달
  editBtn.addEventListener('click', () => {
    approveModalWrap.style.display = 'flex';
  });

  const approveCancelBtn = document.querySelector(".approve-modal-cancel button");
  const approveConfirmButton = document.querySelector(".approve-modal-confirm button");

  // 승인 모달 취소
  approveCancelBtn.addEventListener('click', () => {
    approveModalWrap.style.display = 'none';
  });

  // 승인 실행
  approveConfirmButton.addEventListener('click', async () => {
    approveModalWrap.style.display = 'none';

    // 승인할 강사의 id를 담을 빈 문자열
    let approveIds = ``;

    // 이 시점에서 체크된 박스 개수를 세고
    const checkedBoxes = document.querySelectorAll(".checkbox-input:checked");

    // 각 체크박스를 감싸는 li 태그의 id를 approveIds에 추가
    checkedBoxes.forEach((checkbox) => {
      approveIds += `,${checkbox.parentElement.classList[1]}`;
    });

    // 승인할 신청자의 id를 API에 보내서 승인 처리
    teacherService.approveTeachers(approveIds);

    // 페이지 새로고침
    location.reload();
  });
});

// 아래 게시물 창 버튼
const paginationBtn = document.querySelectorAll(".page-count-num");
const paginationBox = document.querySelector(".page");

paginationBox.addEventListener("click", (e) => {
  let pageBtn = e.target.closest("button.page-count-num");
  if (pageBtn) {
    paginationBtn.forEach((item) => {
      item.classList.contains("page-count-num") &&
        item.classList.remove("page-count-num-choice");
    });
    pageBtn.classList.add("page-count-num-choice");
  }
});

// 검색창 눌렀을때 검색바에 아웃라인주기
const searchBar = document.querySelector("label.search-bar");

document.addEventListener("click", (e) => {
  if (e.target.closest("label.search-bar")) {
    searchBar.classList.add("search-bar-checked");
    return;
  }
  searchBar.classList.remove("search-bar-checked");
});

const inputField = document.querySelector(".search-bar input");
const cancelButton = document.querySelector(".search-bar .cancel-logo");
const searchButton = document.querySelector(".search-bar .search-logo");

// 입력 필드에 입력 내용이 변경될 때마다 실행될 함수를 정의합니다.
function handleInputChange() {
  const inputValue = inputField.value.trim(); // 입력 내용을 가져옵니다.

  // 입력 내용이 있을 때
  if (inputValue !== "") {
    cancelButton.style.display = "flex"; // cancel-logo를 보여줍니다.
    searchButton.style.display = "none"; // search-logo를 숨깁니다.
  } else {
    // 입력 내용이 없을 때
    cancelButton.style.display = "none"; // cancel-logo를 숨깁니다.
    searchButton.style.display = "flex"; // search-logo를 보여줍니다.
  }
}

// cancel-logo를 클릭했을 때 실행될 함수를 정의합니다.
function handleCancelClick() {
  inputField.value = ""; // 입력 필드 내용을 지웁니다.
  cancelButton.style.display = "none"; // cancel-logo를 숨깁니다.
  searchButton.style.display = "flex"; // search-logo를 보여줍니다.
}

// 입력 필드에 이벤트 리스너를 추가합니다.
inputField.addEventListener("input", handleInputChange);

// cancel-logo에 클릭 이벤트 리스너를 추가합니다.
cancelButton.addEventListener("click", handleCancelClick);

// 체크박스 클릭 이벤트 함수화
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
