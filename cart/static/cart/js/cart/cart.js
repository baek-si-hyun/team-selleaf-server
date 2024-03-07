// // 장바구니 페이지 js 파일
//
// // 수빈 장바구니 페이지 JS 코드친거
// // +-버튼 눌렀을때 상품 개수가 +- 되야함
// const subBtns = document.querySelectorAll(".sub-count");
// const addBtns = document.querySelectorAll(".add-count");
// const countBtns = document.querySelectorAll(".counted-number");
// const productPrices = document.querySelectorAll(".price-number");
// let sum = 0;
// let sum2 = 0;
// let originPrice = [];
// NodeList.prototype.forEach = Array.prototype.forEach;
// const sumPrice = [];
// const resultPrice = document.querySelector(".emphasis");
// const toTalPrice = document.querySelector(".total-price");
// productPrices.forEach((price) => {
//   originPrice.push(price.innerText);
// });
//
// originPrice.forEach((op) => {
//   op = op.replace(",", "");
//   op = Number(op);
//   sum += op;
// });
//
// toTalPrice.innerText = sum.toLocaleString();
// // toTalPrice2 = toTalPrice2.replace(",", "");
// // console.log(toTalPrice2.innerText);
// resultPrice.innerHTML = sum.toLocaleString();
//
// // + 버튼
// addBtns.forEach((addBtn, i) => {
//   addBtn.addEventListener("click", () => {
//     const number = addBtn.previousElementSibling;
//     let count = Number(number.innerText);
//     count++;
//     number.innerText = `${count}`;
//     var price = originPrice[i];
//     replacePrice = Number(price.replace(",", ""));
//
//     // 총 상품 금액 부분
//     const realResultPrice = resultPrice.innerText;
//     const realResultPrice2 = realResultPrice.replace(",", "");
//     const realResultPrice3 = Number(realResultPrice2);
//
//     // 최종결제 금액 부분
//     const toTalPrice2 = toTalPrice.innerText;
//     const toTalPrice3 = toTalPrice2.replace(",", "");
//     const toTalPrice4 = Number(toTalPrice3);
//
//     const totalResultPrice = realResultPrice3 + replacePrice;
//     toTalPrice.innerText = toTalPrice4 + replacePrice;
//     resultPrice.innerHTML = totalResultPrice;
//     productPrices[i].innerText = (replacePrice * count).toLocaleString();
//   });
// });
//
// console.log(sumPrice);
// // - 버튼
// subBtns.forEach((subBtn, i) => {
//   subBtn.addEventListener("click", () => {
//     const number = subBtn.nextElementSibling;
//     let count = Number(number.innerText);
//     if (count == 1) {
//       number.innerText = 1;
//       return;
//     }
//     count--;
//     number.innerText = `${count}`;
//     var price = originPrice[i];
//     replacePrice = Number(price.replace(",", ""));
//
//     // 총 상품 금액 부분
//     const realResultPrice = resultPrice.innerText;
//     const realResultPrice2 = realResultPrice.replace(",", "");
//     const realResultPrice3 = Number(realResultPrice2);
//
//     // 최종결제 금액 부분
//     const toTalPrice2 = toTalPrice.innerText;
//     const toTalPrice3 = toTalPrice2.replace(",", "");
//     const toTalPrice4 = Number(toTalPrice3);
//
//     toTalPrice.innerText = toTalPrice4 - replacePrice;
//     const totalResultPrice = realResultPrice3 - replacePrice;
//     resultPrice.innerHTML = totalResultPrice;
//     productPrices[i].innerText = (replacePrice * count).toLocaleString();
//   });
// });

const showPrice = (detail)=>{
    let textlist = ``
    textlist +=`
      <div class="price-wrap">
        <div class="name-side">${detail[0]['lecture_title']}</div>
        <div class="price-side">${detail[0]['lecture_price']}</div>
        <div class="x ${detail[0]['id']}">X</div>
      </div>
    `
    return textlist
}
const checkbox = (targetId)=>{
    let checkbox = ``
    checkbox +=`
      <div class="selection ${detail['id']}"></div>
    `
    return checkbox
}


const showCartItems = (details)=>{
  let text =``

  details.forEach((detail)=>{
    text += `
      <li class="product-preview-wrap">
        <div class="product-preview-container">
          <div class="product-preview-inner">
            <div class="selection ${detail['id']}"></div>
            <h3 class="user-name">${detail['lecture_title']}</h3>
            <div class="delete ${detail['id']}">삭제</div>
          </div>
          <hr class="divide"/>
        </div>
        <div class="order-product-info">
          <figure class="product-preview-image">
            <img
                src="/upload/${detail['lecture_file']}"
                class="product-image" alt=""
            />
          </figure>
          <div class="product-info-contents">
            <div class="delivery-condition">강사명 | ${detail['teacher_name']}</div>
            <p class="product-name">
              ${detail['date']} | ${detail['time']} | ${detail['kit']}
            </p>
            <p class="product-option">
            <div class="selected-product-count">
            수량
                <div class="counted-number">
                  ${detail['quantity']}
                </div>
              </div>
            </p>
            <div class="product-price">
              <span class="price-number">${detail['lecture_price']}</span>
              <span class="won">원</span> &nbsp;
            </div>
          </div>
        </div>
      </li>
    `
    if ( detail.length ===0 ){
      text =`
        <div class="no-items-wrap">
            <h1 class="no-items-text">아직 장바구니에 담은 상품이 없어요.</h1>
            <div class="purchase-link-button-wrap">
              <a href="/lecture/total/" class="purchase-link-button">강의 바로가기</a>
            </div>
        </div>
      `
    }

  })
  return text;

}

const ul = document.querySelector('.cart-item-wrap')

cartService.getList(cart_id, showCartItems).then((text) => {
    ul.innerHTML = text;
});



ul.addEventListener("click", async (e) => {
    if(e.target.classList[0] === 'delete'){
        const detailId = e.target.classList[1]
        await cartService.remove(detailId)
        const text = await cartService.getList(cart_id, showCartItems);
        ul.innerHTML = text;
    }else if(e.target.classList[0]==='selection'){
        let target= e.target
        target.remove()
        const div = document.querySelector('.product-name-side')
        const detailId = e.target.classList[1]
        const textlist = await cartService.select(detailId,showPrice)
        div.innerHTML += textlist
    }
})

const sidebar = document.querySelector('.payment-detail-container')
    sidebar.addEventListener('click', async (e)=>{
        if(e.target.classList[0] === 'x') {
            const targetId = e.target.classList[1]
            e.target.parentElement.remove()
            const checkbox = await checkbox(targetId)
            ul.innerHTML += checkbox
        }
    })
