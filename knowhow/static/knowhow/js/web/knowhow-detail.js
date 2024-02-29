const inputWrap = document.querySelector(".input-wrap");
const inputContainer = document.querySelector(".input-container");
const commentInput = document.querySelector(".comment-input");

commentInput.addEventListener("focus", () => {
  inputContainer.style.border = "1px solid #c06888";
});
commentInput.addEventListener("focusout", () => {
  inputContainer.style.border = "1px solid rgb(218, 221, 224)";
});

const commentSubmitBtn = document.querySelector(".comment-submit-btn");
commentInput.addEventListener("keyup", () => {
  commentInput.value
    ? (commentSubmitBtn.style.color = "#c06888")
    : (commentSubmitBtn.style.color = "rgb(194, 200, 204)");
});

const stickyBtns = document.querySelectorAll(".sticky-btn");
stickyBtns.forEach((item) => {
  item.addEventListener("click", () => {
    if (item.getAttribute("title") === "좋아요") {
      const img = item.querySelector("img");
      const imgSrc = img.getAttribute("src");
      imgSrc === "../../../staticfiles/images/like-off.png"
        ? img.setAttribute("src", "../../../staticfiles/images/like-on.png")
        : img.setAttribute("src", "../../../staticfiles/images/like-off.png");
    }
    if (item.getAttribute("title") === "저장") {
      const img = item.querySelector("img");
      const imgSrc = img.getAttribute("src");
      imgSrc === "../../../staticfiles/images/scrap-off-blk.png"
        ? img.setAttribute(
            "src",
            "../../../staticfiles/images/scrap-on-pink.png"
          )
        : img.setAttribute(
            "src",
            "../../../staticfiles/images/scrap-off-blk.png"
          );
    }
  });
});

const paginationBtn = document.querySelectorAll(".pagination-btn");
const paginationBox = document.querySelector(".pagination-box");

paginationBox.addEventListener("click", (e) => {
  let pageBtn = e.target.closest(".pagination-btn");
  if (pageBtn) {
    paginationBtn.forEach((item) => {
      item.classList.contains("select") && item.classList.remove("select");
    });
    pageBtn.classList.add("select");
  }
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
const contentDeclarationBtn = document.querySelector(
  ".content-declaration-btn"
);
contentDeclarationBtn.addEventListener("click", () => {
  declarationModalWrap.classList.add("open");
});
const commentDeclarationBtns = document.querySelectorAll(
  ".comment-declaration-btn"
);
commentDeclarationBtns.forEach((item) => {
  item.addEventListener("click", () => {
    declarationModalWrap.classList.add("open");
  });
});
//신고 모달 없애기
const declarationBtn = document.querySelector(".declaration-btn");
declarationBtn.addEventListener("click", () => {
  declarationModalWrap.classList.remove("open");
});

//이미지 미리보기
const contentImg = document.querySelector(".content-img");
const prevImgs = document.querySelectorAll(".prev-img");
prevImgs.forEach((item) => {
  item.addEventListener("click", (e) => {
    const imgSrc = e.target.getAttribute("src");
    contentImg.setAttribute("src", imgSrc);
  });
});

const commentLikeBtns = document.querySelectorAll(".comment-like-btn");
commentLikeBtns.forEach((btn) => {
  btn.addEventListener("click", () => {
    const img = btn.querySelector("img");
    const imgSrc = img.getAttribute("src");
    imgSrc === "/staticfiles/images/like-off.png"
      ? img.setAttribute("src", "/staticfiles/images/like-on.png")
      : img.setAttribute("src", "/staticfiles/images/like-off.png");
  });
});
