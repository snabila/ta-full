export function parseDate(str_date) {
	return new Date(Date.parse(str_date)).toLocaleDateString('id-ID', {
		year: 'numeric',
		month: 'short',
		day: 'numeric',
		hour: '2-digit',
		hour12: true,
		minute: '2-digit',
		timeZone: 'Asia/Jakarta'
	});
}
