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

// 이런 00 찾고 있나요에 이미지에 마우스 올렸을 때 확대되게 해야함 마우스 벗어나면 축소되게
const searchimg = document.querySelectorAll(".realmain-plantRecommend-photo");
const searchAtag = document.querySelectorAll(
  ".realmain-plantRecommend-profilelink"
);

searchAtag.forEach((atag, i) => {
  atag.addEventListener("mouseover", () => {
    searchimg[i].style.transform = "scale(1.05)";
  });
});

searchAtag.forEach((atag, i) => {
  atag.addEventListener("mouseout", () => {
    searchimg[i].style.transform = "scale(1)";
  });
});

// 이런 00 찾고 있나요? 부분에 슬라이드 바 구현
const nextButton = document.querySelector(".realmain-nextbutton");
const beforeButton = document.querySelector(".realmain-beforebutton");
const beforeButtonDiv = document.querySelector(
  ".realmain-plantRecommend-beforebuttonWrap"
);
const nextButtonUl = document.querySelector(".realmain-plantRecommend-photoul");

nextButton.addEventListener("click", () => {
  nextButtonUl.style.transition = `transform 0.5s`;
  nextButtonUl.style.transform = `translateX(-963.34px)`;
  nextButton.style.display = "none";
  beforeButtonDiv.style.display = "block";
});

beforeButton.addEventListener("click", () => {
  nextButtonUl.style.transition = `transform 0.5s`;
  nextButtonUl.style.transform = `translateX(0px)`;
  nextButton.style.display = "flex";
  beforeButtonDiv.style.display = "none";
});

// 원데이 클래스 부분에 사진 올리면 확대되고 내리면 축소되게 만들어야함
const searchOnedayImg = document.querySelectorAll(".realmain-lecture-photo");
const searchOnedayA = document.querySelectorAll(
  ".realmain-lecture-explanationA"
);

searchOnedayA.forEach((atag, i) => {
  atag.addEventListener("mouseover", () => {
    searchOnedayImg[i].style.transform = "scale(1.05)";
  });
});

searchOnedayA.forEach((atag, i) => {
  atag.addEventListener("mouseout", () => {
    searchOnedayImg[i].style.transform = "scale(1)";
  });
});

// 오늘의 딜 부분 슬라이더바 구현
const todayHotdealnextButton = document.querySelector(
  ".realmain-todayHotdeal-nextbutton"
);
const todayHotdealbeforeButton = document.querySelector(
  ".realmain-todayHotdeal-beforbutton"
);

const todayHotdealnextButtonUl = document.querySelector(
  ".realmain-todayHotdeal-photoWrapUl"
);

todayHotdealnextButton.addEventListener("click", () => {
  todayHotdealnextButtonUl.style.transition = `transform 0.5s`;
  todayHotdealnextButtonUl.style.transform = `translateX(-867px)`;
  todayHotdealnextButton.style.display = "none";
  todayHotdealbeforeButton.style.display = "flex";
});

todayHotdealbeforeButton.addEventListener("click", () => {
  todayHotdealnextButtonUl.style.transition = `transform 0.5s`;
  todayHotdealnextButtonUl.style.transform = `translateX(0px)`;
  todayHotdealnextButton.style.display = "flex";
  todayHotdealbeforeButton.style.display = "none";
});

// 유저들의 강의 평가 부분 축소 확대 코드
const userReviewImg = document.querySelectorAll(".realmain-userReview-img");
const userReviewA = document.querySelectorAll(".realmain-userReview-contentA");

userReviewA.forEach((atag, i) => {
  atag.addEventListener("mouseover", () => {
    userReviewImg[i].style.transform = "scale(1.05)";
  });
});

userReviewA.forEach((atag, i) => {
  atag.addEventListener("mouseout", () => {
    userReviewImg[i].style.transform = "scale(1)";
  });
});

// 베스트 상품의 카테고리 버튼 구현
const categoryButtons = document.querySelectorAll("#btn");
categoryButtons[0].parentNode.classList.add("active");
console.log(categoryButtons);
categoryButtons.forEach((btn) => {
  btn.addEventListener("click", (e) => {
    // 두번째 버튼을 클릭한 순간 반복문을 돌리면서 버튼들에 active 클래스가 있으면 지워줘야함
    categoryButtons.forEach((btn) => {
      btn.parentNode.classList.remove("active");
    });
    btn.parentNode.classList.add("active");
  });
});

// 이런 00 찾고 있나요에 스크랩을 누르면 색이 들어오고 다시 누르면 색이 없어져야함
const scrapPopup = document.querySelector(".scrap-popup-wrap");
const scrapCancel = document.querySelector(".scrap-popup-cancel-wrap");
let timeoutId;
let animationTarget;

const recommendScrapButton = document.querySelectorAll(
  ".realmain-plantRecommend-scrapbutton"
);

recommendScrapButton.forEach((scrap) => {
  scrap.addEventListener("click", () => {
    const img = scrap.querySelector("img");
    const imgSrc = img.getAttribute("src");
    if (imgSrc === "../../../staticfiles/images/scrap-off.png") {
      img.setAttribute("src", "../../../staticfiles/images/scrap-on.png");
      animationTarget && animationTarget.classList.remove("show-animation");
      animationTarget = scrapPopup;
    } else {
      img.setAttribute("src", "../../../staticfiles/images/scrap-off.png");
      animationTarget.classList.remove("show-animation");
      animationTarget = scrapCancel;
    }
    animationTarget.classList.remove("hide-animation");
    animationTarget.classList.add("show-animation");
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => {
      animationTarget.classList.remove("show-animation");
      animationTarget.classList.add("hide-animation");
    }, 3000);
  });
});

// 원데이 클래스, 인기 콘텐츠 부분에 스크랩 on off 기능
const popularScrapButton = document.querySelectorAll(
  ".realmain-lecture-scrapbutton"
);

popularScrapButton.forEach((scrap) => {
  scrap.addEventListener("click", () => {
    const img = scrap.querySelector("img");
    const imgSrc = img.getAttribute("src");
    if (imgSrc === "../../../staticfiles/images/scrap-off.png") {
      img.setAttribute("src", "../../../staticfiles/images/scrap-on.png");
      animationTarget && animationTarget.classList.remove("show-animation");
      animationTarget = scrapPopup;
    } else {
      img.setAttribute("src", "../../../staticfiles/images/scrap-off.png");
      animationTarget.classList.remove("show-animation");
      animationTarget = scrapCancel;
    }
    animationTarget.classList.remove("hide-animation");
    animationTarget.classList.add("show-animation");
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => {
      animationTarget.classList.remove("show-animation");
      animationTarget.classList.add("hide-animation");
    }, 3000);
  });
});

// 오늘의 딜부분에 스크랩 on off 기능
const todayScrapButton = document.querySelectorAll(
  ".realmain-todayHotdeal-scrapbutton"
);

todayScrapButton.forEach((scrap) => {
  scrap.addEventListener("click", () => {
    const img = scrap.querySelector("img");
    const imgSrc = img.getAttribute("src");
    if (imgSrc === "../../../staticfiles/images/scrap-off.png") {
      img.setAttribute("src", "../../../staticfiles/images/scrap-on.png");
      animationTarget && animationTarget.classList.remove("show-animation");
      animationTarget = scrapPopup;
    } else {
      img.setAttribute("src", "../../../staticfiles/images/scrap-off.png");
      animationTarget.classList.remove("show-animation");
      animationTarget = scrapCancel;
    }
    animationTarget.classList.remove("hide-animation");
    animationTarget.classList.add("show-animation");
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => {
      animationTarget.classList.remove("show-animation");
      animationTarget.classList.add("hide-animation");
    }, 3000);
  });
});

// 베스트 상품 부분에 스크랩 on off 기능
const bestproductScrapButton = document.querySelectorAll(
  ".realmain-bestproduct-realPhotoScrapbtn"
);

bestproductScrapButton.forEach((scrap) => {
  scrap.addEventListener("click", () => {
    const img = scrap.querySelector("img");
    const imgSrc = img.getAttribute("src");
    if (imgSrc === "../../../staticfiles/images/scrap-off.png") {
      img.setAttribute("src", "../../../staticfiles/images/scrap-on.png");
      animationTarget && animationTarget.classList.remove("show-animation");
      animationTarget = scrapPopup;
    } else {
      img.setAttribute("src", "../../../staticfiles/images/scrap-off.png");
      animationTarget.classList.remove("show-animation");
      animationTarget = scrapCancel;
    }
    animationTarget.classList.remove("hide-animation");
    animationTarget.classList.add("show-animation");
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => {
      animationTarget.classList.remove("show-animation");
      animationTarget.classList.add("hide-animation");
    }, 3000);
  });
});
