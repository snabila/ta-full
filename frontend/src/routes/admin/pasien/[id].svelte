<script>
	import { fade } from 'svelte/transition';
	import { onMount } from 'svelte';
	import { pageName } from '../../../stores/admin.js';
	import { parseDate } from '$lib/date.js'
	export let patient, monit
	let monitList = []
	for (let i = 0; i < monit.length; i++) {
		monitList.push(monit[i]['code'])
	}

	console.log(monit)

	onMount(() => {
		pageName.update(() => document.title);
	});

</script>

<script context="module">
	export async function load({ params, fetch }) {
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
					const patients = await fetch('http://localhost:8080/monit/code/' + hosting[i])
					const temp = await patients.json()

					if (temp.code == 200) {
						if (temp.data[0].participants) {
							const inCode = temp.data[0].participants.includes(params.id)
							if (inCode) {
								monitList.push(temp.data[0].code)
							}
						}
					}
				}
				
				if (monitList.length > 0) {
					console.log(monitList)
					const patient = await fetch('http://localhost:8080/auth/user/' + params.id, {
						headers: {'Content-Type': 'application/json', 'If-None-Match': '*'},
						credentials: 'include',
					})
					const patientData = await patient.json()

					let recordData = []
					for (let i = 0; i < monitList.length; i++) {
						const records = await fetch('http://localhost:8080/record/code/' + monitList[i] + '/' + params.id)
						const temp = await records.json()

						const questions = await fetch('http://localhost:8080/monit/code/' + monitList[i] + '/q')
						const temp2 = await questions.json()

						if (temp.code == 200) {
							recordData.push({ 
								code: monitList[i], 
								data: temp.data[0],
								questions: temp2.data[0]
							})
						} else {
							recordData.push({
								code: monitList[i],
								data: [],
								questions: temp2.data[0] 
							})
						}
					}

					return {
						props: {
							patient: patientData,
							monit: recordData
						}
						
					}
				} 
				return {
					status: 403,
					error: 'Akun anda tidak memiliki akses terhadap halaman ini.'
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
	<title>{ patient.name }</title>
</svelte:head>

<div in:fade={{delay: 500, duration: 500}} out:fade|local={{duration: 500}}>
	<!-- Details -->
	<div>
		<h4 class="mb-4 text-lg font-semibold text-gray-600 dark:text-gray-300">Detail</h4>
		<div class="px-5 py-4 mb-8 bg-white rounded-lg shadow-md dark:bg-gray-800 text-sm">
			<div class="grid grid-cols-3 mb-4">
				<p class="font-semibold">Nama</p>
				<p class="col-span-2 ml-2">{ patient.name }</p>
			</div>
			<div class="grid grid-cols-3 mb-4">
				<p class="font-semibold">Username</p>
				<p class="col-span-2 ml-2">{ patient.username }</p>
			</div>
			<div class="grid grid-cols-3">
				<p class="font-semibold">Terdaftar di</p>
				<p class="col-span-2 ml-2">
					{#each monitList as monit}
						{monit} <br>
					{/each}
				</p>
			</div>
		</div>
	</div>

	<!-- Forms -->
	{#each monit as mnt}
	<div class="mb-8">
		<h4 class="mb-4 text-lg font-semibold text-gray-600 dark:text-gray-300">{ mnt['code'] }</h4>
		{#if mnt['data'].length > 0}
		<table class="w-full whitespace-no-wrap border border-neutral-200">
			<thead>
				<tr
					class="text-xs font-semibold tracking-wide text-left text-gray-500 uppercase border-b dark:border-gray-700 bg-gray-50 dark:text-gray-400 dark:bg-gray-800"
				>
					<th class="px-4 py-3">Tanggal</th>
					{#each mnt['questions'] as q, i (q['id'])}
					<th class="px-4 py-3">{ q['label'] }</th>
					{/each}
				</tr>
			</thead>
			<tbody class="bg-white divide-y dark:divide-gray-700 dark:bg-gray-800">
				{#each mnt['data'] as record}
				<tr class="text-gray-700 dark:text-gray-400">
					<td class="px-4 py-5 text-sm">{ parseDate(record['submit_time']) }</td>
					{#each record['answers'] as ans, i (ans['q_id'])}
					<td class="px-4 py-5 text-sm">{ ans['answer'] }</td>
					{/each}
				</tr>
				{/each}
			</tbody>
		</table>
		{:else}
			<div class="text-center">
				<h5 class="text-xl font-bold text-neutral-600">No entries</h5>
				<p class="text-sm text-neutral-600 italic">Pasien ini belum mengisi monitoring { mnt['code'] }</p>
			</div>
		{/if}
	</div>
	{/each}
</div>