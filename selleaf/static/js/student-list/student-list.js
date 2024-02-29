// 수강생 목록 조회 JS

// 검색창에 글자 입력하면 x버튼 표시, x버튼 클릭하면 내용 전체 삭제
const searchInput = document.querySelector(".hearder-inner-thirddiv-input");
const xbutton = document.querySelector(".hearder-inner-thirddiv-div");

searchInput.addEventListener("keydown", (e) => {
  xbutton.style.display = "flex";
  // 입력한 값 가져오기
  const realInput = searchInput.value.trim();
  if (realInput !== "") {
    xbutton.addEventListener("click", (e) => {
      searchInput.value = "";
      xbutton.style.display = "none";
    });
  } else {
    xbutton.style.display = "none";
  }
});
const borderinput = document.querySelector(".header-fourth-inner-thirddiv");
searchInput.addEventListener("focus", () => {
  borderinput.style.border = "1px solid #134F2C";
});
searchInput.addEventListener("blur", () => {
  borderinput.style.border = "1px solid #DADDE0";
});

// 온라인/오프라인 여부에 따라 표시할 정보 변경
// 온라인/오프라인 여부
const isOnline = false;

// 오프라인일 때 표시할 강의 시간 컬럼
const offlineInfos = document.querySelectorAll(".offline-title, .offline");

// 온라인일 때 표시할 선택 키트 컬럼
const onlineInfos = document.querySelectorAll(".online-title, .online");

// 온라인/오프라인 여부에 따라 보여주는 컬럼 변경
if (isOnline) {
  onlineInfos.forEach((info) => {
    info.style.display = "block";
  });

  offlineInfos.forEach((info) => {
    info.style.display = "none";
  });
} else {
  onlineInfos.forEach((info) => {
    info.style.display = "none";
  });

  offlineInfos.forEach((info) => {
    info.style.display = "block";
  });
}

// 각 내역 클릭하면 동반 수강생 목록 표시
// 각 수강 신청 내역들
const entries = document.querySelectorAll(".class-histories-wrap");

// 각 내역에 click 이벤트 추가
entries.forEach((item) => {
  // 각 내역 별 수강생들의 상세 리스트
  const allStudentList = item.nextElementSibling;

  // 내역 클릭하면 숨겨져있던 상세목록 표시
  item.addEventListener("click", () => {
    allStudentList.classList.contains("open")
      ? allStudentList.classList.remove("open")
      : allStudentList.classList.add("open");
  });
});
