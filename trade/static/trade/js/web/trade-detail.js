// 이미지 버튼 슬라이싱

const nextButton = document.querySelector(".scroller-ui-next");
const prevButton = document.querySelector(".scroller-ui-prev");
const target = document.querySelector(".scroller-contents-container");
const prevSvg = document.querySelector(".prev-icon");

var xdegree = 0;
nextButton.addEventListener("click", (e) => {
  xdegree -= 712;
  with (target.style) {
    transform = `translateX(${xdegree}px)`;
    transition = "transform 0.3s ease 0s";
  }
  xdegree === -2848
    ? (nextButton.style.display = "none")
    : (nextButton.style.display = "block");
  xdegree === -712 && (prevButton.style.display = "block");

  console.log(xdegree);
});

prevButton.addEventListener("click", (e) => {
  xdegree += 712;
  with (target.style) {
    transform = `translateX(${xdegree}px)`;
    transition = "transform 0.3s ease 0s";
  }
  xdegree === -2136 && (nextButton.style.display = "block");
  xdegree === 0 && (prevButton.style.display = "none");
  console.log(xdegree);
});

//스크랩 버튼
const scrapBtn = document.querySelector(".scrap-button");

scrapBtn.addEventListener("click", () => {
  const img = scrapBtn.querySelector("img");
  const imgSrc = img.getAttribute("src");
  if (imgSrc === "/staticfiles/images/scrap-off-blk.png") {
    img.setAttribute("src", "/staticfiles/images/scrap-on.png");
  } else {
    img.setAttribute("src", "/staticfiles/images/scrap-off-blk.png");
  }
});

// 비슷한 제품 스크랩 버튼

const scrapButton = document.querySelectorAll(".img-scrap-button");
// const scrapPopup = document.querySelector(".scrap-popup-wrap");
// const scrapCancel = document.querySelector(".scrap-popup-cancel-wrap");
scrapButton.forEach((scrap) => {
  scrap.addEventListener("click", () => {
    const img = scrap.querySelector("img");
    const imgSrc = img.getAttribute("src");
    if (imgSrc === "/staticfiles/images/scrap-off.png") {
      img.setAttribute("src", "/staticfiles/images/scrap-on.png");
    } else {
      img.setAttribute("src", "/staticfiles/images/scrap-off.png");
    }
    // scrapPopup.style.display == "none"
    //   ? (scrapPopup.style.display = "block")
    //   : (scrapPopup.style.display = "none");
  });
});

// 퀵네비 클릭시 색변하도록
const navs = document.querySelectorAll(".product-detail-nav-item");
navs.forEach((nav, index) => {
  nav.addEventListener("click", (e) => {
    navs.forEach((otherNav, otherIndex) => {
      if (index !== otherIndex) {
        otherNav.classList.remove("active");
      }
    });
    nav.classList.add("active");
  });
});
//신고 모달
const declarationLabels = document.querySelectorAll(".declaration-label");
const declarationInputs = document.querySelectorAll(".declaration-input");
declarationLabels.forEach((item) => {
  item.addEventListener("click", () => {
    declarationInputs.forEach((radio, i) => {
      if (radio.checked) {
        radio.parentNode.classList.add("declaration-choice");
      } else {
        radio.parentNode.classList.remove("declaration-choice");
      }
    });
  });
});
//신고모달 띄우기
const declarationModalWrap = document.querySelector(".declaration-modal-wrap");
const contentDeclarationBtn = document.querySelector(".report-button");
contentDeclarationBtn.addEventListener("click", () => {
  declarationModalWrap.classList.add("open");
});

//신고 모달 없애기
const declarationBtn = document.querySelector(".declaration-btn");
declarationBtn.addEventListener("click", () => {
  declarationModalWrap.classList.remove("open");
});
