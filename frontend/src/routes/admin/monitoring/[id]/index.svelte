<script>
	import { goto } from '$app/navigation';
	import { fade } from 'svelte/transition';
	import { onMount } from 'svelte';
	import { pageName } from '../../../../stores/admin.js';
    
    export let monit, recordN, download_file, download_href

	onMount(() => {
		pageName.update(() => document.title);
	});

    // let donwload_href = ''
    // let download_file = ''

    // const downloadResponds = async() => {
    //     const response = await fetch('http://localhost:8000/records/code/' + monit.code + '/csv', {
    //         method: 'GET',
    //         headers: { 'Content-Type': 'text/csv' },
    //     })
    //     if (response.status === 200) {
    //         const data = await response.text()
    //         const blob = new Blob([data], { type: 'text/csv' });
    //         donwload_href = window.URL.createObjectURL(blob)
    //         download_file = 'download.csv'
    //         console.log(data)
    //     }
        
    // }

    // Problem di host-pull dia ambil username dari cookie
    // const deleteMonit = async () => {
	// 	const response = await fetch('http://localhost:8080/monit/code/' + monit.code, {
    //         method: 'DELETE',
    //         headers: { 'Content-Type': 'application/json' },
    //     })
	// 	const hostpull = await fetch('http://localhost:8003/api/host-pull/', {
	// 		method: 'PUT',
	// 		headers: { 'Content-Type': 'application/json' },
	// 		credentials: 'include',
    //         body: JSON.stringify({
    //             "code": monit.code,
    //         })
	// 	})
	// 	const subspullall = await fetch('http://localhost:8080/monit/subs-pull-all', {
	// 		method: 'PUT',
	// 		headers: { 'Content-Type': 'application/json' },
	// 		body: JSON.stringify({
	// 			"code": monit.code
	// 		})
	// 	})
	// 	await goto('/admin/monitoring')
	// }
</script>

<script context="module">
	export async function load({ params, fetch }) {
		const response = await fetch('http://localhost:8080/auth/user', {
			headers: {'Content-Type': 'application/json'},
			credentials: 'include',
		})
		let data = await response.json()
		
		if (response.status == 200) {
			if (data.role === 'admin'){
				const response = await fetch('http://localhost:8080/monit/code/' + params.id)
				
				const temp = await response.json()
				if (temp.code == 200) {
					data = temp.data[0]

					const records = await fetch('http://localhost:8080/record/code/' + params.id)
					const temp2 = await records.json()

					let recordN = 0
                    let download_file = ''
                    let download_href = ''
					if (temp2.code == 200) {
						recordN = temp2.data[0].length
                        const csv = await fetch('http://localhost:8000/records/code/' + params.id + '/csv', {
                            method: 'GET',
                            headers: { 'Content-Type': 'text/csv' },
                        })
                        if (csv.status === 200) {
                            const data = await csv.text()
                            const blob = new Blob([data], { type: 'text/csv' });
                            download_href = window.URL.createObjectURL(blob)
                            download_file = params.id + '.csv'
                            // console.log(data)
                        }
					}
					
					return {
						props: {
							monit: data,
							recordN: recordN,
                            download_href: download_href,
                            download_file: download_file
						}
					}
				} 
				return {
					status: temp.code,
					error: temp.message
				}
				
			} else if (data.role === 'dokter'){
				return {
					status: 302,
					redirect: '/dokter'
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
	<title>{ monit.name }</title>
</svelte:head>

<div in:fade={{delay: 500, duration: 500}} out:fade|local={{duration: 500}}>
    <!-- Cards -->
    <div class="grid gap-6 mb-8 md:grid-cols-2">
        <!-- Card Pasien -->
        <div
            class="flex items-center p-4 bg-white rounded-lg shadow-xs dark:bg-gray-800 border border-neutral-200"
        >
            <div
                class="p-3 mr-4 text-green-500 bg-green-100 rounded-full dark:text-green-100 dark:bg-green-500"
            >
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-5 w-5"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                >
                    <path
                        d="M13 6a3 3 0 11-6 0 3 3 0 016 0zM18 8a2 2 0 11-4 0 2 2 0 014 0zM14 15a4 4 0 00-8 0v3h8v-3zM6 8a2 2 0 11-4 0 2 2 0 014 0zM16 18v-3a5.972 5.972 0 00-.75-2.906A3.005 3.005 0 0119 15v3h-3zM4.75 12.094A5.973 5.973 0 004 15v3H1v-3a3 3 0 013.75-2.906z"
                    />
                </svg>
            </div>
            <div>
                <p class="mb-2 text-sm font-medium text-gray-600 dark:text-gray-400">Jumlah Pasien</p>
                <p class="text-lg font-semibold text-gray-700 dark:text-gray-200">
                    {#if monit.participants}
                        { monit.participants.length }
                    {:else} 0
                    {/if}
                </p>
            </div>
        </div>

        <!-- Card respon -->
        <div
		class="flex items-center p-4 bg-white rounded-lg shadow-xs dark:bg-gray-800 border border-neutral-200"
	    >
            <div
                class="p-3 mr-4 text-blue-500 bg-blue-100 rounded-full dark:text-blue-100 dark:bg-blue-500"
            >
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="h-5 w-5"
                    viewBox="0 0 20 20"
                    fill="currentColor"
                >
                    <path
                        fill-rule="evenodd"
                        d="M18 5v8a2 2 0 01-2 2h-5l-5 4v-4H4a2 2 0 01-2-2V5a2 2 0 012-2h12a2 2 0 012 2zM7 8H5v2h2V8zm2 0h2v2H9V8zm6 0h-2v2h2V8z"
                        clip-rule="evenodd"
                    />
                </svg>
            </div>
            <div>
                <p class="mb-2 text-sm font-medium text-gray-600 dark:text-gray-400">Total Respon</p>
                <p class="text-lg font-semibold text-gray-700 dark:text-gray-200">{ recordN }</p>
            </div>
	    </div>
    </div>

    <div class="grid gap-6 mb-8 md:grid-cols-3 xl:grid-cols-3">
        <!-- Left section -->
        <div class="md:col-span-2">
            <!-- Details -->
            <div>
                <h4 class="mb-4 text-lg font-semibold text-gray-600 dark:text-gray-300">Detail</h4>
                <div class="px-5 py-4 mb-8 bg-white rounded-lg shadow-md dark:bg-gray-800 text-sm">
                    <div class="grid grid-cols-3 mb-4">
                        <p class="font-semibold">Nama Form</p>
                        <p class="col-span-2 ml-2">{ monit.name }</p>
                    </div>
                    <div class="grid grid-cols-3 mb-4">
                        <p class="font-semibold">Kode Form</p>
                        <p class="col-span-2 ml-2">{ monit.code }</p>
                    </div>
                    <div class="grid grid-cols-3">
                        <p class="font-semibold">Deskripsi</p>
                        {#if monit.desc }<p class="col-span-2 ml-2 leading-relaxed">{ monit.desc }</p>
                        {:else} <p class="col-span-2 ml-2 leading-relaxed italic">Monitoring ini tidak memiliki deskripsi</p>
                        {/if}
                    </div>
                </div>
            </div>

            <!-- Fields -->
            <div>
                <h4 class="mb-4 text-lg font-semibold text-gray-600 dark:text-gray-300">Fields</h4>
                <div class="px-5 pb-1 mb-8 bg-white rounded-lg shadow-md dark:bg-gray-800 text-sm divide-y">
                    {#each monit.questions as question}
                        <div class="pt-4">
                            <p class="font-semibold italic mb-4">Field { question.id }</p>
                            <div class="grid grid-cols-3 mb-4">
                                <p class="font-semibold">Label</p>
                                <p class="col-span-2 ml-2">{ question.label }</p>
                            </div>
                            <div class="grid grid-cols-3 mb-4">
                                <p class="font-semibold">Tipe Jawaban</p>
                                {#if question.answer_type == 'str'}
                                    <p class="col-span-2 ml-2">Teks Pendek</p>
                                {:else if question.answer_type == 'int'} <p class="col-span-2 ml-2">Numerik</p>
                                {/if}
                                
                            </div>
                            <div class="grid grid-cols-3 mb-4">
                                <p class="font-semibold">Pertanyaan</p>
                                <p class="col-span-2 ml-2">{ question.question }</p>
                            </div>
                        </div>
                    {/each}				
                </div>
            </div>
        </div>

        <!-- Right section -->
        <div>
            <!-- Pengaturan -->
            <div>
                <h4 class="mb-4 text-lg font-semibold text-gray-600 dark:text-gray-300">Pengaturan</h4>
                <div class="px-5 py-4 mb-8 bg-white rounded-lg shadow-md dark:bg-gray-800 text-sm">
                    <!-- <div class="flex justify-between mb-4">
                        <p class="font-semibold">Reminder</p>
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            class="h-5 w-5 text-green-500"
                            viewBox="0 0 20 20"
                            fill="currentColor"
                        >
                            <path
                                fill-rule="evenodd"
                                d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
                                clip-rule="evenodd"
                            />
                        </svg>
                    </div>

                    <div class="flex justify-between mb-6">
                        <p class="font-semibold">Open join</p>
                        <svg
                            xmlns="http://www.w3.org/2000/svg"
                            class="h-5 w-5 text-red-600"
                            viewBox="0 0 20 20"
                            fill="currentColor"
                        >
                            <path
                                fill-rule="evenodd"
                                d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z"
                                clip-rule="evenodd"
                            />
                        </svg>
                    </div> -->

                    <a
                        class="flex justify-center w-full px-4 py-2 text-sm font-medium leading-5 text-white transition-colors duration-150 bg-purple-600 border border-transparent rounded-lg active:bg-purple-600 hover:bg-purple-700 focus:outline-none focus:shadow-outline-purple mb-4"
                        href="/admin/monitoring/{ monit.code }/edit"
                    >
                        Edit Form
                    </a>

                    <a
                        class="flex justify-center w-full px-4 py-2 text-sm font-medium leading-5 text-purple-600 transition-colors duration-150 bg-white border border-purple-600 rounded-lg active:bg-purple-100 hover:bg-purple-100 focus:outline-none focus:shadow-outline-purple mb-4"
                        
                        href={download_href}
                        download={download_file}
                        
                    >
                        Download Respon Pasien
                    </a>

                    <button
                        class="flex justify-center w-full px-4 py-2 text-sm font-medium leading-5 text-red-600 transition-colors duration-150 bg-white border border-red-600 rounded-lg active:bg-red-100 hover:bg-red-100 focus:outline-none focus:shadow-outline-purple"
                        
                    >
                        Hapus Form
                    </button>
                </div>
            </div>

            <!-- Pasien -->
            <div>
                <h4 class="mb-4 text-lg font-semibold text-gray-600 dark:text-gray-300">Pasien</h4>
                <div class="px-5 py-4 mb-8 bg-white rounded-lg shadow-md dark:bg-gray-800 text-sm">
                    <!-- Header -->
                    <div class="flex justify-between mb-4">
                        <p class="font-semibold">Total</p>
                        <p class="font-semibold">
                            {#if monit.participants}
                                { monit.participants.length }
                            {:else} 0
                            {/if}
                        </p>
                    </div>

                    <hr />

                    <!-- List pasien -->
                    {#if monit.participants}
                        <!-- {#if monit.participants.length > 5}
                            {#each {length: 4} as _, i}
                                <div class="flex justify-between items-center mt-4">
                                    <a href="/admin/pasien/{ monit.participants[i] }" class="font-semibold">{ monit.participants[i] }</a>
                                    <svg
                                        xmlns="http://www.w3.org/2000/svg"
                                        class="h-4 w-4 ml-1"
                                        fill="none"
                                        viewBox="0 0 24 24"
                                        stroke="currentColor"
                                        stroke-width="2"
                                    >
                                        <path
                                            stroke-linecap="round"
                                            stroke-linejoin="round"
                                            d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                                        />
                                    </svg>
                                </div>
                            {/each}
                            <button class="mt-6 flex items-center justify-center w-full text-purple-600">
                                View All
                                <span>
                                    <svg
                                        xmlns="http://www.w3.org/2000/svg"
                                        class="h-5 w-5 ml-2"
                                        viewBox="0 0 20 20"
                                        fill="currentColor"
                                    >
                                        <path
                                            fill-rule="evenodd"
                                            d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                                            clip-rule="evenodd"
                                        />
                                    </svg>
                                </span>
                            </button> -->
                        {#if monit.participants.length > 0}
                            {#each monit.participants as patient}
                                <div class="flex justify-between items-center mt-4">
                                    <a href="/admin/pasien/{ patient }" class="font-semibold">{ patient }</a>
                                    <!-- <svg
                                        xmlns="http://www.w3.org/2000/svg"
                                        class="h-4 w-4 ml-1"
                                        fill="none"
                                        viewBox="0 0 24 24"
                                        stroke="currentColor"
                                        stroke-width="2"
                                    >
                                        <path
                                            stroke-linecap="round"
                                            stroke-linejoin="round"
                                            d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                                        />
                                    </svg> -->
                                </div>
                            {/each}
                        {:else}
                            <div class="text-center italic text-violet-600 bg-violet-100 py-2 px-1 mt-4 w-full rounded-md">
                                <p>Belum ada pasien yang terdaftar pada monitoring ini.</p>
                            </div>
                        {/if}
                    {:else}
                        <div class="text-center italic text-violet-600 bg-violet-100 py-2 px-1 mt-4 w-full rounded-md">
                            <p>Belum ada pasien yang terdaftar pada monitoring ini.</p>
                        </div>
                    {/if}
                </div>
            </div>
        </div>
    </div>
</div>