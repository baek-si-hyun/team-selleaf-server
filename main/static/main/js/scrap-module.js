const knowhowScrapService = (() => {
  const update = async (knowhowId) => {
    await fetch(`/knowhow-scrap/api/`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json;charset=utf-8',
        'X-CSRFToken': csrf_token
      },
      body: JSON.stringify({'knowhow_id': knowhowId})
    });
  }

  return {update: update}
})()

const tradeScrapService = (() => {
  const update = async (tradeId) => {
    await fetch(`/trade-scrap/api/`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json;charset=utf-8',
        'X-CSRFToken': csrf_token
      },
      body: JSON.stringify({'trade_id': tradeId})
    });
  }

  return {update: update}
})()

const lectureScrapService = (() => {
  const update = async (lectureId) => {
    await fetch(`/lecture-scrap/api/`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json;charset=utf-8',
        'X-CSRFToken': csrf_token
      },
      body: JSON.stringify({'lecture_id': lectureId})
    });
  }

  return {update: update}
})()
