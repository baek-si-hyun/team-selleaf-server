const lectureService = (() => {

    const getList = async (page, filters, sorting, type, callback) => {
        const response = await fetch(`/lecture/total/${page}/${filters}/${sorting}/${type}`);
        const lectures = await response.json();
        if(callback){
            return callback(lectures);
        }
        return lectures;
    }


    return {getList: getList}
})();


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