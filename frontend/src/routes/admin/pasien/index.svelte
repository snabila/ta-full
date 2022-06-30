<script>
	import { onMount } from 'svelte';

	import { pageName } from '../../../stores/admin.js';

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
				console.log(patientList)
				if (patientList) {
					patientList = [...new Set(patientList)]
					for (let i = 0; i < patientList.length; i++) {
						const patient = await fetch('http://localhost:8080/auth/user/' + patientList[i], {
							headers: {'Content-Type': 'application/json', 'If-None-Match': '*'},
							credentials: 'include',
						})
						const temp = await patient.json()
						console.log(temp)
						
						// if (patient.code == 200) {
						// 	const temp = patient.json()
						// 	console.log(temp.username)
						// }
					}
				}
				// console.log(hosting)
				return {}
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
	<title>Pasien</title>
</svelte:head>

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
					<th class="px-4 py-3">Tanggal</th>
				</tr>
			</thead>
			<tbody class="bg-white divide-y dark:divide-gray-700 dark:bg-gray-800">
				<tr class="text-gray-700 dark:text-gray-400">
					<td class="px-4 py-5">
						<div class="flex items-center text-sm">
							<!-- Avatar with inset shadow -->
							<div class="relative hidden w-8 h-8 mr-3 rounded-full md:block">
								<img
									class="object-cover w-full h-full rounded-full"
									src="https://images.unsplash.com/flagged/photo-1570612861542-284f4c12e75f?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=200&fit=max&ixid=eyJhcHBfaWQiOjE3Nzg0fQ"
									alt=""
									loading="lazy"
								/>
								<div class="absolute inset-0 rounded-full shadow-inner" aria-hidden="true" />
							</div>
							<div>
								<a href="/admin/patients/id"><p class="font-semibold">John Doe</p></a>
							</div>
						</div>
					</td>
					<td class="px-4 py-5 text-sm">12</td>
					<td class="px-4 py-5 text-sm">24</td>
					<td class="px-4 py-5 text-sm"> 6/10/2020 </td>
				</tr>
			</tbody>
		</table>
	</div>
</div>
