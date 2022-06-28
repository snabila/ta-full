<script>
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { pageName } from '../../../stores/admin.js';

	let data, uname
	let data2 = []

	onMount(async () => {
		pageName.update(() => document.title);

		try {
			const response = await fetch('http://localhost:8080/auth/user', {
				headers: {'Content-Type': 'application/json'},
				credentials: 'include',
			})
			const content = await response.json()
			data = content
			uname = content.username

			if (response.status == 401) {
				goto('/')
			} else {
				console.log(content.hosting)
				let codes = content.hosting
				let codeslen = codes.length
				for (let i = 0; i < codeslen; i++) {
					let datakode = await fetch('http://localhost:8080/monit/code/' + codes[i], {
						headers: {'Content-Type': 'application/json'},
						credentials: 'include',
					})
					data2.push(await datakode.json())
					// data2 = await datakode.json()
					console.log(data2)
				}
				console.log(data2[0]['data'][0]['name'])

			}
		} catch (error) {
			goto('/login')
		}
	});
</script>

<svelte:head>
	<title>Form Monitoring</title>
</svelte:head>

<div class="w-full overflow-hidden rounded-lg shadow-xs">
	<div class="w-full overflow-x-auto">
		<table class="w-full whitespace-no-wrap border border-neutral-200">
			<thead>
				<tr
					class="text-xs font-semibold tracking-wide text-left text-gray-500 uppercase border-b dark:border-gray-700 bg-gray-50 dark:text-gray-400 dark:bg-gray-800"
				>
					<th class="px-4 py-3">Nama</th>
					<th class="px-4 py-3">Jumlah Pasien</th>
					<th class="px-4 py-3">Respon</th>
					<th class="px-4 py-3">Edit Terakhir</th>
				</tr>
			</thead>
			{#each data2 as input}
				<tbody class="bg-white divide-y dark:divide-gray-700 dark:bg-gray-800">
				<tr class="text-gray-700 dark:text-gray-400">
					<td class="px-4 py-5">
						<div class="flex items-center text-sm">
							<div>
								<a href="/admin/monitoring/id"><p class="font-semibold">{ input['data'][0]['name'] }</p></a>
							</div>
						</div>
					</td>
					<td class="px-4 py-5 text-sm"></td>
					<td class="px-4 py-5 text-sm"></td>
					<td class="px-4 py-5 text-sm"></td>
				</tr>
			</tbody>
			{/each }
			<tbody class="bg-white divide-y dark:divide-gray-700 dark:bg-gray-800">
				<tr class="text-gray-700 dark:text-gray-400">
					<td class="px-4 py-5">
						<div class="flex items-center text-sm">
							<div>
								<a href="/admin/monitoring/id"><p class="font-semibold">Monitoring Psoriasis</p></a>
							</div>
						</div>
					</td>
					<td class="px-4 py-5 text-sm">12</td>
					<td class="px-4 py-5 text-sm">36</td>
					<td class="px-4 py-5 text-sm"> 6/10/2020 </td>
				</tr>
			</tbody>
		</table>
	</div>
</div>