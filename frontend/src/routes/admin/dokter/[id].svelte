<script>
    import { goto } from '$app/navigation';
	import { fade } from 'svelte/transition';
	import { onMount } from 'svelte';
	import { pageName } from '../../../stores/admin.js';
    import { parseDate } from '$lib/date.js'

    export let doctor, monit

    // console.log(monit)

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
			if (data.role === 'admin'){				
				
                const doctor = await fetch('http://localhost:8080/auth/user/' + params.id, {
                    headers: {'Content-Type': 'application/json', 'If-None-Match': '*'},
                    credentials: 'include',
                })

                if (doctor.status == 200){
                    const doctorData = await doctor.json()
                    let monitData = []

                    console.log(doctorData.hosting)
                    for (let i = 0; i < doctorData.hosting.length; i++) {
                        const monit = await fetch('http://localhost:8080/monit/code/' + doctorData.hosting[i])
                        const record = await fetch('http://localhost:8080/record/code/' + doctorData.hosting[i])

                        const temp = await monit.json()
                        const temp2 = await record.json()
                        let temp3 = 0

                        if (temp2.code == 200) {
                            temp3 = temp2.data[0].length
                        }

                        if (temp.code == 200) {
                            monitData.push({
                                code: doctorData.hosting[i],
                                pasien: temp.data[0].participants.length,
                                respons: temp3
                            })
                        }
                    }

                    console.log(monitData)

                    return {
                        props: {
                            doctor: doctorData,
                            monit: monitData
                        }
                    }
                } else {
                    return {
                        status: 404,
                        error: 'Halaman tidak ditemukan'
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
	<title>{ doctor.name }</title>
</svelte:head>

<div in:fade={{delay: 500, duration: 500}} out:fade|local={{duration: 500}}>
    <!-- Details -->
	<div>
		<h4 class="mb-4 text-lg font-semibold text-gray-600 dark:text-gray-300">Detail</h4>
		<div class="px-5 py-4 mb-8 bg-white rounded-lg shadow-md dark:bg-gray-800 text-sm">
			<div class="grid grid-cols-3 mb-4">
				<p class="font-semibold">Nama</p>
				<p class="col-span-2 ml-2">{ doctor.name }</p>
			</div>
			<div class="grid grid-cols-3 mb-4">
				<p class="font-semibold">Username</p>
				<p class="col-span-2 ml-2">{ doctor.username }</p>
			</div>
            <div class="grid grid-cols-3 mb-4">
				<p class="font-semibold">Tanggal Daftar</p>
				<p class="col-span-2 ml-2">{ parseDate(doctor.createdDate) }</p>
			</div>
            <div class="grid grid-cols-3">
				<p class="font-semibold">Terakhir Login</p>
				<p class="col-span-2 ml-2">{ parseDate(doctor.lastLoginDate) }</p>
			</div>
		</div>
	</div>

    <!-- Monitoring -->
    <div>
        <h4 class="mb-4 text-lg font-semibold text-gray-600 dark:text-gray-300">Form Monitoring</h4>

        <!-- table -->
        <div class="w-full overflow-hidden rounded-lg shadow-xs">
			<div class="w-full overflow-x-auto">
				<table class="w-full whitespace-no-wrap border border-neutral-200">
					<thead>
						<tr
							class="text-xs font-semibold tracking-wide text-left text-gray-500 uppercase border-b dark:border-gray-700 bg-gray-50 dark:text-gray-400 dark:bg-gray-800"
						>
							<th class="px-4 py-3">Kode Monitoring</th>
							<th class="px-4 py-3">Jumlah Pasien</th>
							<th class="px-4 py-3">Jumlah Respon</th>
						</tr>
					</thead>
					<tbody class="bg-white divide-y dark:divide-gray-700 dark:bg-gray-800">
                        {#each monit as m}
						<tr class="text-gray-700 dark:text-gray-400">
							<td class="px-4 py-3 text-sm">
                                <a href="/admin/monitoring/{ m.code }"><p class="font-semibold">{ m.code }</p></a>
							</td>
							<td class="px-4 py-3 text-sm">{ m.pasien }</td>

							<td class="px-4 py-3 text-sm">{ m.respons }</td>
						</tr>
						<!-- {/each} -->
                        {/each}
					</tbody>
				</table>
			</div>
		</div>
    </div>
</div>