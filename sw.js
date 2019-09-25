addEventListener('install', () => {
    skipWaiting();
  });
  
  addEventListener('activate', () => {
    clients.claim();
  });
  
  addEventListener('fetch', (event) => {
    if (event.request.method == 'POST') {
      event.respondWith(fetch('/webapk-maskable/'));
  
      event.waitUntil(async function () {
        const data = await event.request.formData();
        const client = await self.clients.get(event.resultingClientId);
  
        const old_files = data.getAll('old_image_file');
        const new_files = data.getAll('new_image_file');
        const text_files = data.getAll('text_files');
        const text = data.get('text');
        const title = data.get('title');
        client.postMessage({ old_files, new_files, text, title, text_files });
      }());
    } else if (event.request.method == "GET" && event.request.url.indexOf('sw-post') > -1) {
  
      event.respondWith(fetch('./'));
      event.waitUntil(async function () {
        const client = await self.clients.get(event.resultingClientId);
        const url = new URL(event.request.url);
        const text = url.searchParams.get('text');
        client.postMessage({ text });
  
      }());
    }
  
  });