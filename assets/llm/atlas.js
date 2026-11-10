(() => {
  'use strict';
  const topics = [...document.querySelectorAll('.topic')];
  const boxes = [...document.querySelectorAll('[data-key]')];
  const search = document.querySelector('#search');
  const key = 'llm-atlas-progress-v1';
  let saved = {};
  try { const value = JSON.parse(localStorage.getItem(key) || '{}'); if (value && typeof value === 'object' && !Array.isArray(value)) saved = value; }
  catch { document.querySelector('#storage-note').textContent = 'Progress is available for this visit only'; }
  boxes.forEach(box => { box.checked = saved[box.dataset.key] === true; });
  function progress() {
    const count = boxes.filter(box => box.checked).length;
    document.querySelector('#progress').value = count;
    document.querySelector('#progress-label').textContent = `${count.toLocaleString()} of 1,240 concepts explored`;
    document.querySelector('#percent').textContent = `${Math.round(count / boxes.length * 100)}%`;
  }
  document.querySelector('#topics').addEventListener('change', event => {
    const box = event.target;
    if (!box.matches('[data-key]')) return;
    if (box.checked) saved[box.dataset.key] = true; else delete saved[box.dataset.key];
    try { localStorage.setItem(key, JSON.stringify(saved)); }
    catch { document.querySelector('#storage-note').textContent = 'Progress is available for this visit only'; }
    progress();
  });
  const texts = topics.map(topic => topic.textContent.toLowerCase());
  let beforeSearch;
  function filter() {
    const query = search.value.trim().toLowerCase();
    if (query && !beforeSearch) beforeSearch = topics.map(topic => topic.open);
    let count = 0;
    topics.forEach((topic, i) => {
      topic.hidden = !texts[i].includes(query);
      if (!topic.hidden) count++;
      if (query) topic.open = !topic.hidden;
      else if (beforeSearch) topic.open = beforeSearch[i];
    });
    if (!query) beforeSearch = undefined;
    document.querySelector('#results').textContent = query ? `${count} of 60 topics match` : '60 topics to explore';
    document.querySelector('#empty').hidden = count !== 0;
  }
  search.addEventListener('input', filter);
  document.querySelector('#expand').addEventListener('click', () => topics.forEach(t => { if (!t.hidden) t.open = true; }));
  document.querySelector('#collapse').addEventListener('click', () => topics.forEach(t => { t.open = false; }));
  function reveal() {
    let id; try { id = decodeURIComponent(location.hash.slice(1)); } catch { return; }
    if (!id) return;
    const target = document.getElementById(id);
    if (!target) return;
    search.value = ''; filter();
    const topic = target.closest('details');
    if (topic) topic.open = true;
    requestAnimationFrame(() => target.scrollIntoView({block: 'start'}));
  }
  window.addEventListener('hashchange', reveal);
  progress(); reveal();
})();
