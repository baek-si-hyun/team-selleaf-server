// 장바구니 페이지 js 파일

// 수빈 장바구니 페이지 JS 코드친거
// +-버튼 눌렀을때 상품 개수가 +- 되야함
const subBtns = document.querySelectorAll(".sub-count");
const addBtns = document.querySelectorAll(".add-count");
const countBtns = document.querySelectorAll(".counted-number");
const productPrices = document.querySelectorAll(".price-number");
let sum = 0;
let sum2 = 0;
let originPrice = [];
NodeList.prototype.forEach = Array.prototype.forEach;
const sumPrice = [];
const resultPrice = document.querySelector(".emphasis");
const toTalPrice = document.querySelector(".total-price");
productPrices.forEach((price) => {
  originPrice.push(price.innerText);
});

originPrice.forEach((op) => {
  op = op.replace(",", "");
  op = Number(op);
  sum += op;
});

toTalPrice.innerText = sum.toLocaleString();
// toTalPrice2 = toTalPrice2.replace(",", "");
// console.log(toTalPrice2.innerText);
resultPrice.innerHTML = sum.toLocaleString();

// + 버튼
addBtns.forEach((addBtn, i) => {
  addBtn.addEventListener("click", () => {
    const number = addBtn.previousElementSibling;
    let count = Number(number.innerText);
    count++;
    number.innerText = `${count}`;
    var price = originPrice[i];
    replacePrice = Number(price.replace(",", ""));

    // 총 상품 금액 부분
    const realResultPrice = resultPrice.innerText;
    const realResultPrice2 = realResultPrice.replace(",", "");
    const realResultPrice3 = Number(realResultPrice2);

    // 최종결제 금액 부분
    const toTalPrice2 = toTalPrice.innerText;
    const toTalPrice3 = toTalPrice2.replace(",", "");
    const toTalPrice4 = Number(toTalPrice3);

    const totalResultPrice = realResultPrice3 + replacePrice;
    toTalPrice.innerText = toTalPrice4 + replacePrice;
    resultPrice.innerHTML = totalResultPrice;
    productPrices[i].innerText = (replacePrice * count).toLocaleString();
  });
});

console.log(sumPrice);
// - 버튼
subBtns.forEach((subBtn, i) => {
  subBtn.addEventListener("click", () => {
    const number = subBtn.nextElementSibling;
    let count = Number(number.innerText);
    if (count == 1) {
      number.innerText = 1;
      return;
    }
    count--;
    number.innerText = `${count}`;
    var price = originPrice[i];
    replacePrice = Number(price.replace(",", ""));

    // 총 상품 금액 부분
    const realResultPrice = resultPrice.innerText;
    const realResultPrice2 = realResultPrice.replace(",", "");
    const realResultPrice3 = Number(realResultPrice2);

    // 최종결제 금액 부분
    const toTalPrice2 = toTalPrice.innerText;
    const toTalPrice3 = toTalPrice2.replace(",", "");
    const toTalPrice4 = Number(toTalPrice3);

    toTalPrice.innerText = toTalPrice4 - replacePrice;
    const totalResultPrice = realResultPrice3 - replacePrice;
    resultPrice.innerHTML = totalResultPrice;
    productPrices[i].innerText = (replacePrice * count).toLocaleString();
  });
});

const cartItem = document.querySelector(".cart-item-wrap")




// innerHTML
// <li className="product-preview-wrap">
//   <div className="product-preview-container">
//     <div className="product-preview-inner">
//       <h3 className="user-name">{{cart_detail.lecture.teacher.member.member_name}}</h3>
//       <div className="delivery-condition">{{cart_detail.date.date}}</div>
//     </div>
//     <hr className="divide"/>
//   </div>
//   <div className="order-product-info">
//     <figure className="product-preview-image">
//       <img
//           src="{% static 'public/web/images/common/blank-image.png' %}"
//           className="product-image" alt=""
//       />
//     </figure>
//     <div className="product-info-contents">
//       <p className="product-name">
//         {{cart_detail.lecture.lecture_name}}
//       </p>
//       <p className="product-option">
//         {% if cart_detail.kit == 'offline' %}
//         {{cart_detail.date.date}} | {{cart_detail.time.time}}
//         {% else %}
//         {{cart_detail.date.date}} | {{cart_detail.time.time}} | {{cart_detail.kit.kit_name}}
//         {% endif %}
//       </p>
//       <div className="product-price">
//                         <span className="price-number">{{cart_detail.lecture.lecture_price}}</span
//                         ><span className="won">원</span> &nbsp;
//         <div className="selected-product-count">
//                           <span className="sub-count">
//                             <img src="{% static 'public/web/images/common/sub.png' %}" alt=""/>
//                           </span>
//           <button type="button" className="counted-number">
//             {{cart_detail.quantity}}
//           </button>
//           <span className="add-count">
//                             <img src="{% static 'public/web/images/common/add.png' %}" alt=""/>
//                           </span>
//         </div>
//       </div>
//     </div>
//   </div>
// </li>