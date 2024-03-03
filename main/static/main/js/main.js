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
const searchOnedayImg = document.querySelectorAll(".realmain-my_lecture-photo");
const searchOnedayA = document.querySelectorAll(
    ".realmain-my_lecture-explanationA"
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


const realmainWrap = document.querySelector('.realmain-wrap')
realmainWrap.addEventListener("click", (e) => {
    const scrap = e.target.closest('.scrap-button')
    const img = scrap.querySelector("img");
    const imgSrc = img.getAttribute("src");
    if (imgSrc === "/static/public/web/images/common/scrap-off.png") {
        img.setAttribute("src", "/static/public/web/images/common/scrap-on.png");
        animationTarget && animationTarget.classList.remove("show-animation");
        animationTarget = scrapPopup;
    } else {
        img.setAttribute("src", "/static/public/web/images/common/scrap-off.png");
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
//
// // 원데이 클래스, 인기 콘텐츠 부분에 스크랩 on off 기능
// const popularScrapButton = document.querySelectorAll(
//     ".realmain-my_lecture-scrapbutton"
// );
//
// popularScrapButton.forEach((scrap) => {
//     scrap.addEventListener("click", () => {
//         const img = scrap.querySelector("img");
//         const imgSrc = img.getAttribute("src");
//         if (imgSrc === "../../../staticfiles/images/scrap-off.png") {
//             img.setAttribute("src", "../../../staticfiles/images/scrap-on.png");
//             animationTarget && animationTarget.classList.remove("show-animation");
//             animationTarget = scrapPopup;
//         } else {
//             img.setAttribute("src", "../../../staticfiles/images/scrap-off.png");
//             animationTarget.classList.remove("show-animation");
//             animationTarget = scrapCancel;
//         }
//         animationTarget.classList.remove("hide-animation");
//         animationTarget.classList.add("show-animation");
//         clearTimeout(timeoutId);
//         timeoutId = setTimeout(() => {
//             animationTarget.classList.remove("show-animation");
//             animationTarget.classList.add("hide-animation");
//         }, 3000);
//     });
// });
//
// // 오늘의 딜부분에 스크랩 on off 기능
// const todayScrapButton = document.querySelectorAll(
//     ".realmain-todayHotdeal-scrapbutton"
// );
//
// todayScrapButton.forEach((scrap) => {
//     scrap.addEventListener("click", () => {
//         const img = scrap.querySelector("img");
//         const imgSrc = img.getAttribute("src");
//         if (imgSrc === "../../../staticfiles/images/scrap-off.png") {
//             img.setAttribute("src", "../../../staticfiles/images/scrap-on.png");
//             animationTarget && animationTarget.classList.remove("show-animation");
//             animationTarget = scrapPopup;
//         } else {
//             img.setAttribute("src", "../../../staticfiles/images/scrap-off.png");
//             animationTarget.classList.remove("show-animation");
//             animationTarget = scrapCancel;
//         }
//         animationTarget.classList.remove("hide-animation");
//         animationTarget.classList.add("show-animation");
//         clearTimeout(timeoutId);
//         timeoutId = setTimeout(() => {
//             animationTarget.classList.remove("show-animation");
//             animationTarget.classList.add("hide-animation");
//         }, 3000);
//     });
// });
//
// // 베스트 상품 부분에 스크랩 on off 기능
// const bestproductScrapButton = document.querySelectorAll(
//     ".realmain-bestproduct-realPhotoScrapbtn"
// );
//
// bestproductScrapButton.forEach((scrap) => {
//     scrap.addEventListener("click", () => {
//         const img = scrap.querySelector("img");
//         const imgSrc = img.getAttribute("src");
//         if (imgSrc === "../../../staticfiles/images/scrap-off.png") {
//             img.setAttribute("src", "../../../staticfiles/images/scrap-on.png");
//             animationTarget && animationTarget.classList.remove("show-animation");
//             animationTarget = scrapPopup;
//         } else {
//             img.setAttribute("src", "../../../staticfiles/images/scrap-off.png");
//             animationTarget.classList.remove("show-animation");
//             animationTarget = scrapCancel;
//         }
//         animationTarget.classList.remove("hide-animation");
//         animationTarget.classList.add("show-animation");
//         clearTimeout(timeoutId);
//         timeoutId = setTimeout(() => {
//             animationTarget.classList.remove("show-animation");
//             animationTarget.classList.add("hide-animation");
//         }, 3000);
//     });
// });
