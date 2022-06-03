<script>
	import { onMount } from 'svelte';

	import { pageName } from '../stores';

	onMount(() => {
		pageName.update(() => document.title);
	});
</script>

<svelte:head>
	<title>Form Monitoring Baru</title>
</svelte:head>

<div>
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

	<div class="flex items-center justify-between mb-4">
		<h4 class="text-lg font-semibold text-gray-600 dark:text-gray-300">Pertanyaan</h4>
		<button
			class="flex items-center justify-between px-4 py-2 text-sm font-medium leading-5 text-white transition-colors duration-150 bg-purple-600 border border-transparent rounded-lg active:bg-purple-600 hover:bg-purple-700 focus:outline-none focus:shadow-outline-purple"
		>
			Tambah pertanyaan
			<span class="ml-2" aria-hidden="true">+</span>
		</button>
	</div>

	<div class="px-4 py-3 mb-8 bg-white rounded-lg shadow-md dark:bg-gray-800">
		<!-- Field ID -->
		<div class="flex items-center justify-between mb-4 text-sm font-semibold">
			<p class="italic">Field 1</p>
			<button class="text-red-600 hover:underline">Delete</button>
		</div>

		<!-- Nama Field -->
		<div class="mb-7">
			<label class="block text-sm mb-3 font-semibold" for="field-1-name"> Label </label>
			<input
				class="block w-full mt-1 text-sm border rounded-md dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none dark:text-gray-300 form-input py-2 px-3"
				placeholder="Temperatur"
				type="text"
				id="field-1-name"
			/>
		</div>

		<!-- Tipe jawaban -->
		<div class="mb-7">
			<label for="field-1-type" class="block text-sm mb-3 font-semibold">Tipe Jawaban</label>
			<select
				id="field-1-type"
				class="block mt-1 text-sm border rounded-md bg-white dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none dark:text-gray-300 form-input py-2 px-2"
			>
				<option>Teks pendek</option>
				<option>Numerik</option>
				<option>Yes/No</option>
			</select>
		</div>

		<!-- Pertanyaan -->
		<div>
			<label class="block text-sm mb-3 font-semibold" for="field-1-quest"> Pertanyaan </label>
			<input
				class="block w-full mt-1 text-sm border rounded-md dark:border-gray-600 dark:bg-gray-700 focus:border-purple-400 focus:outline-none dark:text-gray-300 form-input py-2 px-3"
				placeholder="Berapa suhu anda hari ini?"
				type="text"
				id="field-1-quest"
			/>
		</div>
	</div>
</div>
