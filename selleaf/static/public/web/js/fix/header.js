// header 부분
// 통합검색 인풋에 뭔가를 치면 x버튼이 생기게
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

// 강사 로그인 시 글쓰기 버튼 눌렀을 때 강의 시작하기가 생겨야함 원래는 없어야하고
const WriteLetterBtnModal = document.querySelectorAll(".header-content-photo");
WriteLetterBtnModal[4].style.display = "none";

// 헤더부분에 로그인 | 회원가입 | 고객센터를 로그인이 됬을땐 아이콘 아이콘 아이콘 이런식으로 보여야하기 때문에
// 그 부분 구현 코드
const userinfos = document.querySelectorAll(".header-info-each");
const headerscrap = document.querySelector(".header-scrap-a");
const headeralarm = document.querySelector(".header-alarm-a");
const headerWriteLetterBtn = document.querySelector(".header-write-button");
const headeralarmPointer = document.querySelector(".header-alarm-pointer");
const headerkakaoIcon = document.querySelector(".header-kakao-button");
const isLogin = true;
const teacherLogin = false;

if (isLogin) {
  userinfos.forEach((info) => {
    info.style.display = "none";
  });
  if (teacherLogin) {
    WriteLetterBtnModal[4].style.display = "flex";
  }
} else {
  headerWriteLetterBtn.style.display = "none";
  headerscrap.style.display = "none";
  headeralarm.style.display = "none";
  headerkakaoIcon.style.display = "none";
}

// 알람 버튼 클릭하면 빨간 동그라미 없어지게 하는 구현 코드
// headerkakaoIcon.addEventListener("click", () => {
//   headeralarmPointer.style.display = "none";
// });

// 카카오 아이콘 눌렀을 때 모달창 구현 코드
const myPagemodal = document.querySelector(".header-mymenumodal-wrap");

document.addEventListener("click", (e) => {
  if (!e.target.closest(".header-mymenumodal-wrap")) {
    if (e.target.closest(".header-kakao-button")) {
      myPagemodal.classList.toggle("myPagemodalOpen");
      return;
    }
    myPagemodal.classList.remove("myPagemodalOpen");
  }
});

// 글쓰기 버튼을 클릭하면 모달이 생성되고 다시 클릭하면 모달이 없어져야함
// 대신 화면의 다른 부분을 클릭해도 모달이 없어져야함
const modalButton = document.querySelector(".header-write-wrap");
const modal = document.querySelector(".header-post-wrap");

document.addEventListener("click", (e) => {
  if (!e.target.closest(".header-post-wrap")) {
    if (e.target.closest(".header-write-wrap")) {
      modal.classList.toggle("modalOpen");
      return;
    }
    modal.classList.remove("modalOpen");
  }
});