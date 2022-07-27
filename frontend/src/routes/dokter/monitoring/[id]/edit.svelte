<script>
	import { onMount } from 'svelte';
	import { fade } from 'svelte/transition';
	import { goto } from '$app/navigation';
	import { pageName, storeFields } from '../../../../stores/admin.js';
	import fieldItem from '../../../../components/admin/fieldItem.svelte';
	export let monit
	let data, uname

	console.log(monit)
	
	// Update page title on header
	onMount(async () => {
		pageName.update(() => document.title);
	});

	// Monitoring form fields
	$storeFields = monit.questions; // load from stores
	console.log($storeFields)
	function addMoreField() {
		// add new field
		var nField = $storeFields.length;
		$storeFields[nField] = { id: nField + 1, label: '', quest: '' };
		console.log($storeFields);
	}

	// munculin menu reminder
	let timeMenu;

	const codeRest = monit.code.split('-').slice(1).join("-");

	let formData = {
		"name": monit.name,
		"desc": monit.desc,
		// "code": codeRest,
		"notif": monit.notif,
	}

	// save monitoring
	const submit = async () => {
		const response = await fetch('http://localhost:8080/monit/code/' + monit.code, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                "name": formData.name,
                "host": monit.host,
                "desc": formData.desc,
                // "code": monit.host + '-' + formData.code,
				"notif": formData.notif,
				"questions": $storeFields
            })
        })
		
		// formData.questions = $storeFields
		// formData.host = uname
		// formData.code = uname + '-' + formData.code
		// console.log(response)
		await goto('/admin/monitoring/' + monit.code)
	}
</script>

<script context="module">
	export async function load({ params, fetch }) {
		const response = await fetch('http://localhost:8080/auth/user', {
			headers: {'Content-Type': 'application/json'},
			credentials: 'include',
		})
		
		// console.log(params.id)

		let data = await response.json()
		let uname = data.username
		// console.log(uname)
		
		if (response.status == 200) {
			if (data.role === 'dokter'){
				const response = await fetch('http://localhost:8080/monit/code/' + params.id)
				
				const temp = await response.json()
				if (temp.code == 200) {
					data = temp.data[0]

					if (uname !== data.host){
						return {
							status: 403,
							error: 'Akun anda tidak memiliki akses terhadap halaman ini.'
						}
					}
					
					return {
						props: {
							monit: data
						}
					}
				} else {
					return {
						status: temp.code,
						error: temp.message
					}
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
	<title>Edit - { monit.name }</title>
</svelte:head>

<!-- <svelte:window on:beforeunload={beforeUnload} /> -->

<div in:fade={{delay: 500, duration: 500}} out:fade|local={{duration: 500}}>
	<form action="" on:submit|preventDefault={submit}>
	<!-- Upper section -->
		<div class="grid gap-6 mb-8 md:grid-cols-3 xl:grid-cols-3">
			<!-- Left : Details -->
			<div class="md:col-span-2">
				<h4 class="mb-4 text-lg font-semibold text-gray-600 dark:text-gray-300">Detail</h4>
				<div class="px-5 py-4 mb-8 bg-white rounded-lg shadow-md dark:bg-gray-800">
					<!-- Nama Form -->
					<div class="mb-7">
						<label class="block text-sm mb-3 font-semibold" for="name"> Nama Form Monitoring </label>
						<input
							class="block w-full mt-1 text-sm border rounded-md dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none dark:text-gray-300 form-input py-2 px-3"
							placeholder="Monitoring General"
							type="text"
							id="name"
							bind:value={formData.name}
							required
						/>
					</div>

					<!-- Kode Form -->
					<div class="mb-7">
						<label class="block text-sm mb-3 font-semibold" for="code"> Kode </label>
						{monit.host}-{ codeRest }
						<!-- <input
							class="mt-1 text-sm border rounded-md dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none dark:text-gray-300 form-input py-2 px-3"
							placeholder="Kode form"
							type="text"
							id="code"
							bind:value={formData.code}
							required
						/> -->
					</div>

					<!-- Deskripsi -->
					<div>
						<label class="block text-sm mb-3 font-semibold" for="desc"> Deskripsi </label>
						<textarea
							id="desc"
							cols="30"
							rows="10"
							class="block w-full mt-1 text-sm border rounded-md dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none dark:text-gray-300 form-input py-2 px-3"
							placeholder="Deskripsi"
							bind:value={formData.desc}
						/>
					</div>
				</div>
			</div>

			<!-- Right pengaturan -->
			<div>
				<h4 class="mb-4 text-lg font-semibold text-gray-600 dark:text-gray-300">Pengaturan</h4>
				<div class="px-5 py-4 mb-8 bg-white rounded-lg shadow-md dark:bg-gray-800">
					<!-- <div class="flex justify-between items-center">
						<label class="block text-sm font-semibold" for="reminder">Reminder</label>
						<input
							class="h-5 w-5 accent-purple-600"
							type="checkbox"
							id="reminder"
							bind:checked={timeMenu}
						/>
					</div>

					{#if timeMenu}
						<div class="flex justify-between items-center mt-4">
							<label class="block text-sm font-semibold" for="time">Waktu</label>
							<select
								id="time"
								class="block text-sm border rounded-md bg-white dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none dark:text-gray-300 form-input py-2 px-2"
							>
								<option value="1">Setiap hari</option>
								<option value="2">Setiap minggu</option>
								<option value="3">Setiap bulan</option>
							</select>
						</div>
					{/if}

					<hr class="my-4" />

					<div class="flex justify-between items-center">
						<label class="block text-sm font-semibold" for="openJoin">Open join</label>
						<input class="h-5 w-5 accent-purple-600" type="checkbox" id="openJoin" />
					</div> -->

					<button type="submit"
						class="flex justify-center w-full px-4 py-2 text-sm font-medium leading-5 text-white transition-colors duration-150 bg-purple-600 border border-transparent rounded-lg active:bg-purple-600 hover:bg-purple-700 focus:outline-none focus:shadow-outline-purple"
						
					>
						Simpan
					</button>
				</div>
			</div>
		</div>

		<!-- Bottom Section -->
		<div id="fields-form">
			<div class="flex items-center justify-between mb-4">
				<h4 class="text-lg font-semibold text-gray-600 dark:text-gray-300">Pertanyaan</h4>
				<button
					class="flex items-center justify-between px-4 py-2 text-sm font-medium leading-5 text-white transition-colors duration-150 bg-purple-600 border border-transparent rounded-lg active:bg-purple-600 hover:bg-purple-700 focus:outline-none focus:shadow-outline-purple"
					on:click={addMoreField}
				>
					Tambah pertanyaan
					<span class="ml-2" aria-hidden="true">+</span>
				</button>
			</div>

			{#each $storeFields as item}
				<svelte:component this={fieldItem} objAttributes={item} />
			{/each}
		</div>
	</form>
</div>