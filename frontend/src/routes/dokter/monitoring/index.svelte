<script>
	import { onMount } from 'svelte';
	import { fade } from 'svelte/transition';
	import NoEntry from '../../../components/admin/NoEntry.svelte';
	import { pageName } from '../../../stores/admin.js';

	onMount(async () => {
		pageName.update(() => document.title);
	});

	export let monitList

	console.log(monitList)
</script>

<script context="module">
	export async function load({ fetch }) {
		const response = await fetch('http://localhost:8080/auth/user', {
			headers: {'Content-Type': 'application/json', 'If-None-Match': '*'},
			credentials: 'include',
		})

		let data = await response.json()
		
		if (response.status == 200) {
			if (data.role === 'dokter'){
				let hosting = data.hosting
				let monitList = []

				for (let i = 0; i < hosting.length; i++) {
					const response = await fetch('http://localhost:8080/monit/code/' + hosting[i])
					const temp = await response.json()
					let item = temp.data[0]

					const records = await fetch('http://localhost:8080/record/code/' + hosting[i])
					const temp2 = await records.json()
					let recordN
					if (temp2.code == 200) {
						recordN = temp2.data[0].length
					} else {
						recordN = 0
					}

					monitList.push({ monit: item, recordN: recordN})
				}

				return {
					props: { monitList: monitList }
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
	<title>Form Monitoring</title>
</svelte:head>

<div in:fade={{delay: 500, duration: 500}} out:fade|local={{duration: 500}}>
	{#if monitList.length > 0}
	<!-- Table -->
	<div class="w-full overflow-hidden rounded-lg shadow-xs">
		<div class="w-full overflow-x-auto">
			<table class="w-full whitespace-no-wrap border border-neutral-200 table-fixed border-collapse">
				<thead>
					<tr
						class="text-xs font-semibold tracking-wide text-left text-gray-500 uppercase border-b dark:border-gray-700 bg-gray-50 dark:text-gray-400 dark:bg-gray-800"
					>
						<th class="px-4 py-3 border border-neutral-200">Nama</th>
						<th class="px-4 py-3 border border-neutral-200">Jumlah Pasien</th>
						<th class="px-4 py-3 border border-neutral-200">Respon</th>
					</tr>
				</thead>
				{#each monitList as monit}
					<tbody class="bg-white divide-y dark:divide-gray-700 dark:bg-gray-800">
					<tr class="text-gray-700 dark:text-gray-400">
						<td class="px-4 py-3 border border-neutral-200">
							<a href="/dokter/monitoring/{ monit.monit.code }" class="font-semibold text-sm">{ monit.monit.name }</a>
						</td>
						{#if monit.monit.participants}
							<td class="px-4 py-3 text-sm border border-neutral-200">{ monit.monit.participants.length }</td>
						{:else}
							<td class="px-4 py-3 text-sm border border-neutral-200">0</td>
						{/if}
						<td class="px-4 py-3 text-sm border border-neutral-200">{ monit.recordN }</td>
					</tr>
				</tbody>
				{/each }
			</table>
		</div>
	</div>
	{:else}
		<NoEntry title='No entries' message="Anda belum memiliki monitoring apapun."/>
	{/if}
</div>