import http from 'k6/http';

const url = 'http://localhost:8000/';

export default function () {
	const tipos = [
		'GC',
		'PO',
	];
	
	const data = { correo: 'asdasd1@test.test', tipo: tipos[0] };

	for (let id = 1; id <= 10000; id++) {
		data.correo.replace(/[0-9]/, id);
		data.tipo = tipos[Math.floor(Math.random() * tipos.length)];
		http.post(url, JSON.stringify(data), {
			headers: { 'Content-Type': 'application/json' },
		});
	}
}