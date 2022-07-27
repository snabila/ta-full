<script>
	import { fade } from 'svelte/transition';
	import { onMount } from 'svelte';
	import { pageName } from '../../../stores/admin.js';
	import { parseDate } from '$lib/date.js'
	export let patient, monit
	// let monitList = []
	// for (let i = 0; i < monit.length; i++) {
	// 	monitList.push(monit[i]['code'])
	// }

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
				
                const patient = await fetch('http://localhost:8080/auth/user/' + params.id, {
                    headers: {'Content-Type': 'application/json', 'If-None-Match': '*'},
                    credentials: 'include',
                })
                if (patient.status == 200) {
                    const patientData = await patient.json()

                    let recordData = []

                    if (patientData.subscribed.length > 0) {
                        for (let i = 0; i < patientData.subscribed.length; i++) {                    
                            const records = await fetch('http://localhost:8080/record/code/' + patientData.subscribed[i] + '/' + params.id)
                            const temp = await records.json()

                            const questions = await fetch('http://localhost:8080/monit/code/' + patientData.subscribed[i] + '/q')
                            const temp2 = await questions.json()

                            if (temp.code == 200) {
                                let download_file
                                let download_href
                                const csv = await fetch('http://localhost:8000/records/code/' + patientData.subscribed[i] + '/' + params.id + '/csv', {
                                    method: 'GET',
                                    headers: { 'Content-Type': 'text/csv' },
                                })
                                if (csv.status === 200) {
                                    const data = await csv.text()
                                    const blob = new Blob([data], { type: 'text/csv' });
                                    download_href = window.URL.createObjectURL(blob)
                                    download_file = patientData.subscribed[i] + '-' + params.id + '.csv'
                                    // console.log(data)
                                    recordData.push({ 
                                        code: patientData.subscribed[i], 
                                        data: temp.data[0],
                                        questions: temp2.data[0],
                                        download_file: download_file,
                                        download_href: download_href
                                    })
                                } else {
                                    recordData.push({ 
                                        code: patientData.subscribed[i], 
                                        data: temp.data[0],
                                        questions: temp2.data[0],
                                        download_file: '',
                                        download_href: ''
                                    })
                                }
                            } else {
                                recordData.push({
                                    code: patientData.subscribed[i],
                                    data: [],
                                    questions: temp2.data[0],
                                    download_file: '',
                                    download_href: ''
                                })
                            }

                        }
                    }

                    return {
                        props: {
                            patient: patientData,
                            monit: recordData
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
                    {#if monit.length > 0}
                        {#each monit as m}
                            {m.code} <br>
                        {/each}
                    {:else}
                        -
                    {/if}
				</p>
			</div>
		</div>
	</div>

    <!-- Monitoring -->
    {#each monit as mnt}
    <div class="mb-8">
        <div class="flex flex-row justify-between">
            <h4 class="mb-4 text-lg font-semibold text-gray-600 dark:text-gray-300">{ mnt['code'] }</h4>
            <a href={mnt.download_href} download={mnt.download_file} class="text-purple-600">Download Respon</a>
        </div>
        
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