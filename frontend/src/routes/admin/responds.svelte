<script>
	import NoEntry from '../../components/admin/NoEntry.svelte';
	import { onMount } from 'svelte';
	import { fade } from 'svelte/transition';
	import { pageName } from '../../stores/admin';
	import { parseDate } from '$lib/date.js'
	export let recordList

	onMount(() => {
		pageName.update(() => document.title);
	});
</script>

<script context="module">
	export async function load({ fetch }) {
		const response = await fetch('http://localhost:8080/auth/user', {
			headers: {'Content-Type': 'application/json', 'If-None-Match': '*'},
			credentials: 'include',
		})

		let data = await response.json()
		// console.log(data.value)
		
		if (response.status == 200) {
			if (data.role === 'dokter'){
				let hosting = data.hosting
				let recordList = []

				for (let i = 0; i < hosting.length; i++) {
					const records = await fetch('http://localhost:8080/record/code/' + hosting[i])
					const temp2 = await records.json()

					// cek kode monitong punya record atau ngga
					if (temp2.code == 200) {
						// const record = temp2.data[0].
						recordList = recordList.concat(temp2.data[0])
						// recordN = temp2.data[0].length
					}

					// recordList.push({ monit: item, recordN: recordN})
				}
				if (recordList) {
					recordList.sort(function(a,b) {
						const keyA = new Date(a.submit_time), keyB = new Date(b.submit_time);
						if (keyA > keyB) return -1;
						if (keyA < keyB) return 1;
						return 0;
					})
				}
				// console.log(recordList)
				return {
					props: { recordList: recordList }
				}
			} else {
				return {
					status: 403,
					error: 'Akun anda tidak memiliki akses terhadap halaman ini.'
				}
			}
		} else {
			return {
				status: 302,
				redirect: '/login'
			}	
		}
	}
</script>

<svelte:head>
	<title>Respon</title>
</svelte:head>

<div in:fade={{delay: 500, duration: 500}} out:fade|local={{duration: 500}}>
	<!-- Table -->
	{#if recordList.length > 0}
		<div class="w-full overflow-hidden rounded-lg shadow-xs">
			<div class="w-full overflow-x-auto">
				<table class="w-full whitespace-no-wrap border border-neutral-200">
					<thead>
						<tr
							class="text-xs font-semibold tracking-wide text-left text-gray-500 uppercase border-b dark:border-gray-700 bg-gray-50 dark:text-gray-400 dark:bg-gray-800"
						>
							<th class="px-4 py-3">Respon Terbaru</th>
							<th class="px-4 py-3">Form Monitoring</th>
							<th class="px-4 py-3">Tanggal</th>
						</tr>
					</thead>
					<tbody class="bg-white divide-y dark:divide-gray-700 dark:bg-gray-800">
						{#each recordList as record}
						<tr class="text-gray-700 dark:text-gray-400">
							<td class="px-4 py-3 text-sm"><a href="/admin/pasien/{ record.user }"><p class="font-semibold">{ record.user }</p></a></td>
							<td class="px-4 py-3 text-sm">{ record.qs_code }</td>
							<td class="px-4 py-3 text-sm">{ parseDate(record.submit_time) }</td>
						</tr>
						{/each}
					</tbody>
				</table>
			</div>
		</div>
	{:else}
		<NoEntry title='No entries' message='Monitoring anda belum memiliki respon, undang pasien anda dengan membagikan kode monitoring anda'/>
	{/if}
</div>