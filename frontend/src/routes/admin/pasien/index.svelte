<script>
	import { onMount } from 'svelte';
	import NoEntry from '../../../components/admin/NoEntry.svelte';
	import { fade } from 'svelte/transition';
	import { pageName } from '../../../stores/admin.js';
    import { parseDate } from '$lib/date.js'
	export let patientList
	// console.log(doctorList)

	onMount(() => {
		pageName.update(() => document.title);
	});
</script>

<script context="module">
    export async function load({ fetch }) {
        const response = await fetch('http://localhost:8080/auth/user', {
			method : 'GET',
			headers: {'Content-Type': 'application/json', 'If-None-Match': '*'},
			credentials: 'include',
		})

        let data = await response.json()

        if (response.status == 200) {
            if (data.role === 'admin') {
                const patients = await fetch('http://localhost:8003/api/users?role=pasien')

                const patientList = await patients.json()
                
                if (patientList) {
					patientList.sort(function(a,b) {
						const keyA = new Date(a.lastLoginDate), keyB = new Date(b.lastLoginDate);
						if (keyA > keyB) return -1;
						if (keyA < keyB) return 1;
						return 0;
					})
				}
                return {
                    props: {
                        patientList: patientList,
                    }
                }
            } else if (data.role === 'dokter'){
				return {
					status: 302,
					redirect: '/dokter'
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
	<title>Pasien</title>
</svelte:head>

<div in:fade={{delay: 500, duration: 500}} out:fade|local={{duration: 500}}>
    <!-- Table -->
	<div class="w-full overflow-hidden rounded-lg shadow-xs">
		<div class="w-full overflow-x-auto">
			<table class="w-full whitespace-no-wrap border border-neutral-200">
				<thead>
					<tr
						class="text-xs font-semibold tracking-wide text-left text-gray-500 uppercase border-b dark:border-gray-700 bg-gray-50 dark:text-gray-400 dark:bg-gray-800"
					>
						<th class="px-4 py-3">Nama</th>
						<th class="px-4 py-3">Jumlah Form Terdaftar</th>
						<th class="px-4 py-3">Login Terakhir</th>
					</tr>
				</thead>
				<tbody class="bg-white divide-y dark:divide-gray-700 dark:bg-gray-800">
					{#each patientList as patient}
					<tr class="text-gray-700 dark:text-gray-400">
						<td class="px-4 py-3 text-sm">
							<a href="/admin/pasien/{ patient.username }"><p class="font-semibold">{ patient.username }</p></a>
						</td>
						<td class="px-4 py-3 text-sm">{ patient.subscribed.length }</td>
						<td class="px-4 py-3 text-sm">{ parseDate(patient.lastLoginDate) }</td>
					</tr>
					{/each}
				</tbody>
			</table>
		</div>
	</div>
</div>