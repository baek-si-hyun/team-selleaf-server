// 마이페이지/설정/회원정보수정 js 파일

/*
    별명 입력란에 아무것도 입력되지 않았을 경우
    input 테두리 색, focus 되었을 때 box-shadow 색 변경

    아래쪽 user-info-error(div) 에 innerText 추가
*/

// 필요한 객체 가져오기
const nicknameInput = document.querySelector(".user-name-input-form");
const nicknameErrorWrap = document.querySelector(
  ".user-name-input-wrap .user-info-error"
);

// 출력할 메세지 변수화
const mustNeededMsg = "필수 입력 항목입니다."; // 미입력 오류
const lessThanTwoMsg = "2자 이상 입력해주세요."; // 2자 이하(1자) 오류
const moreThanFifteenMsg = "15자 이하로 입력해주세요."; // 15자 초과 오류

// 별명 정규식
const nicknameRegex = /^[A-Za-z0-9ㄱ-ㅎㅏ-ㅣ가-힣\s]{2,15}$/;

// 별명 입력창 - keyup 이벤트
// 자판 눌린 시점에서 값이 없거나, 양식에 위반되면 클래스 추가해서 테두리 색 변경
nicknameInput.addEventListener("keyup", (e) => {
  // 만약 키가 눌린 시점에 값이 없거나, 별명 양식이 안 지켜져 있을 경우
  if (!e.target.value || !nicknameRegex.test(e.target.value)) {
    // 별명 입력창에 error 클래스 추가
    // 클래스의 중첩을 막기 위해, 기존에 error 클래스가 없는지부터 확인
    if (!e.target.classList.contains("error")) {
      e.target.classList.add("error");
    }

    // 위 분기로 얻어낸 에러 메세지를 별명 입력창 아래 div 태그에 innerText로 할당
    /*
        값 없어? -> "필수 입력"

        값 있어?
        2글자 미만이야? -> "2글자 이상 입력"

        2글자 이상이야?
        15글자 초과야? -> "15글자 이하로 입력"
    */
    nicknameErrorWrap.innerText = !e.target.value
      ? mustNeededMsg
      : e.target.value.length < 2
      ? lessThanTwoMsg
      : e.target.value.length > 15
      ? moreThanFifteenMsg
      : "";

    // 아래쪽 경우의 수(값 있고 양식까지 맞춤) 실행 안하고 함수 종료
    return;
  }
  // 만약 어떤 값이라도 있고, 양식도 지킨 경우

  // 별명 입력창의 error 클래스 삭제
  e.target.classList.remove("error");

  // 에러 메시지 출력 태그의 innerText 비우기
  nicknameErrorWrap.innerText = "";
});

/*
    생년월일 입력창의 날짜 제한을 현재 시간에 따라 동적으로 변경

    한국 시간이 표준시보다 9시간 빠르기 때문에 그 점까지 반영해서
    오늘로부터 14년 전을 max로 설정
    -> Date.now() 하면 한국 표준시로 잘 가져와짐

    추가로, 직접 타자로 입력할 경우 유효성 검사도 실행할 것
*/
// 필요한 객체 가져오기
const birthInput = document.querySelector(".birth-input-form"); // 생년월일 입력창

// const korTimeDiff = 1000 * 60 * 60 * 9; // 한국 - 표준시의 시차(9시간)
let now = new Date(Date.now()); // 표준시 + 9시간 = 현재 한국 시간

/*
    max 값으로 설정할 14년 전 날짜 만들기
    
    1. 오늘 날짜를 새로운 변수에 할당
    2. 새로운 변수의 year에서 -14 하기
*/
let maxDate = now;
maxDate.setFullYear(now.getFullYear() - 14);

// 14년 전 날짜를 생년월일 입력창의 max로 설정
birthInput.max = maxDate.toISOString().substring(0, 10);

/*
    프로필 이미지 클릭 시, 컴퓨터 내 이미지 불러오기 이벤트 발생

    이미지를 불러올 경우, 이미지 삭제 버튼(image-delete-button)의
    display를 flex로 변경해서 보이게 함
*/
// 필요한 객체 가져오기
const newImageInput = document.querySelector("#new-image"); // 프로필 이미지 입력칸
const imageDeleteButton = document.querySelector(".image-delete-button"); // 이미지 삭제 버튼
const currentImage = document.querySelector(".current-profile-image"); // 화면에 표시되는 현재 이미지

// 이미지 파일인지를 검사하기 위해, 유효한 형식들을 배열로 만들어놓음
const imageTypes = [];

/* 
    프로필 이미지 입력창 - change 이벤트

    프로필 이미지 클릭하면 label로 연결된 파일 입력창(input)이 표시됨.
    파일을 불러와서 해당 input의 value가 변경될 때 이벤트 발생
*/
newImageInput.addEventListener("change", (e) => {
  // 불러온 파일을 구조분해 할당으로 변수에 할당
  const [file] = e.target.files;

  // 새로운 파일 리더를 변수에 할당
  const reader = new FileReader();

  // 파일의 경로를 읽어옴
  reader.readAsDataURL(file);

  // 위 과정을 통해 이미지 경로가 로드되면 새로운 이벤트 발생
  reader.addEventListener("load", (e) => {
    // 가져온 이미지 경로를 변수에 할당
    const imagePath = e.target.result;

    // 이미지 삭제 버튼 표시
    imageDeleteButton.style.display = "flex";

    // 해당 경로에서 이미지 가져와서 프로필 사진으로 띄움
    currentImage.style.backgroundImage = `url(${imagePath})`;
  });
});

// 삭제 버튼 - click 이벤트
// 클릭 시, 기존의 프로필 이미지로 원복하고, 삭제 버튼 숨김
imageDeleteButton.addEventListener("click", (e) => {
  // 프로필 이미지 기본값으로 원복
  currentImage.style.backgroundImage = `../../../images/mypage/base-profile-image.avif`;

  // 삭제 버튼 숨김
  e.target.style.display = "none";

  // 파일 입력창 value값 비움
  newImageInput.value = "";
});

/*
  강사 여부에 따라 강의 현황 메뉴 표시/숨김
*/

// 강사 여부
let isTeacher = false;

// 강의 현황메뉴 객체
const myClassMenu = document.querySelector(".teacher");

// 강사면 강의 현황 메뉴 표시, 아니면 숨김
if (isTeacher) {
  myClassMenu.style.display = "inline-block";
} else {
  myClassMenu.style.display = "none";
}

/*
  2/19 추가 - 회원탈퇴 클릭하면 확인 모달창 표시
*/

// 탈퇴 버튼과 탈퇴 확인 모달
const widthdrawButton = document.querySelector(".user-withdrawal");
const confirmModal = document.querySelector(".withdrawal-warning");

// 탈퇴 완료 모달과 그 안의 확인 버튼
const completeModal = document.querySelector(".withdrawal-complete");
const completeButton = document.querySelector(".withdrawal-confirm");

// 회원탈퇴 텍스트 - click 이벤트
widthdrawButton.addEventListener("click", (e) => {
  // a 태그의 링크 이동 기능 방지
  e.preventDefault;

  // 삭제 버튼을 누를 때 확인 모달 표시
  confirmModal.style.display = "block";

  // 확인 버튼 이벤트
  const confirmAction = document.querySelector(".confirm");
  confirmAction.addEventListener("click", () => {
    // 확인 모달 숨김
    confirmModal.style.display = "none";

    // 여기서 모달 한 번 더 띄우기?
    completeModal.style.display = "block";

    // 확인 버튼 클릭하면 모달창 닫힘
    completeButton.addEventListener("click", () => {
      completeModal.style.display = "none";
    });
  });

  // 취소 버튼 이벤트
  const cancelAction = document.querySelector(".confirm-cancel");
  cancelAction.addEventListener("click", () => {
    // 취소를 누르면 confirm 모달 숨김
    confirmModal.style.display = "none";
  });
});
