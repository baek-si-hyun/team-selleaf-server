// 스크랩 버튼

const scrapBtn = document.querySelector(".post-wrap");
const scrapPopup = document.querySelector(".scrap-popup-wrap");
const scrapCancel = document.querySelector(".scrap-popup-cancel-wrap");

let timeoutId;
let animationTarget;

scrapBtn.addEventListener("click", handleScrapButtonClick);

function handleScrapButtonClick(event) {
  const target = event.target.closest(".scrap-button");
  if (!target) return; // 스크랩 버튼이 아닌 경우 무시

  const img = target.querySelector("img");
  const imgSrc = img.getAttribute("src");

  if (imgSrc === "/staticfiles/images/scrap-off.png") {
    img.setAttribute("src", "/staticfiles/images/scrap-on.png");
    showPopup(scrapPopup);
  } else {
    img.setAttribute("src", "/staticfiles/images/scrap-off.png");
    showPopup(scrapCancel);
  }
}

const scrapButton = document.querySelector(".update-post-list");

scrapButton.addEventListener("click", (e) => {
  const target = e.target.closest(".scrap-button");
  const img = target.querySelector("img");
  const imgSrc = img.getAttribute("src");
  if (imgSrc === "/staticfiles/images/scrap-off.png") {
    img.setAttribute("src", "/staticfiles/images/scrap-on.png");
    animationTarget && animationTarget.classList.remove("show-animation");
    animationTarget = scrapPopup;
  } else {
    img.setAttribute("src", "/staticfiles/images/scrap-off.png");
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

// 팝업 보여주기
function showPopup(target) {
  clearTimeout(timeoutId);
  if (animationTarget) animationTarget.classList.remove("show-animation");
  animationTarget = target;
  animationTarget.classList.remove("hide-animation");
  animationTarget.classList.add("show-animation");

  // 일정 시간 후 팝업 숨기기
  timeoutId = setTimeout(() => {
    hidePopup();
  }, 3000);
}

// 팝업 숨기기
function hidePopup() {
  if (!animationTarget) return;
  animationTarget.classList.remove("show-animation");
  animationTarget.classList.add("hide-animation");
}

// 마우스 오버와 아웃 이벤트에 대한 함수를 만들어 재사용성을 높임
function handleMouseOverAndOut(event) {
  const target = event.target;
  if (!target) return; // 요소가 없으면 무시

  target.style.opacity = event.type === "mouseover" ? "30%" : "100%";
}

// popular-detail-link 요소에 이벤트 리스너 추가
const letter = document.querySelector(".popular-detail-link");
letter.addEventListener("mouseover", handleMouseOverAndOut);
letter.addEventListener("mouseout", handleMouseOverAndOut);

// new-detail-link 요소에 이벤트 리스너 추가
const newDetail = document.querySelector("#new-detail-link");
newDetail.addEventListener("mouseover", handleMouseOverAndOut);
newDetail.addEventListener("mouseout", handleMouseOverAndOut);

// //더보기 글씨 흐려지기
// const letter = document.querySelector(".popular-detail-link");

// letter.addEventListener("mouseover", (e) => {
//   e.target.style.opacity = "30%";
// });

// letter.addEventListener("mouseout", (e) => {
//   e.target.style.opacity = "100%";
// });

// const newDetail = document.querySelector("#new-detail-link");
// newDetail.addEventListener("mouseover", (e) => {
//   e.target.style.opacity = "30%";
// });

// newDetail.addEventListener("mouseout", (e) => {
//   e.target.style.opacity = "100%";
// });

// 이미지에 마우스 대면 커지기
const images = document.querySelector(".image");

images.forEach((image, i) => {
  image.addEventListener("mouseover", (e) => {
    image[i].style.transform = "scale(1.05)";
  });
});
