<script>
	import { onMount } from 'svelte';
	import NoEntry from '../../../components/admin/NoEntry.svelte';
	import { fade } from 'svelte/transition';
	import { pageName } from '../../../stores/admin.js';
	export let patient
	console.log(patient.length)

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
		
		if (response.status == 200) {
			if (data.role === 'dokter'){
				let hosting = data.hosting
				let patientList = []
				let patientEx = []

				for (let i = 0; i < hosting.length; i++) {

					const patients = await fetch('http://localhost:8080/monit/code/' + hosting[i])
					const temp = await patients.json()

					if (temp.code == 200) {
						if (temp.data[0].participants) {
							patientList = patientList.concat(temp.data[0].participants)
						}
					}
				}
				// console.log(hosting)
				// console.log(patientList)
				if (patientList) {
					patientList = [...new Set(patientList)]
					for (let i = 0; i < patientList.length; i++) {
						let monit = 0
						let record = 0
						const patient = await fetch('http://localhost:8080/auth/user/' + patientList[i], {
							headers: {'Content-Type': 'application/json', 'If-None-Match': '*'},
							credentials: 'include',
						})
						const temp = await patient.json()
						// console.log(temp.subscribed)
						
						if (temp.subscribed) {
							for (let i = 0; i < temp.subscribed.length; i++) {
								if (hosting.includes(temp.subscribed[i])) {
									const records = await fetch('http://localhost:8080/record/code/' + temp.subscribed[i] + '/' + temp.username)
									const recordN = await records.json()
									if (recordN.code == 200){
										record += recordN.data[0].length
									}
									monit += 1
								}
							}
						}

						patientEx.push({
							uname: temp.username,
							monit: monit,
							record: record
						})
					}
				}
				// console.log(hosting)
				return {
					props: {patient: patientEx}
				}
			}
			return {
				status: 403,
				error: 'Akun anda tidak memiliki akses terhadap halaman ini.'
			}
			
		}
		return {
			status: 302,
			redirect: '/login'
		}	
		
	}
</script>

<svelte:head>
	<title>Pasien</title>
</svelte:head>

<div in:fade={{delay: 500, duration: 500}} out:fade|local={{duration: 500}}>
	{#if patient.length > 0}
	<!-- Table -->
	<div class="w-full overflow-hidden rounded-lg shadow-xs">
		<div class="w-full overflow-x-auto">
			<table class="w-full whitespace-no-wrap border border-neutral-200">
				<thead>
					<tr
						class="text-xs font-semibold tracking-wide text-left text-gray-500 uppercase border-b dark:border-gray-700 bg-gray-50 dark:text-gray-400 dark:bg-gray-800"
					>
						<th class="px-4 py-3">Nama</th>
						<th class="px-4 py-3">Jumlah Form</th>
						<th class="px-4 py-3">Respon</th>
					</tr>
				</thead>
				<tbody class="bg-white divide-y dark:divide-gray-700 dark:bg-gray-800">
					{#each patient as p}
					<tr class="text-gray-700 dark:text-gray-400">
						<td class="px-4 py-3">
							<a href="/admin/pasien/{ p.uname }"><p class="font-semibold">{ p.uname }</p></a>
						</td>
						<td class="px-4 py-5 text-sm">{ p.monit }</td>
						<td class="px-4 py-5 text-sm">{ p.record }</td>
					</tr>
					{/each}
				</tbody>
			</table>
		</div>
	</div>
	{:else}
		<NoEntry title='No entries' message='Belum ada pasien yang terdaftar pada monitoring anda. Undang pasien dengan membagikan kode monitoring anda'/>
	{/if}
</div>