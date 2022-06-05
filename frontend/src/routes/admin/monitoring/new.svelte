<script>
	import { onMount } from 'svelte';
	import { pageName, storeFields } from '../stores.js';
	import fieldItem from '../../../components/admin/fieldItem.svelte';

	// Update page title on header
	onMount(() => {
		pageName.update(() => document.title);
	});

	// Monitoring form fields
	$storeFields = [{ id: 1, label: '', quest: '', type: '1' }]; // load from stores

	function addMoreField() {
		// add new field
		var nField = $storeFields.length;
		$storeFields[nField] = { id: nField + 1, label: '', quest: '' };
		console.log($storeFields);
	}

	// munculin menu reminder
	let timeMenu;
</script>

<svelte:head>
	<title>Form Monitoring Baru</title>
</svelte:head>

<!-- <svelte:window on:beforeunload={beforeUnload} /> -->

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
				/>
			</div>

			<!-- Kode Form -->
			<div class="mb-7">
				<label class="block text-sm mb-3 font-semibold" for="code"> Kode </label>
				username-
				<input
					class="mt-1 text-sm border rounded-md dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none dark:text-gray-300 form-input py-2 px-3"
					placeholder="Kode form"
					type="text"
					id="code"
				/>
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
				/>
			</div>
		</div>
	</div>

	<!-- Right pengaturan -->
	<div>
		<h4 class="mb-4 text-lg font-semibold text-gray-600 dark:text-gray-300">Pengaturan</h4>
		<div class="px-5 py-4 mb-8 bg-white rounded-lg shadow-md dark:bg-gray-800">
			<div class="flex justify-between items-center">
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
			</div>
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
