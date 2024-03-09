const lectureCategoryService = (() => {
  const list = async (category) => {
    await fetch(`/lecture-category/api/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json;charset=utf-8',
        'X-CSRFToken': csrf_token
      },
      body: JSON.stringify({'category': category})
    });
  }

  return {list: list}
})()
