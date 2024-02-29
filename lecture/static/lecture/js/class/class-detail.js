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

// 사이드 바 선택옵션 삭제
const deleteButtons = document.querySelectorAll(".sidebar-delete-button");
const deleteBtns = document.querySelectorAll(".delete-button-container");

deleteButtons.forEach((deleteButton) => {
  deleteButton.addEventListener("click", (e) => {
    const options = deleteButton.closest(".sidebar-selected-product-container");
    options.style.display = "none";
  });
});

// 물건 선택옵션 삭제

deleteBtns.forEach((deleteBtn) => {
  deleteBtn.addEventListener("click", (e) => {
    const selection = deleteBtn.closest(".selected-product-list-container");
    selection.style.display = "none";
    studentName.style.display = "none";
    sidebarSelected.style.display = "none";
    days.forEach((day) => {
      day.classList.remove("clicked");
    });
    times.forEach((time) => {
      timeSection.style.display = "none";
      time.classList.remove("clicked");
    });
    kits.forEach((kit) => {
      const target = document.querySelector(".product-option-second-wrap");
      target.style.display = "none";
      kit.classList.remove("clicked");
    });
  });
});

// 날짜 선택 시 색 변하게
const days = document.querySelectorAll(".weekday-selection");
const timeSection = document.querySelector(".product-option-second-wrap");
const inputTarget = document.querySelector(".selected-product-name");
const sidebarInputTarget = document.querySelector(
  ".sidebar-selected-product-option"
);
days.forEach((day) => {
  day.addEventListener("click", (e) => {
    // 모든 요일에서 clicked 클래스를 제거
    days.forEach((otherday) => {
      otherday.classList.remove("clicked");
    });
    // 클릭된 요일에만 clicked 클래스 추가
    day.classList.add("clicked");
    const selectedDay = day.querySelector("span").textContent;
    var inner = inputTarget.querySelector(".selected-date");
    var sidebarInner = sidebarInputTarget.querySelector(".selected-date");
    inner.innerHTML = `${selectedDay}`;
    sidebarInner.innerHTML = `${selectedDay}`;
    // 시간 섹션을 보이거나 숨김
    if (day.classList.contains("clicked")) {
      timeSection.style.display = "block";
    } else {
      timeSection.style.display = "none";
    }
  });
});

// 시간 선택 시 색 변하게
const times = document.querySelectorAll(".time-selection");
const check = document.querySelector(".selected-product-list-container");
const sidebarselectBox = document.querySelector(
  ".sidebar-selected-product-wrap"
);
times.forEach((time) => {
  time.addEventListener("click", (e) => {
    // 모든 시간 요소에서 clicked 클래스를 제거
    times.forEach((othertime) => {
      othertime.classList.remove("clicked");
    });

    // 클릭된 시간에만 clicked 클래스 추가
    time.classList.add("clicked");
    const selectedTime = time.querySelector("span").textContent;
    var inner = inputTarget.querySelector(".selected-time");
    var sidebarInner = sidebarInputTarget.querySelector(".selected-time");
    inner.innerHTML = `${selectedTime}`;
    sidebarInner.innerHTML = `${selectedTime}`;
    // 체크 요소를 보이거나 숨김
    if (time.classList.contains("clicked")) {
      check.style.display = "block";
      sidebarselectBox.style.display = "block";
    } else {
      check.style.display = "none";
      sidebarselectBox.style.display = "none";
    }
  });
});

// 인원 가감
const number = document.querySelector(".counted-number");
const add = document.querySelector(".add-count");
const sub = document.querySelector(".sub-count");
const studentInfo = document.querySelector(".student-info-inner");
const sidebarNumber = document.querySelector(".sidebar-count-number");
const sidebarAdd = document.querySelector(".sidebar-add-count");
const sidebarSub = document.querySelector(".sidebar-sub-count");
const studentName = document.querySelector(".selected-student-list-wrap");
const price = document.querySelector(".total-price");
const studentAlert = document.querySelector(".student-count-title");
const sidebarAlert = document.querySelector(".sidebar-student-count-title");
const sidebarSelected = document.querySelector(
  ".sidebar-selected-product-container"
);
var count = 0;

add.addEventListener("click", (e) => {
  if (count < 5) {
    // 현재 예약된 인원이 5명 미만인 경우에만 추가
    count++;
    count === 0
      ? (studentName.style.display = "none")
      : (studentName.style.display = "block");
    studentInfo.innerHTML += `
    <div class="info-list-wrap">
      <div class="student-label">
        <div>예약자</div> <div>${count}</div>
      </div>
        <input
          class="student-name-input"
          placeholder="예약자 이름을 입력하세요"
          name="price-input"
        />
    </div>`;
    number.innerHTML = `${count}`;
    sidebarNumber.innerHTML = `${count}`;
    if (count >= 5) {
      console.log(studentAlert);
      studentAlert.innerHTML += `
      <div class="student-alert">
        <div>최대 예약인원은 ${count}명입니다.</div>
      </div>`;
      sidebarAlert.innerHTML += `
      <div class="student-alert">
        <div>최대 예약인원은 ${count}명입니다.</div>
      </div>`;
    }
  }
});

sub.addEventListener("click", (e) => {
  count == 0 ? (count = 0) : count--;
  number.innerHTML = `${count}`;
  sidebarNumber.innerHTML = `${count}`;
  var target = studentInfo.querySelectorAll(".info-list-wrap");
  target[count].remove();
  var removeTarget = studentAlert.querySelector(".student-alert");
  var sidebarTarget = sidebarAlert.querySelector(".student-alert");
  removeTarget && removeTarget.remove();
  sidebarTarget && sidebarTarget.remove();
});

sidebarAdd.addEventListener("click", (e) => {
  if (count < 5) {
    // 현재 예약된 인원이 5명 미만인 경우에만 추가
    count++;
    count === 0
      ? (studentName.style.display = "none")
      : (studentName.style.display = "block");
    studentInfo.innerHTML += `
    <div class="info-list-wrap">
      <div class="student-label">
        <div>예약자</div> <div>${count}</div>
      </div>
        <input
          class="student-name-input"
          placeholder="예약자 이름을 입력하세요"
          name="price-input"
        />
    </div>`;
    number.innerHTML = `${count}`;
    sidebarNumber.innerHTML = `${count}`;
    if (count >= 5) {
      studentInfo.innerHTML += `
      <div class="info-list-wrap">
      <div class="student-alert">
        <div>최대 예약인원은 ${count}명입니다.</div>
      </div>
    </div>`;
    }
  }
});

sidebarSub.addEventListener("click", (e) => {
  count == 0 ? (count = 0) : count--;
  number.innerHTML = `${count}`;
  sidebarNumber.innerHTML = `${count}`;
  var target = studentInfo.querySelectorAll(".info-list-wrap");
  target[count].remove();
  var studentAlert = studentInfo.querySelector(".student-alert");
  studentAlert && studentAlert.remove();
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

// 리뷰 리스트 다음 장
const lists = document.querySelectorAll(".product-review-page");
lists.forEach((list, index) => {
  list.addEventListener("click", (e) => {
    lists.forEach((otherList, otherIndex) => {
      if (index !== otherIndex) {
        otherList.classList.remove("selected-page");
      }
    });
    list.classList.add("selected-page");
  });
});

// 도움이 되요 버튼
const help = document.querySelector(".product-review-help-button");
help.addEventListener("click", (e) => {
  help.classList.toggle("help-clicked");
});

// kit 선택 시 색 변하게
const kits = document.querySelectorAll(".kit-selection");
const infoContainer = document.querySelector(
  ".selected-product-list-container"
);
kits.forEach((kit) => {
  kit.addEventListener("click", (e) => {
    // 모든 요일에서 clicked 클래스를 제거
    kits.forEach((otherkit) => {
      otherkit.classList.remove("clicked");
    });
    // 클릭된 요일에만 clicked 클래스 추가
    kit.classList.add("clicked");
    console.log(kit);
    const selectedKit = kit.querySelector(".kit-title").textContent;
    var inner = inputTarget.querySelector(".selected-kit");
    var sidebarInner = sidebarInputTarget.querySelector(".selected-kit");
    inner.innerHTML = `${selectedKit}`;
    sidebarInner.innerHTML = `${selectedKit}`;
    // 시간 섹션을 보이거나 숨김
    if (kit.classList.contains("clicked")) {
      infoContainer.style.display = "block";
      sidebarSelected.style.display = "block";
    } else {
      infoContainer.style.display = "none";
      sidebarSelected.style.display = "none";
    }
  });
});

// 별점순 정렬버튼
const arrange = document.querySelector(".review-rating-button");

arrange.addEventListener("click", (e) => {
  var icon = arrange.querySelector(".icon");
  // 현재 회전된 각도를 가져오기
  var currentRotation = icon.style.transform.replace(/[^0-9]/g, "");
  // 현재 각도가 없는 경우 0으로 설정
  var currentAngle = parseInt(currentRotation) || 0;
  // 현재 각도에서 180도씩 더하기
  var newAngle = currentAngle + 180;
  // 회전 애니메이션 적용
  icon.style.transform = `rotate(${newAngle}deg)`;
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
