// 주소 모달창 나오게
const addressModal = document.querySelector(".address-modal-wrap");
const modalBtn = document.querySelector(".change-button");

modalBtn.addEventListener("click", (e) => {
    addressModal.style.display = "block";
});

// 주소 모달창 닫기
const closeBtn = document.querySelector(".close-button");
closeBtn.addEventListener("click", (e) => {
    addressModal.style.display = "none";
});

// 주소 수정 모달창 나오게
const updateModal = document.querySelector(".address-update-modal-wrap");
const updateBtns = document.querySelectorAll(".update-button");

updateBtns.forEach((updateBtn) => {
    updateBtn.addEventListener("click", (e) => {
        updateModal.style.display = "block";
    });
});

// 주소 수정 모달창 뒤로가기
const backBtn = document.querySelector(".back-button");
backBtn.addEventListener("click", (e) => {
    updateModal.style.display = "none";
});

// 주소 수정 모달창 닫기
const cancelBtn = document.querySelector(".cancel-button");
cancelBtn.addEventListener("click", (e) => {
    updateModal.style.display = "none";
    addressModal.style.display = "none";
});

// 주소 추가 모달창 나오게
const addModal = document.querySelector(".add-address-total-wrap");
const addBtn = document.querySelector(".add-button");

addBtn.addEventListener("click", (e) => {
    addModal.style.display = "block";
});

// 주소 추가 모달창 뒤로가기
const addBack = document.querySelector(".add-back-button-image-wrap");
addBack.addEventListener("click", (e) => {
    addModal.style.display = "none";
});

// 주소 추가 모달창 닫기
const addClose = document.querySelector(".add-cancel-button");

addClose.addEventListener("click", (e) => {
    addModal.style.display = "none";
    addressModal.style.display = "none";
});

// 모달에서 삭제누르면 경고가 나오게

const deleteButtons = document.querySelectorAll(".delete-button");
const confirmModal = document.querySelector(".confirm-total-wrap");

deleteButtons.forEach((deleteButton) => {
    deleteButton.addEventListener("click", (e) => {
        // 삭제 버튼을 누를 때 confirm 모달 표시
        confirmModal.style.display = "block";

        // 확인 버튼 이벤트
        const confirmAction = document.querySelector(".confirm");
        confirmAction.addEventListener("click", () => {
            // 확인을 누르면 삭제 수행
            const target = deleteButton.closest(".address-wrap");
            target.remove();

            // confirm 모달 숨김
            confirmModal.style.display = "none";
        });

        // 취소 버튼 이벤트
        const cancelAction = document.querySelector(".confirm-cancel");
        cancelAction.addEventListener("click", () => {
            // 취소를 누르면 confirm 모달 숨김
            confirmModal.style.display = "none";
        });
    });
});

// 기본배송지 수정 체크박스

const mainCheckers = document.querySelectorAll(".main-address-checker");
mainCheckers.forEach((mainChecker) => {
    mainChecker.addEventListener("click", (e) => {
        e.target.closest(".main-address-checker").classList.toggle("checked");
    });
});

// 주소찾기 api
window.onload = function () {
    const addressBtn = document.querySelector(".address-search-button");
    addressBtn.addEventListener("click", function () {
        //주소입력칸을 클릭하면
        //카카오 지도 발생
        new daum.Postcode({
            oncomplete: function (data) {
                //선택시 입력값 세팅
                console.log(data);
                document.querySelector(".zipcode").value = data.zonecode; // 주소 넣기
                document.querySelector(".address-input").value = data.address; //상세입력 포커싱
            },
        }).open();
    });
};

// 주소 추가 모달 주소찾기
window.onload = function () {
    const addressBtn = document.querySelector(".address-add-button");
    addressBtn.addEventListener("click", function () {
        //주소입력칸을 클릭하면
        //카카오 지도 발생
        new daum.Postcode({
            oncomplete: function (data) {
                //선택시 입력값 세팅
                console.log(data);
                document.querySelector(".added-zipcode").value = data.zonecode; // 주소 넣기
                document.querySelector(".added-address").value = data.address; //상세입력 포커싱
            },
        }).open();
    });
};

// 선택한 주소 화면에 적용
const selectBtns = document.querySelectorAll(".select-button");

selectBtns.forEach((selectBtn) => {
    selectBtn.addEventListener("click", handleSelectButtonClick);
});

function handleSelectButtonClick(event) {
    addressModal.style.display = "none";
    const target = event.target.closest(".address-wrap");
    if (!target) return; // 해당 요소가 없으면 함수 종료

    const placeInfo = document.querySelector(".delivery-place-name");
    const address = document.querySelector(".address");
    const userInfo = document.querySelector(".user-info-wrap");

    // 주소 정보 업데이트
    const updateAddress = target.querySelector(".address-text").textContent;
    const updateAddressTitle = target.querySelector(".address-title").textContent;
    const updateName = target.querySelector(".address-user-name").textContent;
    const updatePhone = target.querySelector(".address-user-phone").textContent;
    const updatetag = target.querySelector(".address-tag").textContent;

    // 화면에 정보 업데이트
    placeInfo.innerHTML = `<div class="address-name">${updateAddressTitle}</div>${updatetag && `<div class="tag">${updatetag}`}`;
    address.textContent = updateAddress;
    userInfo.innerHTML = `<div class="name">${updateName}</div><div class="phone">${updatePhone}</div>`;
}

// 결제 수단 선택하기
const payments = document.querySelectorAll(".payment");
const cardSelection = document.querySelector(".card-type-option-wrap");
payments.forEach((payment) => {
    payment.addEventListener("click", (e) => {
        let target = e.target.closest(".payment");
        payments.forEach((payment) => {
            let target = payment.closest(".payment");
            console.log(111);
            target.classList.remove("selected");
        });
        target.classList.add("selected");

        button = e.target.closest(".payment-button");
        console.log(button);
        button.title === "카드결제" ? (cardSelection.style.display = "block") : (cardSelection.style.display = "none");
    });
});

NodeList.prototype.filter = Array.prototype.filter;

// 결제창 동의 체크
const allCheckBox = document.querySelector(".total-agree-checkbox-wrap");
const checkBoxes = document.querySelectorAll(".term-checkbox-wrap");
const agreeDivs = document.querySelectorAll(".term-inner");
const agreeCheck = document.querySelectorAll(".check1");
const totalAgree = document.querySelector(".total-agree-wrap");
const totalCheck = document.querySelector(".total-check");

// 전체 동의 체크박스 클릭시
allCheckBox.addEventListener("click", (e) => {
    if (totalCheck.checked) {
        allCheckBox.classList.remove("checked");
        totalCheck.checked = false;
        agreeCheck.forEach((agree) => {
            agree.checked = false;
        });
        checkBoxes.forEach((box) => {
            box.classList.remove("checked");
        });
    } else {
        allCheckBox.classList.add("checked");
        totalCheck.checked = true;
        agreeCheck.forEach((agree) => {
            agree.checked = true;
        });
        checkBoxes.forEach((box) => {
            box.classList.add("checked");
        });
    }
});
// 전체 동의 텍스트 클릭 시
totalAgree.addEventListener("click", (e) => {
    if (totalCheck.checked) {
        allCheckBox.classList.remove("checked");
        totalCheck.checked = false;
        agreeCheck.forEach((agree) => {
            agree.checked = false;
        });
        checkBoxes.forEach((box) => {
            box.classList.remove("checked");
        });
    } else {
        allCheckBox.classList.add("checked");
        totalCheck.checked = true;
        agreeCheck.forEach((agree) => {
            agree.checked = true;
        });
        checkBoxes.forEach((box) => {
            box.classList.add("checked");
        });
    }
});

// 개인정보수집, 결제대행 체크박스 클릭 시
checkBoxes.forEach((div, i) => {
    div.addEventListener("click", () => {
        if (agreeCheck[i].checked) {
            agreeCheck[i].checked = false;
            checkBoxes[i].classList.remove("checked");
        } else {
            agreeCheck[i].checked = true;
            checkBoxes[i].classList.add("checked");
        }

        if (agreeCheck[0].checked && agreeCheck[1].checked) {
            allCheckBox.classList.add("checked");
            totalCheck.checked = true;
        } else {
            allCheckBox.classList.remove("checked");
            totalCheck.checked = false;
        }
    });
});

// 개인정보수집, 결제대행 텍스트 클릭 시
agreeDivs.forEach((div, i) => {
    div.addEventListener("click", () => {
        if (agreeCheck[i].checked) {
            agreeCheck[i].checked = false;
            checkBoxes[i].classList.remove("checked");
        } else {
            agreeCheck[i].checked = true;
            checkBoxes[i].classList.add("checked");
        }

        if (agreeCheck[0].checked && agreeCheck[1].checked) {
            allCheckBox.classList.add("checked");
            totalCheck.checked = true;
        } else {
            allCheckBox.classList.remove("checked");
            totalCheck.checked = false;
        }
    });
});

// checkBoxes.forEach((checkBox) => {
//   checkBox.addEventListener("click", (e) => {
//     if (checkBox.classList.contains("checked")) {
//       checkBox.classList.remove("checked");
//       allCheckBox.classList.remove("checked");
//     } else {
//       checkBox.classList.add("checked");
//     }

//     if (console.log(checkBox.classList.contains("checked")) === "ture") {
//       allCheckBox.classList.add("checked");
//     }
//   });
// });

// const all = document.querySelector("input.all");
// const terms = document.querySelectorAll("input.term");

// termAll.addEventListener("click", (e) => {
//   checkBoxes.forEach((checkBox) => {
//     checkBox.checked = e.target.checked;
//   });
// });

// terms.forEach((term) => {
//   term.addEventListener("click", (e) => {
//     all.checked = terms.filter((term) => term.checked).length === 3;
//   });
// });
